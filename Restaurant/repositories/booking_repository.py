from db.run_sql import run_sql
from models.table import Table
from models.customer import Customer
from models.waiter import Waiter
from models.booking import Booking

import repositories.customer_repository as customer_repository
import repositories.waiter_repository as waiter_repository
import repositories.table_repository as table_repository

def save(booking):
    sql = "INSERT INTO bookings(capacity, day_time, time, booked, table_id, customer_id, waiter_id) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING *"
    values = [booking.capacity, booking.day_time, booking.time, True, booking.table_id.id, booking.customer_id.id, booking.waiter_id.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id 
    return booking

def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for result in results:
        customer = customer_repository.select(result['customer_id'])
        waiter = waiter_repository.select(result['waiter_id'])
        table = table_repository.select(result['table_id'])
        booking = Booking(result['capacity'], result["day_time"], result["time"], result["booked"], table, customer, waiter, result['id'])
        bookings.append(booking)
    return bookings
    
def select(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id=%s"
    values = [id]
    results = run_sql(sql, values)
# checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    if results:
        result = results[0]
        customer = customer_repository.select(result['customer_id'])
        table = table_repository.select(result['table_id'])
        waiter = waiter_repository.select(result['waiter_id'])
        booking = Booking(result['capacity'],result["day_time"], result["time"], result["booked"], table, customer, waiter, result['id'])
    return booking

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def update(booking):
    sql = "UPDATE bookings SET (capacity, day_time, time, booked, table_id, customer_id, waiter_id) = (%s,%s,%s,%s,%s,%s,%s) WHERE id=%s"
    values = [booking.capacity, booking.day_time, booking.time, True, booking.table.id, booking.customer.id, booking.waiter.id, booking.id]
    run_sql(sql, values)


def add_time(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id=%s, DATEADD (HR, 2, date) AS date"
    values = [id]
    results = run_sql(sql, values)

    if booking.booked == True:
        new_time = booking.time
        return new_time

# god help me 
def check_time(id):
    booking_to_be_checked = booking_repository.select(id)
    bookings = booking_repository.select_all
    new_time = booking_repository.add_time(id)
    for booking in bookings:
        if booking.time < booking_to_be_checked.date:
            booking1 = booking.time
            return booking1
    for booking in bookings:
        booking2 = booking.time
        return booking2
    if booking1 < booking_to_be_checked and new_time < booking.time:
                    
        booking = booking_to_be_checked
        return booking
#  ^ the most optimized code i have written so far ^
            
#
