from tkinter import Y


(x, y) = (4, 'fred')
print(y)

d  = (1, 2,3) > (3, 2, 4)
print(d)
c = {'d':10, "c":6, 'a':3, 'b':20}
print(c.items())
print(sorted(c.items()))

#going through a dictionary in key order
for i, j in sorted(c.items()):
    print(i, j)



#going through a dictionary in value order
c = {'d':10, "c":6, 'a':3, 'b':20}
gh  = list()
for i, j in c.items():
    gh.append((j, i))
print(gh)

fg = sorted(gh, reverse=False)
print(fg)