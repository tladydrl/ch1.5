# 기본 인수 값. # 파라미터에 값이 있는 것. 기본적으로 값이 가지는거
def incr(a, step=1): # 디폴트값으로 세팅.. 에러가 안난다.
    return a + step

print(incr(10, 1))
print(incr(10))

print(incr(10, step = 2))  # 보통거에다 마지막에가 디폴드값 넣는다.
print(incr(10,2))

print(incr(10))

# 오류
#def decr(step=1, a):
#    return a - step

# 키워드 인수
def area(width, height):
    return width*height

print(area(10, 20 ))
print(area(width=10, height=20))
print(area(height=20, width= 10))
print(area(height = 20, width = 10))
print(area(10, height= 20))
#오류
#print(area(10, width = 20) )
#print(area(height = 20, 10)) # 하잇 다음에 없다..


# 튜플형식으로 받겠다: * args,,
# 가변 인수
def vargs(a, *arg): # 딕셔너리일때는,,
    print (a, arg)

#에러 : vargs()
vargs(10)
vargs(10, 1) # 하나짜리 튜플은 , 붙는다
vargs(10, 1, 2, 3, 4, 5)

def vargs2(*arg):  # var 아그스 2
    print(arg)

vargs2()
vargs2(10)
vargs2(10, 20, 30)

# 모든 인수를 sum
def sum(*numbers):
    s = 0;
    for n in numbers:
        s += n
    return s

print(sum())
print(sum(1,2,3,4,5))

# 내장함수 print는 어떻게 만들어졌을까?
def _print(*arg, e='newline'):
    print(arg, e)
_print(10, 20, 30)
_print(10, 20, 30, e= 'tab')

# c의 printf함수 흉내내기 printf("%s이 %d 원짜리 %s입고 %s를 차고 노래를 한다", "타잔",  100, "팬티", "칼");
def printf(f, *arg):
    print(f % arg) # 튜플을 포맷을 넣는다. # 튜플 가변변수를 받는다..

printf("%s이 %d 원짜리 %s입고 %s를 차고 노래를 한다", "타잔",  100, "팬티", "칼");

# 딕셔너리로 받기..
# 정의되지 않은 키워드 인수 처리하기
def f(width, height, **kwd):
    print(width, height, kwd['depth'], kwd['dimension'])
    #print(kwd) # 딕셔너리로 들어오네./

f(10, 20, depth=30, dimension=3) # 윗스 하잇,, # 뎁스도 , 디맨젼도.
 # 키워드 값을 안주고 출력하려고 하면 에러가 난다.. 이름 = 값,, 넣어주기..

def g(a, b, *arg, **kwd):
    print(a, b)
    print(arg)
    print(kwd)

g(10, 20)
g(10, 20, 30)
g(10, 20, c=6)
g(10, 20, 30, 40, 50, c=7, d=7)

def h(name, age, height):  # * 는 개별적인 값으로 보라. **는 개별적인값으로 두번 보라?
    print(name, age, height)
# 딕셔너리는 키가 아규먼트의 값에 일치해야한다.
# 튜플도 개수가 맞지 않으면 에러난다.

h('둘리', 10, 140)

t = ('둘리', 10, 140)
h(*t) #갯수 맞지 않으면 에러ㅏ.

d = {'name' : '둘리','age' : 10, 'height' :140 }
h(**d)  #갯수 맞지 안으면에러

