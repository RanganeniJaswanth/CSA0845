# author jaswanth 065 05\09\22
def max_of_two(x,y):
    if x > y:
         return x
         return y
    return z
def max_of_three( x, y, z):
    return max_of_two(x, max_of_two(y, z))
print(max_of_three(99,86,77))
