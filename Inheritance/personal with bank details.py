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


class Bank(Educational):
    
    def information(self, name, email, mobile, address,
                    marks1, marks2, marks3, total, percentage,
                    acc_num, branch_name, bank_name, ifsc_code, available_balance):
        
        
        Educational.information(self, name, email, mobile, address, marks1, marks2, marks3, total, percentage)
        
        self.acc_num = acc_num
        self.branch_name = branch_name
        self.bank_name = bank_name
        self.ifsc_code = ifsc_code
        self.available_balance = available_balance

        
        print("----- Personal Information -----")
        print("Name:", self.name)
        print("Email:", self.email)
        print("Mobile:", self.mobile)
        print("Address:", self.address)

        print("\n----- Educational Information -----")
        print("Marks 1:", self.marks1)
        print("Marks 2:", self.marks2)
        print("Marks 3:", self.marks3)
        print("Total:", self.total)
        print("Percentage:", self.percentage)

        print("\n----- Bank Information -----")
        print("Account Number:", self.acc_num)
        print("Branch Name:", self.branch_name)
        print("Bank Name:", self.bank_name)
        print("IFSC Code:", self.ifsc_code)
        print("Available Balance:", self.available_balance)



customer = Bank()
customer.information(
    "Nanthini", "nanthu@gmail.com", "9876543210", "Madurai",
    85, 90, 88, 263, 87.67,
    "1234567890", "Kumaram Branch", "SBI Bank", "ABC12345", 50000
)
