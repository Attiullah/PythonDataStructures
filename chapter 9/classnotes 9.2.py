#coounting with dictionaries
ccc= dict()
ccc['zhen']  = 1
ccc['chuck'] = 1
'zhen' in ccc

counts = dict()
x = ['a', 'b', 'c', 'a', 'e', 'e']
for letter in x:
    if letter in counts:
        counts[letter] = counts[letter] + 1
    else:
        counts[letter] = 1
print(counts)

#another way of doing the same thing 
for letter in x:
    counts[letter] = counts.get(letter, 0) +1
print(counts)