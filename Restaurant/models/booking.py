class Booking:

    def __init__(self, booking_capacity, time, booked, table_id, customer_id, stuff_id,  id=None):
        self.booking_capacity = booking_capacity
        self.time = time
        self.booked = booked
        self.table_id = table_id
        self.customer_id = customer_id
        self.stuff_id = stuff_id
        self.id = id
