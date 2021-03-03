name=input("enter your name")
age=int(input("enter your age"))

print("hello my name is",name,"and i am",age, "year old")

print("hello my name is",+ name+ "and i am"+ str(age)+ "year old")
print("hello my name is %s and i am %d year old" % (name, age))
print("hello my name is {} and i am {} year old ", format(name, age))
print(f"your name:{name}.your age:{age}")
