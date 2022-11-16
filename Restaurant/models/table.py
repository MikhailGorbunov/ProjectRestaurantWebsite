class Table:

    def __init__(self, capacity, time_slot, customer_id, waiter_id,  id=None):
        self.capacity = capacity
        self.time_slot = time_slot
        self.customer_id = customer_id
        self.waiter_id = waiter_id
        self.id = id