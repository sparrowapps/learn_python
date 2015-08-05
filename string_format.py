# string_format.py

number = 10
day = "three"
print("sparrow %d old, %s days" % (number, day))

# arrange
print("{0:<10}".format("sp"))
print("{0:>10}".format("sp"))
print("{0:^10}".format("sp"))

# fill
print("{0:=^10}".format("sp"))


# string functions
a = 'SPARROW'
print(a.lower())

a = 'sparrow'
print(a.upper())

a = '  sparrow           '
print(a.lstrip())

a = ' sparrow            '
print(a.rstrip())

a = '        sparrow        '
print(a.strip())

a = 'sparrow is programmer'
print (a.replace("sparrow", "junho"))

a = 'sparrow is programmer'
print(a.split())

a = 'a|b|c'
print(a.split('|'))