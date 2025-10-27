from datetime import date

birth_year=int(int(input("Enter your Birth Year:")))
birth_month=int(int(input("Enter your Birth month:")))
birth_day=int(int(input("Enter your Birth day:")))

today=date.today()
age=today.year - birth_year

if(today.month,today.day)<(birth_month,birth_day):
    age-=1
print("Your Age is:",age,"Years")
               
