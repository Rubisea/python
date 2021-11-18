# Chelsea Rubio Programming Logic and Design (ITSE-1429-51G02)
# Tuesday Nov. 16
 
y = 6
x = [1,2]

# Create list

print("---> Everything in my possesion")

inventory = ["money","slim-jim","pocket knife", "dog"]

# Print variables

print(y)
print(x)

print(inventory)
print(inventory[2])

# Print loop

print("---> Regular loop")

count = 0

while count < 4:
    print(inventory[count])
    count = count + 1

# Second loop

print("---> Backward loop")

count = 3

while count > 0:
    print(inventory[count])
    count = count - 1

# For loop

print("---> The inventory for loop")

for count in inventory:
    print(count)
