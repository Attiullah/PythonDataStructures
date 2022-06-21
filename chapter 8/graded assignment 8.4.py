#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname= input("Enter the name of the file: ")
fo= open(fname)
a = list()
for line in fo:
    line = line.rstrip()
    b= line.split()
    for word in b:
        if word not in a:
            a.append(word)
            a.sort()
print(a)
