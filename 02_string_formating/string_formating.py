# String formating

name="nasim"
name="Reja"
ask="how are you ?"

greeting=f"hello {name} {ask}"

print(greeting)

# Another way

greeting="Hello {} {}".format("nasim","How are You.?") # Hello nasim How are You.?

# Providing Values by Position
greeting ="Hello {1} {0}".format("How are you.?","Nasim")

ask="How are you.?"
name="Nasim"

greeting="Hello {1} {0}".format(ask,name)

# greeting="Hello {name} {ask}".format(ask,name) #KeyError: 'name'
greeting="Hello {name} {ask}".format(ask="How are you.?",name="Nasim") 

greeting_skeleton="Hello {1}. {0}"

# print(greeting_skeleton.format("How are you.?","Nasim"))

add="2+2={}"
# print(add.format(2+2))

# print(greeting)
