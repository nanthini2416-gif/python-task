aptitude=int(input("Enter Marks in Aptitude"))
gd=int(input("Enter Marks in GD"))
technical=int(input("Enter Marks in Technical"))
hr=int(input("Enter Marks in HR"))

total=aptitude+gd+technical+hr

if total>=390:
    print("Eligible for salary:30,000")
elif total>=380:
    print("Eligible for salary:28,000")
elif total>=370:
    print("Eligible for salary:25,000")
elif total>=350:
    print("Eligible for salary:20,000")
else:
    print("Not Eligible for job")
