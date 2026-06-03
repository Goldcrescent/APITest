from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '171869704e339bc29182a859942581e8'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/users.db'

    db.init_app(app)
    bcrypt.init_app(app)

    try:
        from routes.auth import auth_bp
        app.register_blueprint(auth_bp)
    except ImportError:
        pass

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)