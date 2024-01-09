import datetime


def age_calculator(y, m, d):
    today = datetime.datetime.now().date()
    date_of_birth = datetime.date(y, m, d)
    age = int((today - date_of_birth).days / 365.25)
    print("Your present age is", age)


birth_date = input("Enter your DOB in dd-mm-yyyy format: ")
# for example 1999-10-12

date, month, year = map(int, birth_date.split("-"))
age_calculator(year, month, date)
