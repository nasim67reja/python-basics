#  List Comprehensions

l=[1,2,3,4,5,6,7,8]

# doubleL=[]

# for index in range(len(l)):
#     doubleL.append(l[index]*2)


# list comprehension

doubleL=[item for item in l if item%2==0]

print(doubleL)