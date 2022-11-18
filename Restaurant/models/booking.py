class Booking:

    def __init__(self, capacity, day_time, time, booked, table_id, customer_id, waiter_id,  id=None):
        self.capacity = capacity
        self.day_time = day_time
        self.time = time
        self.booked = booked
        self.table_id = table_id
        self.customer_id = customer_id
        self.waiter_id = waiter_id
        self.id = id
