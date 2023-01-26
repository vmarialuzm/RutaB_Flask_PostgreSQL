from flask import Flask
from flask_migrate import Migrate
from database.db import db
from router.todo import todo_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@18.209.223.249:5432/todos'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(todo_bp)

    migrate = Migrate()
    migrate.init_app(app, db)

    return app

def setup_database(app):
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    app=create_app()
    setup_database(app)
    app.run(debug=True)
