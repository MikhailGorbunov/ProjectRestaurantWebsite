from flask import Flask, render_template

from controllers.customer_controller import customers_blueprint
from controllers.table_controller import tables_blueprint
from controllers.waiter_controller import waiters_blueprint

app = Flask(__name__)

app.register_blueprint(customers_blueprint)
app.register_blueprint(tables_blueprint)
app.register_blueprint(waiters_blueprint)

@app.route("/HIDE")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

