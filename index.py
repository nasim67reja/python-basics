# 👉👉👉👉 Python Keywords
import keyword
# print(keyword.kwlist)

# print( True==2)


# myNum=23
# print(myNum)
# myName="Nasim Reja"
# print(myName)
# myList=[26,"Nasim Reja",{"name":"nasim"}]
# print(myList[2]["name"])


# # 👉👉👉👉 any /all

list1=[]
list2=[]

# Index ranges from 1 to 10 to multiply
for i in range(1,11):
    list1.append(4*i) 
 
# Index to access the list2 is from 0 to 9
for i in range(0,10):
    list2.append(list1[i]%5==0)
print(list1," ",list2)
print('See whether at least one number is divisible by 5 in list 1=>')
print(any(list2))

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

# print( "original list",orginalList)
# reverse=reverseList(orginalList,lenOfList)
# print("after reversing",orginalList)



# 👉👉👉👉 Implement Binary search using python

# orginalList=[1,2,3,4,5,6]
arr=[1,2,3,4,5,6,12,25,29,54]

def search(num):
    s=0
    e=len(arr)-1
    mid= round((s+e)/2)

    while(s<=e):
        if(arr[mid]==num):
            return mid
        elif (num>arr[mid]):
            s=mid+1
        else:
            e=mid-1
        mid= round((s+e)/2)
    return -1


# num=int(input("print your number : "))

# output=search(num)
# if(output==-1):
#     print(num,"is not present in the list")
# else:
#     print(num,"is present at",output)