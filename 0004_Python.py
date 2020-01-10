# Project Euler: 4
# Find the largest palindrome made from the product of two 3-digit numbers.

def euler_4(n): # n = n-digit numbers
  for i in range(10**n - 1,1,-1):
    for j in range(10**n - 1,1,-1):
      if check_palindrome(i*j):
        return i,j,i*j


def check_palindrome(n):
  return str(n)==str(n)[::-1]
    

##############################################

if __name__ == "__main__":
  a,b,c = euler_4(3)
  print("Biggest Palindrome {} x {} = {}".format(a,b,c))
    
##############################################

"""
Biggest Palindrome 999 x 91 = 90909
"""

