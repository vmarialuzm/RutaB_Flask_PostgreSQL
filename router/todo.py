from flask import Blueprint,render_template,redirect,url_for,request
from sqlalchemy.sql import func
from database.db import db
from models.todo import Todo

todo_bp=Blueprint('todo_bp', __name__)

@todo_bp.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@todo_bp.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    body=request.form.get("body")
    new_todo = Todo(title=title,body=body,complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("todo_bp.home"))


@todo_bp.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    update_dt=func.now()
    todo.updated_at=update_dt
    db.session.commit()
    return redirect(url_for("todo_bp.home"))


@todo_bp.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todo_bp.home"))
