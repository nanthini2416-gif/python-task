quantity=int(input("Enter the Quantity"))
price=float(input("Enter the price per item"))
total_cost=quantity*price

if total_cost>1000:
    discount=total_cost*0.10
    total_cost-=discount
    print("Discount Applied 10%")
else:
    print("No Discount Applied")
print("Total Cost:",total_cost)
