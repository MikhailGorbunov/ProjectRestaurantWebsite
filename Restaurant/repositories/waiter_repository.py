from db.run_sql import run_sql
from models.waiter import Waiter
import repositories.customer_repository as customer_repository

def save(waiter):
    sql = "INSERT INTO waiters (f_name, l_name, table_capacity) VALUES (%s,%s,%s) RETURNING *"
    values = [waiter.f_name, waiter.l_name, waiter.table_capacity]
    results = run_sql(sql, values)
    id = results[0]['id']
    waiter.id = id
    return waiter

def select_all():
    waiters = []
    sql = "SELECT * FROM waiters"
    results = run_sql(sql)
    for result in results:
        # customer = waiter_repository.select(result['customer_id'])
        waiter = Waiter(result['f_name'], result['l_name'], result['table_capacity'], result['id'])
        waiters.append(waiter)
    return waiters

def select(waiter):
    waiter = None
    sql = "SELECT * FROM waiters WHERE id=%s"
    values = [id]
    results = run_sql(sql, values)

 # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    if results:
        result = results[0]
        # customer = waiter_repository.select(result['customer_id'])
        waiter = Waiter(result['f_name'], result['l_name'], result['table_capacity'], result['id'])
    return waiter

def delete_all():
    sql = "DELETE FROM waiters"
    run_sql(sql)

def delete(id):
    sql = "DELETE FORM waiters WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def update(waiter):
    sql = "UPDATE waiters SET (f_name, l_name, table_capacity, customer_id) = (%s,%s,%s) WHERE id = %s"
    values = [waiter.f_name, waiter.l_name, waiter.capacity, waiter.id]
    run_sql(sql, values)


    