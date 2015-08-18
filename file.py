#file

filename = raw_input ("file name :")

f = open(filename,'r')
lines = f.readlines()

for line in lines:
    print(line)

f.close()