###-----------------index-----------------###

# define index : returns the index of the first occurrence of a specified value in a list

# courses =['Math','Physics','Chemistry','Biology']

# this prints the list with index
# for index, course in enumerate(courses):
#     print(index, course)


# this prints the list with index starting from 1
# for index, course in enumerate(courses, start=1):
#     print(index, course)


###-----------------join-----------------###

# define join : returns a string in which the elements of sequence have been joined by str separator


# courses =['Math','Physics','Chemistry','Biology']
# courses_str = ', '.join(courses)
# print(courses_str)

###-----------------split-----------------###

# define split : splits a string into a list where each word is a list item

# new_courses = courses_str.split(', ')
# print(new_courses)

###-----------------Tuple-----------------###

# define tuple : a collection which is ordered and unchangeable

# mutable : can be changed
# immutable : cannot be changed

# example for mutable

# list_1 = ['physics','chemistry','biology']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'math'  
# print(list_1)
# print(list_2)

# example for immutable

# tuple_1 = ('physics','chemistry','biology')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# # tuple_1[0] = 'math'  # TypeError: 'tuple' object does not support item assignment

# print(tuple_1)
# print(tuple_2)



###-----------------Set-----------------###

# define set : a collection which is unordered and unindexed

# example for set

# cs_courses = {'Math','Physics','Chemistry','Biology'}

# print(cs_courses)
# print('Math' in cs_courses)

# #intersection
# cs_courses = {'Math','Physics','Chemistry','Biology'}
# art_courses = {'History','English','Math','Physics'}

# print(cs_courses.intersection(art_courses))

# #difference
# print(cs_courses.difference(art_courses))

# #union
# print(cs_courses.union(art_courses))


###-----------------create Empty List, Empty Tuple and Empty Set-----------------###

# define empty list
empty_list = []
print(empty_list)

# define empty tuple
empty_tuple = ()
print(empty_tuple)

# define empty set
empty_set = set() 
# empty_set = set() # This is't right! it will create an empty dictionary
print(empty_set)  # set()
