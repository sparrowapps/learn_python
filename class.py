#class

#class classname[(parent_class_name)]:
#   <class variable 1>
#   <class variable 2>

#   def classfunc1(self[, arg1, arg2,,,]):
#       <statement 1>
#       <statement 2>

#   def classfunc2(self[, arg1, arg2,,,]):
#       <statement 1>
#       <statement 2>


# __init__ (constructor)

# multiplication class

class multiplication:
    def __init__(self, num):
        self.num = num
    def run(self):
        for j in range (1,10):
            print(" %d * %d = %d" %(self.num,j, self.num*j))

mul2 = multiplication(2)
mul3 = multiplication(3)
mul4 = multiplication(4)
mul5 = multiplication(5)
mul6 = multiplication(6)
mul7 = multiplication(7)
mul8 = multiplication(8)
mul9 = multiplication(9)

mul2.run()
mul3.run()
mul4.run()
mul5.run()
mul6.run()
mul7.run()
mul8.run()
mul9.run()


