eee = "hello " + "world"
# eee = eee +1 
# print(type(1))
# print(type(3.14))
# print(type("hello"))
# print(type(eee))
# print(type([1,2,3,4]))
# print(type({'a':1}))

#  covert interger to float 
# print(float(3))

# convert is float automatically in python 3
print(3/4)

sval ="123"
# will not convert to integer automatically 
# print(sval +1 )
print(type(sval))

# covert string to integer 
ival = int(sval)
print(ival)
print(type(ival))

nsv = "hello bob"
# won't work if this is not a number 
# int(nsv)

# True has a numeric value of 1
print(int(True))

# collect input through prompt 
#  is always a string 
name = input("who are you?")
print(name, type(name))