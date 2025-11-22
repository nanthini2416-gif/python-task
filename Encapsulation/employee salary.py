class employee:

    def __init__(self,name):
        self.__name=name
        self.__salary=0.0

    def set_salary(self,amount):

        if amount>0:
            self.__salary=amount
        else:
            print("Invalid salary!")

    def get_salary(self):
        return self.__salary

    def get_name(self):
        return self.__name


emp=employee("Bob")
emp.set_salary(5000)
print(emp.get_salary())

emp.set_salary(-100)
print(emp.get_name())
