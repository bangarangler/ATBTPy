# spam = ["cat", "bat", "rat", "elephant"]
# bacon = [["cat",'bat'], ['rat','elephant']]
# eggs = [10,20,30]

# eggs[1] = 'Hello'
# del eggs[1]
# print(eggs)
# print(spam[1:3])
# # print(bacon[0][0])

# list methods
spam = ['hello','hi','howdy','heyas']
#find index of parameter. raise exception if not in list. if duplicates returns
# the first
print(spam.index('hello'))

bacon = ['cat','dog','bat']
bacon.insert(1, 'chicken')

bacon.append('moose')

bacon.remove('chicken')
eggs = [2,5,3.14,1,-7]
eggs.sort()
eggs.sort(reverse=True)
ham = ['a', 'z', 'A', 'Z']
ham.sort(key=str.lower)
print(ham)
print(eggs)
print(bacon)

import copy

spam = [1,2,3,4,5,6,7,8,9]
cheese = copy.deepcopy(spam)
print(cheese)
