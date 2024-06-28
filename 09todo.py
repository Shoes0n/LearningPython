#create program to ask to enter n num of toda and display it.
todos = []

total_todo = int(input("Enter total number of todo: "))

for i in range(1,total_todo):
    todo = input(f"Enter todo {i}: ")
    todos.append(todo)


print("\n--------------------\n")
print("All todos are: ")


#Display all result
for todo in todos:
    print(todo)