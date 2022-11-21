from flask import Blueprint, Flask, redirect, render_template, request
from models.stuff import Stuff
from werkzeug.utils import secure_filename

import repositories.stuff_repository as stuff_repository
stuff_blueprint = Blueprint("stuffs", __name__)             # blueprint's name can be different     
# INDEX 

@stuff_blueprint.route("/HIDE/team")
def stuff():
    stuff = stuff_repository.select_all()
    return render_template("admin/stuff/index.html", stuff=stuff)

# NEW

@stuff_blueprint.route("/HIDE/admin/new")
def new_stuff():
    stuff = stuff_repository.select_all()
    return render_template("admin/stuff/new.html", stuff=stuff)

# CREATE

@stuff_blueprint.route("/HIDE/admin/stuff", methods=['POST'])
def create_stuff():
    # pic = pic.files["avatar"]
    # if not pic:
    #     return 'No pic uploaded', 400
    # filename = secure_filename(pic.filename)
    # mimetype = pic.mimetype


    f_name = request.form["f_name"]
    l_name = request.form["l_name"]
    table_capacity = request.form["table_capacity"]
    role = request.form["role"]
    new_stuff = Stuff(f_name, l_name, table_capacity, role)
    stuff_repository.save(new_stuff)
    return redirect("/HIDE/team")

# EDIT

@stuff_blueprint.route("/HIDE/admin/stuff/<id>/edit")
def edit_stuff(id):
    stuff = stuff_repository.select(id)
    stuffs = stuff_repository.select_all()
    return render_template('admin/stuff/edit.html', stuff=stuff, stuffs=stuffs)

# UPDATE 

@stuff_blueprint.route("/HIDE/admin/stuff/<id>", methods=['POST'])
def update_stuff(id):
    # pic = pic.form["avatar"]
    f_name = request.form["f_name"]
    l_name = request.form["l_name"]
    table_capacity = request.form["table_capacity"]
    role = request.form["role"]
    new_stuff = Stuff(f_name, l_name, table_capacity, role, id)
    stuff_repository.save(new_stuff)
    return redirect("/HIDE/team")

# DELETE

@stuff_blueprint.route("/HIDE/admin/stuff/delete", methods=["POST"])
def delete_stuff(id):
    stuff_repository.delete(id)
    return redirect("/HIDE/team")
