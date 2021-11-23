# In a product array puzzle problem we need to construct an array where the ith element will be the product of all the elements in the given array except element at the ith position.
array = [ 10, 5, 3, 6, 2 ]
product = 1
for index in range ( 0 , len ( array ) ) : product *= array [ index ]
ans = [ product ] * len ( array )
for index in range ( 0 , len ( ans ) ) : 
    temp = ans [ index ] / array [ index ]
    ans [ index ] = int ( temp )
print ( ans )