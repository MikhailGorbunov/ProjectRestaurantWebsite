from flask import Blueprint, Flask, redirect, render_template, request
from models.table import Table

import repositories.table_repository as table_repository
import repositories.customer_repository as customer_repository
import repositories.stuff_repository as stuff_repository


tables_blueprint = Blueprint("tables", __name__)             # blueprint's name can be different     
# INDEX 

@tables_blueprint.route("/HIDE/admin/tables")
def tables():
    tables = table_repository.select_all()
    return render_template("admin/tables/index.html", tables=tables)

# NEW

@tables_blueprint.route("/HIDE/admin/table-new")
def new_table():
    stuff = stuff_repository.select_all()
    customers = customer_repository.select_all()
    return render_template("admin/tables/table-new.html", stuffs=stuff, customers=customers)

# CREATE

@tables_blueprint.route("/HIDE/admin/tables", methods=['POST'])
def create_table():
    capacity = request["capacity"]
    time_slot = request["time_slot"]                                                 # time might be wrong 
    customer_id = request["customer_id"]
    stuff_id = request["stuff_id"]
    new_table = Table(capacity, time_slot, customer_id, stuff_id)
    table_repository.save(new_table)
    return redirect("/HIDE/admin/tables")

# EDIT

@tables_blueprint.route("/HIDE/reservation")
def edit_table():
    table = table_repository.select_all()
    stuff = stuff_repository.select_all()
    customers = customer_repository.select_all()
    return render_template('admin/tables/edit.html', table=table, customers=customers, stuff=stuff)

# UPDATE 

@tables_blueprint.route("/HIDE/restaurants/<id>", methods=['POST'])
def update_table(id):
    capacity = request["capacity"]
    time_slot = request["time_slot"]                                                 # time might be wrong 
    customer_id = request["customer_id"]
    stuff_id = request["stuff_id"]
    new_table = Table(capacity, time_slot, customer_id, stuff_id, id)
    table_repository.save(new_table)
    return redirect("/HIDE")

# DELETE

@tables_blueprint.route("/HIDE/admin/tables/delete", methods=["POST"])
def delete_table(id):
    table_repository.delete(id)
    return redirect("/HIDE/admin/tables")
