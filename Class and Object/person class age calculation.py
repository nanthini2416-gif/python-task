from datetime import date

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob  # dob should be a date object (year, month, day)

    def age(self):
        today = date.today()
        age = today.year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        return age


p = Person("Nanthini", "India", date(1998, 4, 16))

print("Name:", p.name)
print("Country:", p.country)
print("Date of Birth:", p.dob)
print("Age:", p.age())
