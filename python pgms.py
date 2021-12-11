# interchange first and last elements in a list
def swap(x):
    y = len(x)
    temp = x[0]
    x[0] = x[y - 1]
    x[y-1] = temp
    return x
x = [13, 24, 8, 55, 22]
print(swap(x))


# find the smallest and largest number in a list
list = [10, 15, 4, 22, 50]
print("smallest element is: ", min(list))
print("largest element is : ", max(list))


# print even numbers in a list
list = [10, 15, 4, 33, 22, 67, 18]
for i in list:
    if i % 2 == 0:
        print(i, end= " ")


# print odd numbers in a list
list = [10, 15, 4, 33, 22, 67, 18]
for i in list:
    if i % 2 != 0:
        print(i, end= " ")


# print positive numbers in a list
list = [12, -5, 0, 26, -32, 42, -65]
for i in list:
    if i >= 0:
        print(i, end= " ")



# Append Items
x = ["apple", "banana", "cherry"]
x.append("orange")
print(x)

# extend items
x = ["apple", "banana", "cherry"]
y = ["mango", "pineapple", "papaya"]
x.extend(y)
print(x)

# List Length
x = ["apple", "banana", "cherry"]
print(len(x))

# print negative numbers in a list
list = [12, -5, 0, 26, -32, 42, -65]
for i in list:
    if i < 0:
        print(i, end= " ")


# convert fahrenheit to celsius.
temperature = float(input("Enter temperature in fahrenheit: "))
celsius = (temperature - 32) * 5 / 9
print("Temperature in celsius: ", celsius)


# print maximum and minimum number in a tuple
t = tuple()
n = int(input("Total number of values in tuple"))
for i in range(n):
    a = input("Enter elements")
    t = t + (a,)
    print("maximum value =", max(t))
    print("minimum value =", min(t))


# create a list and  use the functions append() and extend() len() membership(in, not in)
# Append Items
x = ["apple", "banana", "cherry"]
x.append("orange")
print(x)

# Extend List
x = ["apple", "banana", "cherry"]
y = ["mango", "pineapple", "papaya"]
x.extend(y)
print(x)

# List Length
x = ["apple", "banana", "cherry"]
print(len(x))

# membership(in, not in)
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
for item in list1:
    if item in list2:
        print("overlapping")
    else:
        print("not overlapping")


x = 24
y = 20
list = [10, 20, 30, 40, 50];
if ( x not in list ):
    print("x is not present in the given list")
else:
    print("x is present in the given list")

if ( y in list ):
    print("y is present in the given list")
else:
    print("y is present not in the given list")




