def findMissing(A1,A2):

    if len(A1)>0 and len(A2)>0 :
        A1.sort()
        A2.sort()

        missing=[]
        for i in range(0,len(A1)-1):
          if A1[i] not in A2:
            missing.append(A1[i])
    #elif len(A1)==len(A2):
        #print ("not missing")
    else:
        print ("empty array")

    return missing

a1=[8,7,3,4,4,5]
a2=[2,4,9,8,5]
print(findMissing(a1,a2))



