class Student:
    def __init__(self, student_id, name, dob, classification):
        self.student_id = student_id
        self.name = name
        self.dob = dob.split('/')
        self.classification = classification
    
    def calculate_age(self, current_date):
        birth_month, birth_day, birth_year = self.dob
        current_month, current_day, current_year = current_date.split('/')
        
        age = current_year - birth_year
        if (current_month < birth_month) or (current_month == birth_month and current_day < birth_day):
            age -= 1

        
        
    def registration_dates(self):
        if self.classification == 'Sr':
            return "4/1 thru 4/3"
        elif self.classification == 'Jr':
            return "4/4 thru 4/6"
        elif self.classification == 'S':
            return "4/7 thru 4/9"
        elif self.classification == 'F':
            return "4/10 thru 4/12"
    

    def get_age(self, current_date):
        return self.calculate_age(current_date)
    

    def get_registration_dates(self):
        return self.registration_dates()