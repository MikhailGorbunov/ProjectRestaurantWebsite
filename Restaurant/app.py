from flask import Flask, render_template

from controllers.customer_controller import customers_blueprint
from controllers.table_controller import tables_blueprint
from controllers.stuff_controller import stuff_blueprint
from controllers.booking_controller import bookings_blueprint


app = Flask(__name__)

app.register_blueprint(customers_blueprint)
app.register_blueprint(tables_blueprint)
app.register_blueprint(stuff_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route("/HIDE")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/HIDE/reservation_policy")
def policy():
    return render_template('pages/policy.html')
