#Find and replace
string = "It's Thanksgiving day. It's my birthday,too!"
print string
print string.find("day")
string = string.replace("day", "month", 1)
print string

#Min and max
x = [23,5,89, 28, -4, -10, 65]
print x
print max(x)
print min(x)

#First and Last
x = ["hi", 3, 67, 12, "five", 10]
print x[0], x[len(x) - 1]

#New List
x = [12, -5, 28, 34, -45, -2, 27, 66, 90, 21]
print x
x.sort()
print x
first_list = x[:5]
second_list = x[5 : 10]
print first_list
print second_list
second_list.insert(0, first_list)
print second_list