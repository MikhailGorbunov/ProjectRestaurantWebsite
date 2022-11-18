from db.run_sql import run_sql
from models.customer import Customer

import repositories.table_repository as table_repository

def save(customer):
    sql = "INSERT INTO customers (first_name, last_name, email, phone_number) VALUES (%s,%s,%s,%s) RETURNING *"
    values = [customer.first_name, customer.last_name, customer.email, customer.phone_number]
    results = run_sql(sql, values)
    id = results[0]['id']
    customer.id = id 
    return customer


def select_all():
    customers = []
    sql = "SELECT * FROM customers"
    results = run_sql(sql)

    for result in results:
        customer = Customer(result['first_name'],result['last_name'], result['email'], result['phone_number'], result['id'])
        customers.append(customer)
    return customers

def select(id):
    customer = None
    sql = "SELECT * FROM customers WHERE id=%s"
    values = [id]
    results = run_sql(sql, values)
# checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly'     
    if results:
        result = results[0]
        customer = Customer(result['first_name'],result['last_name'], result['email'], result['phone_number'], result['id'])

def delete_all():
    sql = "DELETE FROM customers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM customers WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def update(customer):
    sql = "UPDATE customers SET (first_name, last_name, email, phone_number) = (%s,%s,%s,%s) WHERE id=%s"
    values = [customer.first_name, customer.last_name, customer.email, customer.phone_number, customer.id]
    run_sql(sql, values)


