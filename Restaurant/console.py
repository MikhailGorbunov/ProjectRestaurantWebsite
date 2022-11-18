# for debuging 
import pdb

#  Import models/classes 
from models.customer import Customer
from models.table import Table
from models.waiter import Waiter
from models.booking import Booking

#  Import repositories 
import repositories.customer_repository as customer_repository
import repositories.table_repository as table_repository
import repositories.waiter_repository as waiter_repository
import repositories.booking_repository as booking_repository

# Functions that are linked to repositories


#____Delete_all functions to clean the table instead of stacking data 
customer_repository.delete_all()
table_repository.delete_all()
waiter_repository.delete_all()
booking_repository.delete_all()

#____Save date to db table / sql
#  DATE format YYYY-MM-DD hh:mm:ss
# ___________Customer______________
customer1 = Customer("Jakub", "Cahil", "jakub@gmail.com", "+078948596") 
customer2 = Customer("Nicolas", "Bassett"," nicolas@gmail.com", "+44012345") 
customer3 = Customer("Kenneth", "Mckinney", "kenneth.gmail.com", "+44012345") 
customer4 = Customer("Tobias", "Moyer", "tobias@gmail", "123456") 
customer5 = Customer("Alexandre", "Ryan","alexndre@gmail", "123456") 
customer6 = Customer("Caelan", "Cleveland", "caelan@gmail", "123456") 
customer7 = Customer("Jordanna", "Gonzales", "jordanna@gmail", "123456") 
customer8 = Customer("Mack", "Rennie", "mack@gmail", "123456") 

customer_repository.save(customer1)
customer_repository.save(customer2)
customer_repository.save(customer3)
customer_repository.save(customer4)
customer_repository.save(customer5)
customer_repository.save(customer6)
customer_repository.save(customer7)
customer_repository.save(customer8)

# customer9 = Customer("Name", "Surname", "email", 0, "123456")
# customer10 = Customer("Name", "Surname", "email", 0, "123456")
# customer11 = Customer("Name", "Surname", "email", 0, "123456")
# customer12 = Customer("Name", "Surname", "email", 0, "123456")
# customer13 = Customer("Name", "Surname", "email", 0, "123456")
# customer14 = Customer("Name", "Surname", "email", 0, "123456")
# customer15 = Customer("Name", "Surname", "email", 0, "123456")
# customer16 = Customer("Name", "Surname", "email", 0, "123456")
# customer17 = Customer("Name", "Surname", "email", 0, "123456")
# customer18 = Customer("Name", "Surname", "email", 0, "123456")
# customer19 = Customer("Name", "Surname", "email", 0, "123456")
# customer20 = Customer("Name", "Surname", "email", 0, "123456")
# customer21 = Customer("Name", "Surname", "email", 0, "123456")
# customer22 = Customer("Name", "Surname", "email", 0, "123456")
# customer23 = Customer("Name", "Surname", "email", 0, "123456")
# customer24 = Customer("Name", "Surname", "email", 0, "123456")
# customer25 = Customer("Name", "Surname", "email", 0, "123456")
# customer26 = Customer("Name", "Surname", "email", 0, "123456")




# customer_repository.save(customer9)
# customer_repository.save(customer10)
# customer_repository.save(customer11)
# customer_repository.save(customer12)
# customer_repository.save(customer13)
# customer_repository.save(customer14)
# customer_repository.save(customer15)
# customer_repository.save(customer16)
# customer_repository.save(customer17)
# customer_repository.save(customer18)
# customer_repository.save(customer19)
# customer_repository.save(customer20)
# customer_repository.save(customer21)
# customer_repository.save(customer22)
# customer_repository.save(customer23)
# customer_repository.save(customer24)
# customer_repository.save(customer25)
# customer_repository.save(customer26)


# ___________Waiter______________

# Deacon Parker
# Annabell Mackie

waiter1 = Waiter("Lucie", "White", 2)
waiter2 = Waiter("Elana", "Whitfield", 2)
# waiter1 = Waiter("Deacon", "Parker", 2, )

waiter_repository.save(waiter1)
waiter_repository.save(waiter2)


#___________Table_______________

table1 = Table(4)
table2 = Table(4)
table3 = Table(4)

table_repository.save(table1)
table_repository.save(table2)
table_repository.save(table3)

# table1_14_00 = Table(4, "2022-12-01 14:00:00", customer9,waiter1 )
# table2_14_00 = Table(4, "2022-12-01 14:00:00", customer10,waiter2 )
# table1_14_30 = Table(4, "2022-12-01 14:30:00", customer11,waiter1 )
# table2_14_30 = Table(4, "2022-12-01 14:30:00", customer12,waiter2 )

# table1_15_00 = Table(4, "2022-12-01 15:00:00", customer13,waiter1 )
# table2_15_00 = Table(4, "2022-12-01 15:00:00", customer14,waiter2 )
# table1_15_30 = Table(4, "2022-12-01 15:30:00", customer15,waiter1 )
# table2_15_30 = Table(4, "2022-12-01 15:30:00", customer16,waiter2 )

# table1_16_00 = Table(4, "2022-12-01 16:00:00", customer17,waiter1 )
# table2_16_00 = Table(4, "2022-12-01 16:00:00", customer18,waiter2 )
# table1_16_30 = Table(4, "2022-12-01 16:30:00", customer19,waiter1 )
# table2_16_30 = Table(4, "2022-12-01 16:30:00", customer20,waiter2 )

# table1_17_00 = Table(4, "2022-12-01 17:00:00", customer21,waiter1 )
# table2_17_00 = Table(4, "2022-12-01 17:00:00", customer22,waiter2 )
# table1_17_30 = Table(4, "2022-12-01 17:30:00", customer23,waiter1 )
# table2_17_30 = Table(4, "2022-12-01 17:30:00", customer24,waiter2 )

# table1_18_00 = Table(4, "2022-12-01 18:00:00", customer23,waiter1 )
# table2_18_00 = Table(4, "2022-12-01 18:00:00", customer24,waiter2 )



# table1_2 = Table(4, "2022-12-01 14:00:00", "error", "error" )
# table2_2 = Table(4, "2022-12-01 14:00:00", "error", "error" )

# table1_3 = Table(4, "2022-12-01 16:00:00", "error", "error" )
# table2_3 = Table(4, "2022-12-01 16:00:00", "error", "error" )

# table1_4 = Table(4, "2022-12-01 18:00:00", "error", "error" )
# table2_4 = Table(4, "2022-12-01 18:00:00", "error", "error")

# table1 = Table(2, , )



# table_repository.save(table2_12_30)

# table_repository.save(table1_13_00)
# table_repository.save(table2_13_00)
# table_repository.save(table1_15_30)
# table_repository.save(table2_13_30)

# table_repository.save(table1_14_00)
# table_repository.save(table2_14_00)
# table_repository.save(table1_14_30)
# table_repository.save(table2_14_30)

# table_repository.save(table1_15_00)
# table_repository.save(table2_15_00)
# table_repository.save(table1_15_30)
# table_repository.save(table2_15_30)

# table_repository.save(table1_16_00)
# table_repository.save(table2_16_00)
# table_repository.save(table1_16_30)
# table_repository.save(table2_16_30)

# table_repository.save(table1_17_00)
# table_repository.save(table2_17_00)
# table_repository.save(table1_17_30)
# table_repository.save(table2_17_30)

# table_repository.save(table1_18_00)
# table_repository.save(table2_18_00)

# _________Bookings 


booking1_12_00 = Booking(2, '2022-12-01', "12:00", True, table1, customer1,waiter1 )
booking2_12_00 = Booking(4, '2022-12-01', "12:00", True, table2, customer2,waiter2 )
booking1_12_30 = Booking(2, '2022-12-01', "12:30", True, table1,customer3,waiter1 )
booking2_12_30 = Booking(4, '2022-12-01', "12:30", True, table2, customer4,waiter2 )

booking1_13_00 = Booking(4, '2022-12-01', "13:00", True, table3, customer5,waiter1 )
booking2_13_00 = Booking(3, '2022-12-01', "13:00", True, table1, customer6,waiter2 )
booking1_15_30 = Booking(4, '2022-12-01', "15:30", True, table2, customer7,waiter1 )
booking2_13_30 = Booking(4, '2022-12-01', "13:30:", True, table1, customer8,waiter2 )



booking_repository.save(booking1_12_00)
booking_repository.save(booking2_12_00)
booking_repository.save(booking1_12_30)
booking_repository.save(booking2_12_30)

booking_repository.save(booking1_13_00)
booking_repository.save(booking2_13_00)
booking_repository.save(booking1_15_30)
booking_repository.save(booking2_13_30)