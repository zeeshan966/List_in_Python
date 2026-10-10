
# List in Python.

# List is Data Structure in python.
# List is data type in python.
# List is mutable in python.
# List follows the ordered method.
# List follows indexing in python.
# List contains multiple type of data.
# It is define square brackets.

print("Welcome to Our List Topic")

data = ['Apple','Banana','Grapes','Papaya','Mango',10,20,30,40,50]
print(data)

# Access the elements throw indices.
print(data[0])
print(data[1])
print(data[2])

# find the length of list using len() method.

print(len(data))

# Loop on a list.

for each in data:
    print(each)


# Membership operator on a list


print('Banana' in data)


print('Zeeshan' not in data)

# insert item on a list.


data.insert(1,'Milk')
print(data)

# check the type of list.

print(type(data))

# Slicing on a list.

print(data[0:])
print(data[4:7])
print(data[3:5])

print(data[-1])
print(data[-5:-1])
