cls_held=int(input("Enter Number of class held"))
cls_attend=int(input("Enter Number of Class Attend"))

attendance=(cls_attend/cls_held)*100

if attendance>=75:
    print("Allowed to sit in Exam")
else:
    print("Not Allowed to sit Exam")
    
