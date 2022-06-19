#lists
from numpy import average


dred = ['wer','wer','qwe','er','trt','e']
print(dred[4])

#lists are mutable/changeable
dred[3] = 6
print(dred)
print(len(dred))
print(range(len(dred)))
for i in range(len(dred)):
    letter = dred[i]
    print("the letter is ", letter)    



#manipulating lists/// slicing
a= [3,34,33,554]
b = [1,2,3,45,5]
c = a+b
print(c)
print(c[1:3])

c.append('book')
print(c)
print(3232 in c)


numlist=list()
while True:
    inpu = input("enter a number: ")
    if inpu=='done':
        break
    value = float(inpu)
    numlist.append(value)
average=sum(numlist)/len(numlist)
print("Average: ", average)