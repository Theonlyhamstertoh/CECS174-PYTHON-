
service = {"Oil change": 35, "Tire rotation": 19, "Car wash": 7}
user_input = input("Enter desired auto service:\n")
if service.get(user_input) == None:
    print("Error: Requested service is not recognized")
else:
    print("You entered:", user_input)
    print(f"cost of {user_input.lower()} ${service[user_input]}")
