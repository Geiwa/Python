def values(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
    
result = values([3, 3, 3, 7])
print(result)  

result = values([7, 7, 3])
print(result)  
