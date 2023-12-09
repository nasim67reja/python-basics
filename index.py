# myNum=23
# print(myNum)
# myName="Nasim Reja"
# print(myName)
# myList=[26,"Nasim Reja",{"name":"nasim"}]
# print(myList[2]["name"])

# 👉👉👉👉 Password 

# password=input("Enter your password ")

# if(password=="nasim"):
#     print("correct password")
# else:
#     print("Incorrect Password! try again")
      

# 👉👉👉👉 Reverse list

orginalList=[1,2,3,4,5,6]

lenOfList=0

for num in orginalList:
    lenOfList=lenOfList+1


def reverseList(list,len):
    s=0
    e=len-1
    while(s<e):
        temp=list[s]
        list[s]=list[e]
        list[e]=temp
        s+=1
        e-=1
        
    return list

print( "original list",orginalList)
reverse=reverseList(orginalList,lenOfList)
print("after reversing",orginalList)



