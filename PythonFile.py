print("hello");
name="world is good"
age =2
print(name ,"Age is:", age)
print(name[2])
print(name[2:5])
print (len(name))
print ("My name is %s and weight of %s is %d kg!" % ('Zara',"sujo", 21))

print (name.replace("world","this"))

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print (str.split( ))
print(str.split(' ', 2 ))

print("te" in name)
str2 = "  Python split strings article  "
str2=str2.strip()
splitStr=str2.split()
revstr=[]
print("Length: " , len(splitStr))
for inx in range(1, len(splitStr)+1 ):
    #if(inx>=1):
     i=inx * -1
     print(i)
     revstr.append(splitStr[i])

print(revstr)




