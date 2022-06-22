a= dict()
b = input("Enter the text here: ")
fb = open(b)
for line in fb:
    line = line.split()
print(line)
for x in line:
    a[x] = a.get(x, 0)+1
print(a)

#for specific entered text 
a= dict()
line = input("Enter the text here: ")
word = line.split()
for every in word:
    a[every] = a.get(every, 0) +1
print(a)
#looping through the keys in the dictionary
for word in a:
    print(word, a[word])

#getting list of keys and values from a dictionary
print(list(a))
print(a.keys())
print(a.values)
print(a.items()) #key value pairs

##more than one iteration variablea
c = {'a': 1, 'b': 2, 'c':3, 'd':4}
for a,b in c.items():
    print(a,b)





