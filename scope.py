# scope test


def func(a):
    x = 2
    return a * x  # 이건 워닝이 난다.. x값이 없기때문에?

print(func(10))  # 결과는 2이 나온다.. LGB 규칙 중에 로컬에서 찾는 경우,

# L(G)B 중에 글로벌 변수 x 사용함.
x = 2
def func2(a):
    return a * x
print(func2(10))

def func3(a):
    global y  #글로벌로 쓸 수 있다.. 함수 내부엣 ㅓ적어줌.
    y = 2
    return a * y

print(func3(10))
print(y)

# 내장 영역(built-in score)
print(dir('__builtines__')) # 함수들 정의해놓은거이다.
