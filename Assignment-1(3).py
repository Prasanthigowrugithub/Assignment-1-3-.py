lst = [1,2,3,4,5,6,7,8,9]
odd = 0
even = 0
for i in lst:
    if i%2==0:
        odd = odd+1
    else:    
        even = even+1
    
print("total odd numbers are ",odd)
print("total even numbers are",even)