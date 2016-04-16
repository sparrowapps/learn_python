# python control statement



# if <condition statement>:
#   <statement>
# else:
#   <statement>

# if indenet
# condition statement after :

# c, c++ else if --> elif

#while <condition statement>:
#    <statement>
#    <statement>
#    <statement>
#    <statement>

# break, continue


# for variable in LIST(or TUPLE, STRING):
#   <statement>
#   <statement>

# range function

# sum of ( 1 to 100 ) 5050
sum = 0
for i in range (0, 101):
    sum = sum + i

print (sum)


# the rules of multiplication
for i in range ( 2, 10):
    for j in range (1, 10):
        print(" %d * %d = %d" %(i,j,i*j))


>>> l =  [ 100, 1, "apple"]
>>> for i in enumerate(l):
...     print(i)
... 
(0, 100)
(1, 1)
(2, 'apple')


>>> def get20over(i):
...     return i > 20
... 
>>> L = [10, 20, 30, 40]
>>> Iter = filter(get20over, L)
>>> for i in Iter:
...     print(i)
... 
30
40
>>> 


# if statement logical operation C &&, || --> and, or
