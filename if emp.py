salary=float(input("Enter your Salary"))
years=int(input("Enter years of service"))
if years>5:
    bonus=salary*0.05
    print("Bonus Amount:",bonus)
    print("Net salary After Bonus",salary+bonus)
else:
    print("No Bonus")
