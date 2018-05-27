import random
print(random.randint(5, 20)) # line 1
print(random.randrange(3, 10, 2)) # line 2
print(random.uniform(2.5, 5.5)) # line 3

"""
- What did you see on line 1?
  What was the smallest number you could have seen, what was the largest?
  -> A random number between 5 until 20. The smallest number is 5 an dthe largest is 20.
  
- What did you see on line 2?
  What was the smallest number you could have seen, what was the largest?
  Could line 2 have produced a 4?
  -> A random number between 3 until 9 with the range of 2. The smallest number is 3 and the largest is 9.
     No, line 2 cannot print 4, because line 2 has the range of 2 (3, 5, 7, 9)
     
- What did you see on line 3?
  What was the smallest number you could have seen, what was the largest? 
  -> A random number between 2.5 until 5.5. The smallest number is 2.5 and the largest number is 5.5.
"""


