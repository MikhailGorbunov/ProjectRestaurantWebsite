from db.run_sql import run_sql
# from models.table import Table
# from models.customer import Customer
# from models.stuff import stuff
from models.booking import Booking

import repositories.customer_repository as customer_repository
import repositories.stuff_repository as stuff_repository
import repositories.table_repository as table_repository


def save(booking):
    sql = "INSERT INTO bookings(booking_capacity, time, booked, table_id, customer_id, stuff_id) VALUES (%s,%s,%s,%s,%s,%s) RETURNING *"
    values = [booking.booking_capacity, booking.time, booking.booked, booking.table_id.id, booking.customer_id.id, booking.stuff_id.id]
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
        stuff = stuff_repository.select(result['stuff_id'])
        table = table_repository.select(result['table_id'])
        booking = Booking(result['booking_capacity'], result["time"], result["booked"], table, customer, stuff, result['id'])
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
        stuff = stuff_repository.select(result['stuff_id'])
        booking = Booking(result['booking_capacity'], result["time"], result["booked"], table, customer, stuff, result['id'])
    return booking

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def update(booking):
    sql = "UPDATE bookings SET (booking_capacity, time, booked, table_id, customer_id, stuff_id) = (%s,%s,%s,%s,%s,%s) WHERE id=%s"
    values = [booking.booking_capacity, booking.time, True, booking.table_id.id, booking.customer_id.id, booking.stuff_id.id, booking.id]
    run_sql(sql, values)



# --SELECT DATEADD(hour, 2, time) estimated_table_return FROM bookings
# --SELECT date '2027-05-20' + interval '5 minute';
# --SELECT * from bookings
# SELECT time from bookings 
# --SELECT date '2027-05-20' + interval '2 hour' from bookings as estimated_table_return
# --SELECT time '2022-12-01 12:00:00' + integer '5 hour';




# def add_time(id):
#     booking = None
#     sql = "SELECT * FROM bookings WHERE id=%s, DATEADD(hour, 2, time) estimated_table_return"
    
#     values = [id]
#     results = run_sql(sql, values)

#     if booking.booked == True:
#         new_time = booking.estimated_table_return
#         return new_time

# def check_time(id):
#     booking_to_be_checked = booking_repository.select(id)
#     bookings = booking_repository.select_all
#     new_time = booking_repository.add_time(id)
#     for booking in bookings:
#         if booking.time < booking_to_be_checked.date and 
#             booking1 = booking.time
#             return booking1
#     for booking in bookings:
#         booking2 = booking.time
#         return booking2
#     if booking1 < booking_to_be_checked and new_time < booking.time:
#         booking = booking_to_be_checked
#         return booking
# #  ^ the most optimized code i have written so far ^
            
# #
#     for booking in bookings:
#         if booking.time < booking_to_be_checked.date:
#             booking1 = booking.time
#             return booking1
#     for booking in bookings:
#         booking2 = booking.time
#         return booking2
#     if booking1 < booking_to_be_checked and new_time < booking.time:
#         booking = booking_to_be_checked
#         return booking