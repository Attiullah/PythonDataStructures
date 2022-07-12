name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
l = dict()
for line in handle:
    if line.startswith("From "):
        line = line.rstrip(' ')
        line = line.split()
        b = line[5]
        c = b.split(':')
        d = c[0]
        l[d] = l.get(d, 0) +1
      
lst = list()
for key, val in l.items():
    newtup = (key, val)
    lst.append(newtup)
lst = sorted(lst, reverse=False)
for key, val in lst:
    print(key, val)


