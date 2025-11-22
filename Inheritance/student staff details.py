class School:
    
    def information(self, name, mail, mobile, address):
        self.name = name
        self.mail = mail
        self.mobile = mobile
        self.address = address


class Staff(School):
    
    def staff_information(self, name, mail, mobile, address, dept):
    
        School.information(self, name, mail, mobile, address)
        self.dept = dept

        print("\n----- STAFF INFORMATION -----")
        print("Name:", self.name)
        print("Email:", self.mail)
        print("Mobile:", self.mobile)
        print("Address:", self.address)
        print("Department:", self.dept)


class Student(School):
    
    def student_information(self, name, mail, mobile, address, dept):
        
        School.information(self, name, mail, mobile, address)
        self.dept = dept

        print("\n----- STUDENT INFORMATION -----")
        print("Name:", self.name)
        print("Email:", self.mail)
        print("Mobile:", self.mobile)
        print("Address:", self.address)
        print("Department:", self.dept)



choice = input("Enter 'staff' or 'student': ").strip().lower()

if choice == "staff":
    name = input("Enter staff name: ")
    mail = input("Enter staff email: ")
    mobile = input("Enter staff mobile: ")
    address = input("Enter staff address: ")
    dept = input("Enter department: ")

    s = Staff()
    s.staff_information(name, mail, mobile, address, dept)

elif choice == "student":
    name = input("Enter student name: ")
    mail = input("Enter student email: ")
    mobile = input("Enter student mobile: ")
    address = input("Enter student address: ")
    dept = input("Enter department: ")

    st = Student()
    st.student_information(name, mail, mobile, address, dept)

else:
    print("Invalid choice! Please enter either 'staff' or 'student'.")
