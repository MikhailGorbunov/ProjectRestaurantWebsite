from flask import Blueprint, Flask, redirect, render_template, request
from models.waiter import Waiter
from werkzeug.utils import secure_filename

import repositories.waiter_repository as waiter_repository
waiters_blueprint = Blueprint("waiters", __name__)             # blueprint's name can be different     
# INDEX 

@waiters_blueprint.route("/HIDE/team")
def waiters():
    waiters = waiter_repository.select_all()
    return render_template("admin/waiters/index.html", waiters=waiters)

# NEW

@waiters_blueprint.route("/HIDE/admin/new")
def new_waiter():
    waiters = waiter_repository.select_all()
    return render_template("admin/waiters/new.html", waiters=waiters)

# CREATE

@waiters_blueprint.route("/HIDE/admin/waiters", methods=['POST'])
def create_waiter():
    # pic = pic.files["avatar"]
    # if not pic:
    #     return 'No pic uploaded', 400
    # filename = secure_filename(pic.filename)
    # mimetype = pic.mimetype


    f_name = request.form["f_name"]
    l_name = request.form["l_name"]
    capacity = request.form["capacity"]
    new_waiter = Waiter(f_name, l_name, capacity)
    waiter_repository.save(new_waiter)
    return redirect("/HIDE/team")

# EDIT

@waiters_blueprint.route("/HIDE/admin/waiters/<id>/edit")
def edit_waiter(id):
    waiter = waiter_repository.select(id)
    return render_template('admin/waiters/edit.html', waiter=waiter)

# UPDATE 

@waiters_blueprint.route("/HIDE/admin/waiters/<id>", methods=['POST'])
def update_waiter(id):
    # pic = pic.form["avatar"]
    f_name = request.form["f_name"]
    l_name = request.form["l_name"]
    capacity = request.form["capacity"]
    new_waiter = Waiter(f_name, l_name, table, id)
    waiter_repository.save(new_waiter)
    return redirect("/HIDE/team")

# DELETE

@waiters_blueprint.route("/HIDE/admin/waiters/delete", methods=["POST"])
def delete_waiter(id):
    waiter_repository.delete(id)
    return redirect("/HIDE/team")
