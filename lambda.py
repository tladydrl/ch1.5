# lambda 함수

def f(x):   # 인풋이 x이네.
    return x * 2

print(f(2))  # f는 여러번 쓰겠다.

# 같은 식을 람다식으로,, 함수이름 없는걸 한다..
#print( (lambda x: return x * 2)(2)  )  # 함수로 만들면.,, 함수 주소를 넘겨줄수 있다는것인가.  # 한번만 쓰고 말거기 때문에 함수이름 정하지 않겟다.
# 위처럼 하면 파이썬 문법에 어긋남.
print( (lambda x: x * 2)(2)  )  # 이거는 f(2)랑 같은 구문이다.

# 한번 쓰고 말걸,, 람다를 쓴다.. 뒤에서 쓰지 않을때, 익명 함수이다.. 함수이름준다는건 계속 쓰겠다는 것이다.






























