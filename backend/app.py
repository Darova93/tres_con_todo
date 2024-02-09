from flask import Flask
from database.connection import db_session, init_db
from routes import ROUTES

init_db()
app = Flask(__name__)
app.config["CORS_HEADERS"] = "Content-Type"

for route in ROUTES:
    app.register_blueprint(route)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
