###-----------------casting-----------------###
# define casting : converting one data type to another data type

# num_1='100' # string
# num_2='200' # string

# num1=int(num_1) # integer
# num2=int(num_2) # integer

# print(num1+num2) # 300

# print(int(num_1)+int(num_2)) # 300


###-----------------list-----------------###

# define list : a collection of items

# courses =['Math','Physics','Chemistry','Biology']
# print(courses)      # prints the list
# print(courses[1:3]) # prints the list from index 1 to 3
# print(len(courses))   # prints the length of the list
# print(courses[0])   # prints the first element
# print(courses[1])   # prints the second element
# print(courses[2])   # prints the third element
# print(courses[3])   # prints the fourth element
# print(courses[-1])  # prints the last element
# print(courses[-2])  # prints the second last element
# print(courses[-3])  # prints the third last element
# print(courses[-4])  # prints the fourth last element


###-----------------append/Extend/pop-----------------###

# define append : adds to the end of the list
# define extend : adds all elements from an iterable (such as a list, tuple, or string) to the end of an existing list, modifying it in-place and increasing its length
# define insert : adds to the specified index
# define remove : removes the specified element
# define pop : removes the element at the specified index

# courses.append('Computer Science') # adds to the end of the list
# courses.extend(['Computer Science']) # adds all elements from an iterable (such as a list, tuple, or string) to the end of an existing list, modifying it in-place and increasing its length
# courses.insert(1,'Computer Science') # adds to the specified index
# courses.remove('Math') # removes the specified element
# courses.pop() # removes the last element
# courses.pop(1) # removes the element at the specified index

# print(courses)


# ------->>> Sortings
###-----------------sort/reverse-----------------###

# define sort : sorts the list in ascending order
# define reverse : reverses the list

# courses.sort() # sorts the list in ascending order
# courses.reverse() # reverses the list
# courses.sort(reverse=True) # sorts the list in descending order

# sorted_courses = sorted(courses) # sorts the list in ascending order


# print(sorted_courses)
# print(courses)

###-----------------min/max/sum/len-----------------###

# define min : returns the smallest item in an iterable or the smallest of two or more arguments
# define max : returns the largest item in an iterable or the largest of two or more arguments
# define sum : returns the sum of all items in an iterable
# define len : returns the number of items in an iterable

# numbers=[1,2,3,4,5,6,7,8,9,10]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# print(len(numbers))


###-----------------index-----------------###

# define index : returns the index of the first occurrence of a specified value in a list

# courses =['Math','Physics','Chemistry','Biology']
# print(courses.index('Biology'))

# print('Math' in courses)  # returns True if the element is present in the list else False



###-----------------loop-----------------###

# define loop : iterates over a sequence (such as a list, tuple, or string)

courses =['Math','Physics','Chemistry','Biology']

# for item in courses:
#     print(item)

# for index, item in enumerate(courses): # returns the index and the item example: 0 Math
#     print(index,item) # 0 Math
    
for index,item in enumerate(courses,start=1): # returns the index and the item example: 1 Math
    print(index,item) # 1 Math
















