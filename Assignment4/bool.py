def compare(a, b):
    '''
    compare function makes a comparison between arguments a and b, and returns an integer value
    '''
    if a>b:
        return 1
    elif a==b:
        return 0
    else:
        return -1

# static function calls for test
print(compare(5,2))
print(compare(2,5))
print(compare(3,3))

# switch to user input to test compare function
user_input_A = int(input("Enter first value: "))
user_input_B = int(input("Enter second value: "))

print(compare(user_input_A, user_input_B))