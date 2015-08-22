#-*-coding: utf-8 -*-
#exception

#try:
#   <statement>
#except ZeroDivisionError as e: //예외 0으로 나누기
#   <statement> // 예외 발생시 수행
#else:
#   <statment>
#finally:
#   <statement> // 예외 수행과 상관 없이 수행


#pass 예외 무시 하기
#raise 에러 발생시키기

import sys
args = sys.argv[1:]

for i in args:
    try:
        f = open(i, 'r')
    except IOError as e:  #FileNotFoundError
        print(str(e))
    else:
        lines = f.readlines()
        
        for line in lines:
            print(line)
        f.close()