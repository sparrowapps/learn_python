#file

#cat
#filename = raw_input ("file name :")

#f = open(filename,'r')
#lines = f.readlines()

#for line in lines:
#    print(line)

#f.close()

# cat version up

import sys
args = sys.argv[1:]

for i in args:
    f = open(i, 'r')
    lines = f.readlines()

    for line in lines:
        print(line)
    f.close()
