import StudentClass as sc

def main():
    studentID = input("Insert ID:")
    studentName = input("Insert name:")
    studentDOB = input("Insert date of birth:")
    studentClassification = input("Insert classification:")
    student1 = sc.Student(studentID, studentName, studentDOB, studentClassification)
    current_date = input("Insert current date:")


    print(student1.get_age(current_date))
    print(student1.get_registration_dates())

main()