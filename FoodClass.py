class Customer:
    def __init__(self, customerid, name, address, email, phone, member_status):
        self.customerid = customerid
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.member_status = member_status
    

    def get_customerid(self):
        return self.__customerid
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_email(self):
        return self.__email
    
    def get_phone(self):
        return self.__phone
    
    def get_member_status(self):
        return self.__member_status


class Transaction:
    def __init__(self, date, item_name, cost, customerid):
        self.date = date
        self.item_name = item_name
        self.cost = cost
        self.customerid = customerid
    

    def get_date(self):
        return self.__date
    
    def get_item_name(self):
        return self.__item_name
    
    def get_cost(self):
        return self.__cost
    
    def get_customerid(self):
        return self.__customerid