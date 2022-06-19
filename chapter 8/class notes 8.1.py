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