" 함수 사용 설명서를 보고 싶을 때 help() 를 이용한다.
"ex) help(print) 

"사용자 함수도 출력 할수 있다.
"설명을 달고 싶으면 다음과 같이 한다.

>>> def plus(a,b):
...     return a + b
... 
>>> help(plus)

>>> plus.__doc__ = " 두 인자의 합을 리턴 한다."
>>> help(plus)

>>> 

__doc__ 속성을 입력 하면 help() 의 도움말이 표시 된다.

또는 함수의 첫번째 실행 줄에 """로 주석을 달아도 된다.

>>> def plus(a,b):
...     """ 플러스 함수의 주석임
...     이것도 도움말에 표시됨
...     두 인자의 합을 리턴
...     """
...     return a + b
... 
>>> help(plus)

>>> 
>>> help(plus)

Help on function plus in module __main__:

plus(a, b)
    플러스 함수의 주석임
    이것도 도움말에 표시됨
    두 인자의 합을 리턴
(END)
