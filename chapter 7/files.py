fhand = open("text.txt", 'r')
b = fhand.read()
a = 0
for i in fhand:
  a = a+1
  print('number of lines: ', a)
# reading the whole file
print(b[:])
#length
print(len(b))

#skipping a line
for line in fhand:
  line= line.rstrip()
  if line.startswith("I'm"):
    continue
  print(line)
#another way of skipping lines we are not intersted in: this will skip all those lines that do not start with with "I'm" 
for line in fhand:
  line= line.rstrip()
  if not line.startswith("I'm"):
    continue
  print(line)
 # reading specific lines
for line in fhand:
    line= line.rstrip()
    if line.startswith("I'm"):
      print(line)
#searching for line with specific words
for line in fhand:
  line= line.rstrip()
  if not 'deeper'in line:
    continue
  print(line)

#getting a file name from user and checking for words
myFile = input("enter the name of the file: ")
try:
  ofile= open(myFile)
except:
  print("the file", myFile, "does not exist. TRY AGAIN!")
  quit()
count = 0
for line in ofile:
  if line.startswith("you"):
    count = count+1
print("there are", count, "number of lines in", myFile)            

