import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

order_total = 0


#customer = fc.Customer(570,'Danni Sellyar','97 Mitchell Way Hewitt Texas 76712','dsellyarft@gmpg.org', '254-555-9362', 'False')
customer = fc.Customer(569,'Aubree Himsworth','1172 Moulton Hill Waco Texas 76710','ahimsworthfs@list-manage.com', '254-555-2273', 'True')


print('Name:',customer.get_name())
print('Phone:',customer.get_phone())
for key in dict:
    if dict[key][3] == customer.get_customerid():
        order_total += dict[key][2]
        print(f'Order Item: {dict[key][1]}    Price: ${dict[key][2]:.2f}')
print(f'Total cost: ${order_total:.2f}')
if customer.get_member_status() == 'True':
    member_discount = order_total * 0.2
    discounted_total = order_total * 0.8
    print(f'Member discount: ${member_discount:.2f}')
    print(f'Total cost after discount: ${discounted_total:.2f}')