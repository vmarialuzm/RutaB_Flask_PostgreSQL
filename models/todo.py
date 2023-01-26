from database.db import db
from sqlalchemy.sql import func

class Todo(db.Model):
    __tablename__='todo'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body=db.Column(db.String(500))
    complete = db.Column(db.Boolean)
    created_at=db.Column(db.DateTime(timezone=True),default=func.now())
    updated_at=db.Column(db.DateTime(timezone=True))