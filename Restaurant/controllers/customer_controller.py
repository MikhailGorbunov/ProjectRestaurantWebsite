from flask import Blueprint, Flask, redirect, render_template, request
from models.customer import Customer

import repositories.customer_repository as customer_repository
customers_blueprint = Blueprint("customers", __name__)             # blueprint's name can be different     
# INDEX 

@customers_blueprint.route("/HIDE/admin/customers")
def customers():
    customers = customer_repository.select_all()
    return render_template("admin/customers/index.html", customers=customers)

# NEW

@customers_blueprint.route("/HIDE/reservation")
def new_customer():
    return render_template("admin/customers/customer-new.html")

# CREATE

@customers_blueprint.route("/HIDE", methods=['POST'])
def create_customer():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    number = request["number"]
    new_customer = Customer(first_name, last_name, email, number)
    customer_repository.save(new_customer)
    return redirect("/HIDE")

# EDIT

@customers_blueprint.route("/HIDE/admin/customers/edit")
def edit_customer(id):
    customer = customer_repository.select(id)
    return render_template('admin/customers/edit.html', customer=customer)

# UPDATE 

@customers_blueprint.route("/HIDE/admin/customers/<id>", methods=['POST'])
def update_customer(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    number = request["number"]

    new_customer = Customer(first_name, last_name, email, number, id)
    customer_repository.save(new_customer)
    return redirect("/HIDE")

# DELETE

@customers_blueprint.route("/HIDE/admin/customers/<id>/delete", methods=["POST"])
def delete_customer(id):
    customer_repository.delete(id)
    return redirect("/HIDE")




