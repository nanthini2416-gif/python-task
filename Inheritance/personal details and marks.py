class Personal:
    
    def information(self, name, email, mobile, address):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.address = address


class Educational(Personal):
    
    def information(self, name, email, mobile, address, marks1, marks2, marks3, total, percentage):
    
        Personal.information(self, name, email, mobile, address)
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        self.total = total
        self.percentage = percentage

    
        print("Name:", self.name)
        print("Email:", self.email)
        print("Mobile:", self.mobile)
        print("Address:", self.address)
        print("Marks 1:", self.marks1)
        print("Marks 2:", self.marks2)
        print("Marks 3:", self.marks3)
        print("Total:", self.total)
        print("Percentage:", self.percentage)

student = Educational()
student.information("Nanthini", "nanthu@gmail.com", "9876543210", "Madurai", 85, 90, 88, 263, 87.67)
