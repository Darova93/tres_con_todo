from authlib.common.security import generate_token
from flask import Blueprint, request, redirect, jsonify, url_for, current_app, session
from werkzeug.datastructures import ImmutableMultiDict
from flask_cors import cross_origin
from sqlalchemy import select
from os import environ
from database.connection import db_session
from database.models import User
import json

app_route = Blueprint('auth', __name__, url_prefix="/auth")


def get_or_create_user(user: User) -> User:
    query = select(User).where(User.external_id == user.external_id)
    if users := db_session.execute(query).first():
        return users[0]
    db_session.add(user)
    db_session.commit()
    return user

@app_route.route("/login", methods=["POST"])
@cross_origin()
def login():
    from app import oauth
    oauth.register(
        name='google',
        client_id=environ.get("GOOGLE_CLIENT_ID", None),
        client_secret=environ.get("GOOGLE_CLIENT_SECRET", None),
        server_metadata_url=environ.get("GOOGLE_DISCOVERY_URL", None),
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
    redirect_uri = url_for('auth.callback', _external=True)
    session['nonce'] = generate_token()
    response = oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])
    print(response.location)
    return response

@app_route.route("/login/callback")
@cross_origin()
def callback():
    from app import oauth
    token = oauth.google.authorize_access_token()
    google_user = oauth.google.parse_id_token(token, nonce=session['nonce'])

    user = User(
        external_id=google_user["sub"],
        name=google_user["name"],
        email=google_user["email"],
        profile_picture=google_user["picture"],
        token=google_user["token"]
    )

    db_user = get_or_create_user(user)
    return jsonify({
        "email": db_user.email,
        "profile_picture": db_user.profile_picture,
        "name": db_user.name,
        "token": db_user.token
    })

@app_route.route("/logout")
@cross_origin()
def logout():
    return redirect("/")
