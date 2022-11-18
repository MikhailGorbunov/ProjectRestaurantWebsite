from flask import Blueprint, Flask, redirect, render_template, request
from models.booking import Booking

import repositories.table_repository as table_repository
import repositories.customer_repository as customer_repository
import repositories.waiter_repository as waiter_repository
import repositories.booking_repository as booking_repository


bookings_blueprint = Blueprint("bookings", __name__)             # blueprint's name can be different     
# INDEX 

@bookings_blueprint.route("/HIDE/admin/tables")
def bookings():
    bookings = booking_repository.select_all()
    waiters = waiter_repository.select_all()
    customers = customer_repository.select_all()
    tables = table_repository.select_all()
    return render_template("admin/tables/index.html", bookings=bookings, customers=customers, waiters=waiters, tables=tables)



# SHOW
@bookings_blueprint.route("/HIDE/booking/<id>")
def show_booking(id):
    booking = booking_repository.select(id)
    waiter = waiter_repository.select(id)
    table = table_repository.select(id)
    customer = customer_repository.select(id)
    return render_template("admin/bookings/show.html", booking=booking, customer=customer, waiter=waiter, table=table)




# NEW

@bookings_blueprint.route("/HIDE/booking")
def new_booking():
    waiters = waiter_repository.select_all()
    customers = customer_repository.select_all()
    tables = table_repository.select_all()
    bookings = booking_repository.select_all()
    return render_template("admin/bookings/index.html", waiters=waiters, customers=customers, tables=tables, bookings=bookings)

# CREATE

@bookings_blueprint.route("/HIDE/booking", methods=['POST'])
def create_booking():
    capacity = request["capacity"]
    day_time = request["day_time"]
    time = request["time"]                                                 # time might be wrong 
    booked = request["booked"]
    table_id = request["table_id"]
    customer_id = request["customer_id"]
    waiter_id = request["waiter_id"]
    def check_busy():
        if  booked == False:
            new_booking = booking(capacity, day_time, time, booked, table_id, customer_id, waiter_id)
            booking_repository.save(new_booking)
            return redirect("/HIDE")

# EDIT

@bookings_blueprint.route("/HIDE/<id>/edit")
def edit_booking(id):
    booking = booking_repository.select(id)
    waiters = waiter_repository.select_all()
    tables = table_repository.select_all()
    customers = customer_repository.select_all()
    return render_template('admin/bookings/edit.html', booking=booking, customers=customers, waiters=waiters, tables=tables)

# UPDATE 

@bookings_blueprint.route("/HIDE/<id>/update", methods=['POST'])
def update_booking(id):
    capacity = request["capacity"]
    day_time = request["day_time"]
    time = request["time"]                                                 # time might be wrong 
    booked = request['booked']
    table_id = request["table_id"]
    customer_id = request["customer_id"]
    waiter_id = request["waiter_id"]
    if  booked == False:
        new_booking = booking(capacity, day_time, time, booked, table_id, customer_id, waiter_id, id)
        booking_repository.save(new_booking)
        return redirect("/HIDE/booking/<id>")

# DELETE

@bookings_blueprint.route("/HIDE/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/HIDE")