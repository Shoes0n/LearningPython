#Display person age from his/her birth year
birth_year = int(input("Enter birth year: "))
age = 2024 - birth_year



#print(f"Your age is {age}")
if age >= 18:
    print("You are voter")

else:
    print("You are not voter")