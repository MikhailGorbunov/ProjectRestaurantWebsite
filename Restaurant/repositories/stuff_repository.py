from db.run_sql import run_sql
from models.stuff import Stuff
import repositories.customer_repository as customer_repository

def save(stuff):
    sql = "INSERT INTO stuff (f_name, l_name, table_capacity, role) VALUES (%s,%s,%s,%s) RETURNING *"
    values = [stuff.f_name, stuff.l_name, stuff.table_capacity, stuff.role]
    results = run_sql(sql, values)
    id = results[0]['id']
    stuff.id = id
    return stuff

def select_all():
    stuffs = []
    sql = "SELECT * FROM stuff"
    results = run_sql(sql)
    for result in results:
        # customer = stuff_repository.select(result['customer_id'])
        stuff = Stuff(result['f_name'], result['l_name'], result['table_capacity'], result['role'], result['id'])
        stuffs.append(stuff)
    return stuffs

def select(stuff):
    stuff = None
    sql = "SELECT * FROM stuff WHERE id=%s"
    values = [id]
    results = run_sql(sql, values)

 # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    if results:
        result = results[0]
        # customer = stuff_repository.select(result['customer_id'])
        stuff = Stuff(result['f_name'], result['l_name'], result['table_capacity'], result['role'], result['id'])
    return stuff

def delete_all():
    sql = "DELETE FROM stuff"
    run_sql(sql)

def delete(id):
    sql = "DELETE FORM stuff WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def update(stuff):
    sql = "UPDATE stuff SET (f_name, l_name, table_capacity, role) = (%s,%s,%s,%s) WHERE id = %s"
    values = [stuff.f_name, stuff.l_name, stuff.table_capacity, stuff.role, stuff.id]
    run_sql(sql, values)


    