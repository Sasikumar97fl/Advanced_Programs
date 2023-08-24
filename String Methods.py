''' String Methods '''

''' There are 47 Regular Methods and Special or Magic methods are 33 '''

""" 
Strings are one of the most commonly used data types in any programming language. It represents textual data and 
sequences of characters. In python, strings are immutable and ordered. This is very impportant while implementing a functions to operate a string. 
Fortunately, Python has rich in-bulid functions that manipulate strings.
"""

""" Capitalize """
# def capitalize(self)->str
# def capitalize(self,*args, **kwargs): #real signature unknown
# Return a capitalized version of the string.
# More specifically, make the first character have upper case and the rest all lower.

# Case

s = 'youth 123 python'
print(s.capitalize())

# Note : The first character only convert to uppercase in the given string.

s = 'YOUth 123 python'
print(s.capitalize())

# Note : The first character convert to upper case and then remaining characters are converted to lower case

""" Title """
# def title(self)->str
# def title(self,*args, **kwargs): #real signature unknown
# Return a version of the string where each word is titlecased.
# More specifically words start with uppercased characters and all remaining cased characters have lower case.

# Case

s = "i am learning PYTHON FOR EVERY DAY"
print(s.title())

s = "#1i_2am_learning_PYTHON_FOR_EVERY_DAY"
print(s.title())
dnosbab