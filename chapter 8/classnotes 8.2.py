#manipulating lists/// slicing
a= [3,34,33,554]
b = [1,2,3,45,5]
c = a+b
print(c)
print(c[1:3])

c.append('book')
print(c)
print(3232 in c)

print(sum(a))

numlist=list()
while True:
    inpu = input("enter a number: ")
    if inpu=='done':
        break
    value = float(inpu)
    numlist.append(value)
average=sum(numlist)/len(numlist)
print("Average: ", average)