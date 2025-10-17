cities=[]

for i in range(5):
    city = input(f"Enter city {i+1}: ")
    cities.append(city)

print("\nYour list of cities:", cities)


city_remove = input("Enter the name of the city to remove: ")


if city_remove in cities:
    
    cities.remove(city_remove)
    
    print("\nUpdated list of cities:", cities)
else:
    print(f"\nCity '{city_remove}' not found in the list.")
