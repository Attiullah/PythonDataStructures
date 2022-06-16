fname = input("Enter the name of the file: ")
try:
    fo = open(fname)
except:
    print("No such file")
    quit()
for line in fo:
    line = line.rstrip()
    line = line.upper()
    print(line)