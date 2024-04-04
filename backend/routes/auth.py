from requests import get, post
from flask import Blueprint, request, redirect, jsonify
from flask_cors import cross_origin
from sqlalchemy import select
from oauthlib.oauth2 import WebApplicationClient
from os import environ
from database.connection import db_session
from database.models import User
import json


app_route = Blueprint('auth', __name__, url_prefix="/auth")


def get_or_create_user(user: User) -> User:
    query = select(User).where(User.external_id == user.external_id)
    if users := db_session.execute(query).first():
        users[0].token = user.token
        user = users[0]
    else:
        db_session.add(user)
    db_session.commit()
    return user

def redirect_uri(request) -> str:
    return "https://" + request.host + environ.get("BACKEND_PATH", "") + request.path

@app_route.route("/login", methods=["POST"])
@cross_origin()
def login():
    client_id = environ.get("GOOGLE_CLIENT_ID", None)
    authorization_endpoint = environ.get("GOOGLE_AUTHORIZATION_ENDPOINT", None)

    request_uri = WebApplicationClient(client_id).prepare_request_uri(
        authorization_endpoint,
        redirect_uri=redirect_uri(request) + "/callback",
        scope=["openid", "email", "profile"],
    )
    return jsonify({"auth_url": request_uri})

@app_route.route("/login/callback")
@cross_origin()
def callback():
    code = request.args.get("code")
    token_endpoint = environ.get("GOOGLE_TOKEN_ENDPOINT", "")
    secret = environ.get("GOOGLE_CLIENT_SECRET", None)
    client_id = environ.get("GOOGLE_CLIENT_ID", None)
    client = WebApplicationClient(client_id)
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url.replace("http://", "https://"),
        redirect_url=redirect_uri(request),
        code=code
    )
    token_response_raw = post(
        token_url,
        headers=headers,
        data=body,
        auth=(client_id, secret), # type: ignore
    )
    token_response = token_response_raw.json()
    client.parse_request_body_response(json.dumps(token_response))
    userinfo_endpoint = environ.get("GOOGLE_USER_INFO_ENDPOINT", None)
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = get(uri, headers=headers, data=body).json()

    user = User(
        external_id=userinfo_response["sub"],
        name=userinfo_response["name"],
        email=userinfo_response["email"],
        profile_picture=userinfo_response["picture"],
        token=token_response["access_token"]
    )

    db_user = get_or_create_user(user)
    return redirect(
        f"https://{request.host}?token={db_user.token}&email={db_user.email}&profile_picture={db_user.profile_picture}&name={db_user.name}"
    )

@app_route.route("/logout")
@cross_origin()
def logout():
    return redirect("/")
