class student:

    def __init__(self,name):
        self.__name=name
        self.__grades=[]


    def add_grade(self,grade):
        self.__grades.append(grade)

    def get_average(self):
        if len(self.__grades)==0:
            return 0
        return sum(self.__grades)/len(self.__grades)

    def get_name(self):
        return self.__name


student=student("Alice")
student.add_grade(85)
student.add_grade(90)
print(student.get_average())
print(student.get_name())
