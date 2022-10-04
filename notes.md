#CSE2120 Data and Data Structures 1 - Notes

Date structures are organizational, management, and formatting tools for the storing large data sets in single variables. Data structures may include different types such as Tuples, Lists, Arrays, and Dictionaries. Variations of some of these types include Queues and Stacks (IB ONLY)

## Types of Data Structures in Python
### Tuple
A _Tuple_ is a static data structure, where data is immutable (cannot be changed). All data are declared when the variable is created
```python
# A Tuple 
A_TUPLE = (1, 3, 5.0, 7, "eleven", 13)
A_TUPLE = (1, 3, 5.0, 7, "eleven", 17)

print(A_TUPLE) # output (1, 3, 5.0, 7, "eleven", 17)
print (A_TUPLE[1]) # output "3"
# items in a data structure begin at - so the first item = 0, second item = 1, third item = 2, etc...
print(A_TUPLE[4]) # output 5th item: "eleven"
```


When using a data structure, each individual item within the structure is assigned an __index number__. This index number identifies the specific location that the data is stores (index numbers start at 0)

### Lists
A __List__ is a one-dimensional away that is a dynamic data structure where individual data points are mutable (they can be updated).
```python
A_LIST = [1, 3, 5.0, 7, "eleven", 13]
#you can updated / change single pieces of data in a list
A_LIST[5] = 17
#this changes the 6th data point from 13 to 17

print(A_LIST) # output [1, 3, 5.0, 7, "eleven" 17]
print(A_LIST[1]) # outputs 3
```

NOTE: Despite tuples always using parenthesis and lists always using square brackets, when declaring an index value the index number is _always in square brackets_.

### Static vs Dynamic Arrays
In most cases either a static or dynamic array can be used to store data. However, there are instances where one is preferable over another. For data that should not be changed independently, static arrays are preferable. For data where values can be changed independently of one another, dynamic arrays are preferable.
Static arrays are preferred for things like...
* Storing screen resolution
* Storing a position on a 2D or 3 plane
* Storing identification information of an individual
* Storing last semester's grades

Oftentimes, tuples are used to store information that's difficult to change. For example, your nae links to your student ID. One should never be changed in a program without also changing the other.

### Data Structure Indexing and Calling

Frequently, calling on a single value within the data structure is needed instead of calling the entire structure. Therefore, there needs to be a process of identifying a single value. Each value has a positional index number associated with it.
```python
indexNumber = [0, 1, 2, 3, ...]
```

To reference a specific value, include the list name followed immediately with the index number in square brackets.


```python
A_LIST = ["This", "is", "a", "sentence"]
print (A_LIST[3]) # outputs "sentence".
```

Array indexing has forward (head-to-tail) indexing and backwards (tail-to-head) indexing. Either index number will call teh data value, and each data has a forward and backwards index number.

```python
A_LIST = ["This", "is", "a", "sentence"]
# index      0      1    2        3
# index     -4    -3   -2       -1
print (A_LIST[-3]) # outputs "is".
print (A_LIST[1]) # outputs "is".
```

To reference a subset of values, include a start index value and an end index value separated by a colon. NOTE: the subset starts at the starting index value, but only goes up to (not including) the end index value

```python
A_LIST = ["This", "is", "a", "sentence"] 
SUBLIST = A_LIST[1:3] #SUBLIST equals ["is", "a"]
# SUBLIST will equal items 1 and 2 from A_LIST, but will not include item 3
```
 
There are two shortcuts to creating sublists from the beginning and the end of the list. When starting a sublist from the beginning of the list, omit the first number; to have a sublist go to the end, omit the last number,

```python
SUBLIST2 = A_LIST[:3] # SUBLISTS equals ["This", "is" "a"] DOES NOT INCLUDE ITEM 3
SUBLIST3 = A_LIST [1:] # SUBLIST3 equals ["is", "a", "list."] DOES NOT INCLUDE ITEM 1
```

NOTE: When starting a sublist from the beginning of the list, the sublist __WIL NOT__ include your stopping point. When ending a sublist at the end of a list, the sublist __WILL__ include your starting point.

#### Lists Length'
All lists also have a length property, where the total number of data values is callable using the ````len(LIST)```` function.

```python
A_LIST [ "This", "is", "a", "sentence."]
print(len(A_LIST)) # output 4              

for i range(len(A_LIST)):
print(A_LIST[i])

'''
equals
print(A_LIST[0])
print(A_LIST[1])
print(A_LIST[2])
print(A_LIST[3])
'''
```  

## Manipulating Data in Lists
Data in a dynamic list can undergo many processes. They are often summarized with the acronym CRUD

(C)reate (R)ead (U)pdate (D)elete

###Creating Data in Arrays
#### Append data to the end of a list

To add data to the tail (the end) of a list, use the ```append(DATA)```dot function (.isnumberic() is a dot function) 

```python
A_LIST = []

A_LIST.append("Hello")
print(A_LIST) # output ["Hello"]

A_LIST.append("World")
print(A_LIST) # output ["Hello", "World"]
```

#### Insert data to a specific index value within the list
To add data to a specific index position, use the ```insert(DATA)``` dot function. This function should be used sparingly because it may result in mis-addressing data. When a value is inserted into a list, it shifts subsequent index values forward by one.

```python
A_LIST = ["this", "is", "a", "sentence"]
A_LIST.insert(2, "not")
print(A_LIST) # output ["this", "is", "not", "a", "sentence. "]
```

### Reading Data in Arrays
All examples of this have been covered in the introduction above

```python
print(A_LIST[1]) # output "is"
```

### Updating Data Arrays
NOTE: tuples cannot update a single value, only the entire tuple. However, to update a single value in a list, the list node can be assigned a new value.

```python
A_LIST = ["this", "is", "a", "sentence. "]
A_LIST[0] = "THIS"
print(A_LIST) # output ["THIS", "is", "a", "sentence"]\
```

### Deleting Values in Data Arrays
Deleting data from an array will change the overall length of an array and may re-assign new index values to pre-existing values within the array.

#### Pop data off an array
To remove a value off an array, the ```pop(INDEX)``` dot function removes the value at the index number. When using .pop() the data is removed off the list, but not destroyed. If desired, the removed data can be stored in  new variable.

NOTE: If no index value is given, .pop() will remove the highest index value data (in other words, the last item in the list)

```python
A_LIST = ["this", "is", "a", "sentence. "]
A_LIST.pop()
print(A_LIST) # output ["This, "is", "a"]

A_LIST.pop(1)
print(A_LIST) # output ["this", "a"]

VARIABLE = A_LIST.pop(0)
print(A_LIST) # output ["a"]
print(VARIABLE) # output ["This"]
```

.pop() is used to remove an item with a known index value.

#### Remove data from an array
To remove a value off an array, the ```remove(VALUE)``` dot function will remove the first instance of the value while traversing the array from head to tail (from beginning to end).

```python
NEW_LIST = [0, 1, 2, 5, 7, 11, 13, 11, 17]
NEW_LIST.remove(11)  #removes the first value that's 11
print (NEW_LIST) # output [0, 1, 2, 5, 7, 13, 11, 17]
```