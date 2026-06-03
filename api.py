from flask import Flask
from APITest.routes.extensions import db, bcrypt

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '171869704e339bc29182a859942581e8'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    bcrypt.init_app(app)

    from routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)