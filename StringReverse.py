# Reverse the String
#Slicing Method
string = "Madam"
print(string[::-1])

#ReverseMethod
String = "Madam"
print("".join(reversed(String)))

#For Loop
strReverse = ""
for i in String:
    strReverse = i + strReverse
print(strReverse)

#While loop
strReverse = ""
count = len(strReverse)
while count > 0:
    strReverse += string[count-1]
    count= count - 1
print(strReverse)
