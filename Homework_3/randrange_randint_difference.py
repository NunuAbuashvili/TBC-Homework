"""
What is the difference between random.randrange( ) function and random.randint( ) function?

	1. Parameters
	
	random.randrange( ) function takes in three parameters:
	start - an integer specifying at which position to start (optional) | default = 0
	stop - an integer specifying end position (required) (exclusive)
	step - an integer specifying the incrementation (optional) | default = 1
	
	While random.randint( )  function takes in only two parameters:
	start - an integer specifying at which position to start (required)
	stop - an integer specifying end position (required) (inclusive)
	
	So, start parameter is required while using the random.randint( ) function, while it is optional for the random.randrange( ) function. 
	Only random.randrange( ) function allows a step parameter to be passed. 
	
	2. Behaviour 
	
    random.randint( ) function generates a random integer between a specified range (inclusive of both endpoints), while random.randrange( ) function generates a random integer within a specified range starting at "start", less than "stop" (exclusive of the endpoint), and incremented in between by "step" (optional). 
"""
import random

print(random.randrange(0, 10)) # Random integer between 0 and 9
print(random.randint(0, 10)) # Random integer between 0 and 10
print(random.randrange(10)) # Random integer between 0 and 9
print(random.randrange(0, 10, 2)) # Random integer from [0, 2, 4, 6, 8]

# Sources:
# https://www.codecademy.com/forum_questions/521bcf2b548c359b28000367
# https://www.prepbytes.com/blog/python/randint-function-in-python/
# https://pynative.com/python-random-randrange/