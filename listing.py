# for the listing it will be like this
vowels = ['a', 'e', 'i', 'o', 'u']
# if I want to get one of them I will
print(vowels[0])
# The list or the index of the list start with "0" or u can use (-)

#Other method we can use is (slicing) its the to get more than one indivigual at the same time
vowles = ['a', 'e', 'i', 'o', 'u']
print(vowels[0 : 4])
#if you put number out of the range it will display (index error)

#some Built-in Functions
#The len() function returns the total length of a list.
#The max() function returns the maximum value in a list.
#The min() function returns the minimum value in a list.
stock1_prices = [2.52, 2.44, 2.32, 2.41, 2.51, 2.50, 2.44]
stock2_prices = [8.36, 8.31, 8.21, 8.21, 8.25, 8.11, 8.13]

print(len(stock1_prices))      # Output: 7
print(max(stock1_prices))      # Output: 2.52
print(min(stock2_prices))      # Output: 8.11

#Reading list
#.append() method adds an item to the end of the list.
#.insert() method adds an item to a specific index.
#.remove() method removes an item from a list based on the value.
#.pop() method removes the item at a particular index.
reading_list = ['Harry Potter',
'1984',
'The Fault in Our Stars',
'The Mom Test',
'Life in Code']
reading_list.insert(0, 'Pachinko')
reading_list.remove('1984')
print(reading_list)