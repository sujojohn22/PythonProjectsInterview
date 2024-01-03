str ="Management"
lenstr=len(str)

#str1=str.substring[0: (lenstr/2)]
#str2 =str.

for i in range(1 , lenstr+1):

    if(i<=lenstr):
        ind= (-1)* i
        print(str[ind],end="")

import re
strSpell ="mississippi"
num=len(re.findall("s",strSpell))
print("\n number of s",num)



#re regural expression

# \w is equivalent to [a-zA-Z0-9_].
p = re.compile('\w')
print(p.findall("He said * @ in some_lang."))
# '*' replaces the no. of occurrence of a character.
p = re.compile('ab*')
print(p.findall("ababbaabbb"))

m = re.search('\\bopen\\b', "please open the door")
print( m)

Nameage = '''
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21
'''

ages = re.findall(r'\d{1,3}', Nameage)
names = re.findall(r'[A-Z][a-z]*', Nameage)
ageDict = {}
x = 0
print("ages",ages)
print("names",names)
for eachname in names :
    ageDict[eachname] = ages[x]
    x+=1
print("DataDic",ageDict)

Str = "we need to inform him with the latest information"
# strating and ending index
for i in re.finditer("inform.", Str):
    locTuple = i.span()
    print(locTuple)

#Matching patern
Str = "Sat, hat, mat,rat, pat,cat"
# any starting char[rshmp]
allStr = re.findall("[rshmp]at", Str)
print("rshmp")
for i in allStr:
    print(i)

#string with starting char between h-m
someStr = re.findall("[h-m]at", Str)
print("\nIn h-m")
for i in someStr:
        print(i)

#string with  char NOT between h-m
someStr = re.findall("[^h-m]at", Str)
print("\n NOT in h-m")
for i in someStr:
            print(i)

#replace an item of the string with something else
Food = "hat rat mat pat"

regex = re.compile("[r]at")

Food = regex.sub("food", Food)

print(Food)


#Working with white space removal
randstr = '''
You Never
Walk Alone
Liverpool FC
'''

print("string with whiteapace" , randstr)

regex = re.compile("\n")

randstr = regex.sub(" ", randstr)

print("string without whitespace", randstr)

#Validate phone number
#\w validate [a-z][A-Z][0-9_]

phone= "425-773-4558"
if re.search('\d{3}-\d{3}-\d{4}',phone):
    print("Yes! phone number")
else:
    print("not phone number")


    #Find valid email
email = "ac@aol.com md@.com @seo.com dc@.com"

print("Email Matches: ", re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email))






