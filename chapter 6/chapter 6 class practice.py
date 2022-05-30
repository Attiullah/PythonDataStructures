stem = "Hey there what's up"
for i in stem:
    print(i)
print(stem[0:23])
g = stem.lower()
print(g)
f = stem.startswith('hey')
print(f)
x = stem.find("t")
print(x)
s = stem.find(" ", x)
y = stem[x+1: s]
print(y)