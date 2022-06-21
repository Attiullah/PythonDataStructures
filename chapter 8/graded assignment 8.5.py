fname = input("Enter the name of the file: ")
fo = open(fname)
count = 0
for line in fo:
    line = line.rstrip()
    if line.startswith("From "):
        a = line.split()
        b = a[1]
        count = count+1
        print(b)
        if line.startswith("From:"):
            continue
print("There were", count, "lines in the file with From as the first word")
