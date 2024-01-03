#Get the od string
'''def ChkStringOdd(st):
    if (len(st)%2)==1:
        return True
    else:
        return False

valstr= ["Two", "Line", "there","to" ,"insert","five7"]
for txt in valstr:
    if ChkStringOdd(txt):
        print(txt)

'''
# Get sorted string from string

def Sorting(lst ,n):
	lst.sort(key=len)
	return lst[n]

valstr= ["Two", "Line", "there",2 ,"insert","is"]
ls=[]
for vl in valstr:
    if type(vl)==str:
        ls.append(vl)

print(Sorting(ls,2))






