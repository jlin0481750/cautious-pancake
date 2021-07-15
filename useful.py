#THIS IS SPAGHETTI CODE. THE SOURCE BELOW MEANS NOTHING, I INCLUDED IT CAUSE I DID NOT WRITE THIS. I NEEDED CODE TO POPULATE THINGS. 
# ALL COMMENTS ARE MINE. PLEASE DON'T LOOK IN TO THIS THAT DEEP LOL

import math
 
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibonacci(n):
 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
    
for i in range(1,11):
     if (isFibonacci(i) == True):
         print i,"is a Fibonacci Number"
     else:
         print i,"is a not Fibonacci Number "
