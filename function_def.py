# 함수 정의

#  C: function(){} ... 끝이 있다.
def dummy():    # 아무것도 안하는 함수,,, 더미.
    pass  # 더미 하나 만들땐 패스 써준다.. 함수 정의..

def my_function():
    print('Hello World')

def times(a, b):
    result = a * b
    return result

def none():
    return

dummy()
my_function()
result = times(10, 20)
print(result)  # 아니면 프린트문 안에다가 함수를 넣어도 된다.
print(none(), type(none())) # 논을 리턴한다.

# 함수도 객체다.

# 파이썬은 거의 모든게 객체로 되어있다.

print(dummy, type(dummy))  # 펑션 클래스의 주소이다..

f = my_function   # 마이펑션 함수가 정의가 되어있다.  # 함수함수함수, 객체객체객체  # 함수 객체..  실행해버리면 실행값이 나온다.
f()

def my_function2(func):
    func()  # 함수 넣어줘서 실행한다.

my_function2(f) # 헬로월드 찍는다.

print(f, my_function(), sep='.')  # 함수도 객체이다. 같은곳 가르키고 있다... 주소값이 같다.



































