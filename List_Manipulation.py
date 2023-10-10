'''

   Program Description: In this program we made use of list methods in manipulating the list, like remove(), insert() and append() methods respectively.. 

'''   

stack_of_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
'''The stack keyword is known as list keyword in python language'''

print('The old list = {}'.format(stack_of_numbers))

print('\t')
''' "\t": It is an escape key which is use for spacing(Tab key) in the python program'''

stack_remove = stack_of_numbers.remove(10)
'''Using remove(element) method, we removed the element (10) in the list'''


stack_addition_at_any_position = stack_of_numbers.insert(4, 8)
'''Using the insert(index,element) method'''
'''The new element (8) is added at index/position (4) in the list'''

stack_addition_at_the_end_position = stack_of_numbers.append(17)
'''Using the append keyword to add 17 at the end of the list'''

print('The new list = {}'.format(stack_of_numbers))
'''Using the print() method to display the new list with the new element'''