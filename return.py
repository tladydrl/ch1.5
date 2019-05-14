# 인수없이 반환하기.

def nothing():
    return

n = nothing()  # n에다가 함수 넣어줌다.
print(n)  # nothing()의 반환값이 나온다.

# return문이 없어도 됨
def print_menu(): # 중간에 리턴있으면 함수 그다음실행안된다.
    print('1. Python')
    print('2. Java')
   # return
    print('3. C')
    print('4. C++')
    print('5. C#')

print_menu()
# 다른언어: 반환값이 하나인데,, 파이썬에서는 반환값이 여러개를 가질 수 있다.

# 1개의 값을 반환할 때.
def max_value(a, b):
    if a > b:
        return a
    else:
        return b

print(max_value(10, 20))  # 큰 값이 반환되게 하는 함수이다.

# 여러개의 값을 반환할 때
def func():
    return 10, 'hello', {1,2,3}, (1,2,3)  # 4개 반환... #사실.. 패킹이 일어나서 튜플을 반환하는것이다. 튜플객체를 반환하게 된다.
    # 패킹해서 리턴 안해도 알아서 패킹해서 반환한다.
t = func()
print(t, type(t))  # 오토 패킹..

# 언패킹 해보기.
n, s ,e, t = func()  # 리턴할땐 패킹 받을땐 언패킹..으로 받을 수 있다.  #
print(n, s, e, t)

# 객체를 만들어서 레퍼런스를 넘겨줌.. 레퍼런싱..
# call by value 가 아닌,,, call function by reference

























