fname = input("Enter the file: ")
fo = open(fname)
fine= dict()
for line in fo:
    if line.startswith('From '):
        line = line.split()
        b = line[1]
        fine[b] = fine.get(b, 0)+1
        
bigco=None
bigword= None
for word,count in fine.items():
    if bigword is None or count >bigco:
        bigword = word
        bigco= count
print(bigword, bigco) 
