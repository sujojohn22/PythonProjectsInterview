def chkAnagram(s1,s2):
    disCnt={}
    s1=s1.replace(' ','').lower()
    s2 = s2.replace(' ', '').lower()
    if len(s1)!= len(s2):
        print("len notmatch")
        return False
    else:
        for ch in s1:
             if ch in disCnt:
                 disCnt[ch] += 1
             else:
                  disCnt[ch]=1
        print("First dic",disCnt)
        for ch in s2:
            if ch in disCnt:
                disCnt[ch] -=1
            else:
                disCnt[ch]= 1
        print("Sec dic", disCnt)
        for cnt in disCnt:
          if disCnt[cnt]!=0:
              return False

    return True


s1= input("Enter String1:")
s2= input("\nEnter String2:")

print (chkAnagram(s1.lower().strip(),s2.lower().strip()))

