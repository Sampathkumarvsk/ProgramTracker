# Using Join
list1 = ["apple","banana","citrus","orange"]
string = ",".join(list1)
print(string)

# Using Map Join
list1 = ["apple","banana","citrus","orange",11,12]
string = ",".join(map(str,list1))
print(string)

# Using Iterable
string = ",".join([str(elements) for elements in list1])
print(string)


list2 = ["apple","banana","citrus","orange"]
stringEle = ""
for element in list2:
    stringEle = stringEle + " "+ element
print(stringEle)