#function



#def functionname( input_argument):
#   <statement 1>
#   <statement 2>

#ex

def sum( a, b)
    return a + b

print (sum(1,2))


def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

result =  sum_many(1,2,3,4,5,6,7,8,9,10)
print (result)


# return tuple
def sum_and_mul(a,b):
    return a+b, a*b

a = sum_and_mul(3,4)
#a = (7, 12)

#default value
