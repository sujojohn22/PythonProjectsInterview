#Given a string write a function that will convert the string to all uppercase letters
'''def stringupper(s):
    return s.upper()

value=input("Enter string :\n")
print(stringupper(value))
'''

def AmountAcct(FindacctN):
   Account= {'Acct1':
        {
        'name': 'Test1',
        'AccNm': 'A12',
        'Amt': 3000
         },
           'Acct2':{'name': 'Test2',
                'AccNm': 'A132',
                'Amt':5000
                 },
       'Acct3': {'name': 'Test3',
                 'AccNm': 'A127',
                 'Amt': 7000
                 }
   }
   Amount=0
   for acct in Account:

       if Account[acct]['AccNm']==FindacctN or Account[acct]['name']== FindacctN:
           Amount= Account[acct]['Amt']
   if Amount==0:
         print("\n Invalide Acct")

   return Amount

acctNum =input("\nEnter Acctnum or name : ")
#AmountAcct(acctNum)
print('Amount in the acct %s is %d' %(acctNum,AmountAcct(acctNum)))
#print()