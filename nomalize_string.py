# 문자열 데이터를 분석하기 전에 처리함수 만들기
# 1. 공백제거
# 2. 필요없는 문장 부호 제거
# 3. 대소문자 정리하기. # 캐피탈라이즈,, 맨 앞문자 대문자.. 타이틀함수,, title Hello World..
import re  # 레귤러 익스프레션

#위의 3개를 하나의 함수로 만들어 볼 것이다.

states = ['Alabana', ' Ge#!?orgial', 'south caro']

def clean_strings(strings):
    results = []
    for s in strings:  # 리스트 하나씩 돌아간다.
        s = s.strip()  # s 가 바뀐다.. 왼쪽 오른쪽 공백 없앤다.
        # 정규 표현식을 쓸 것이다. 스트링을 표현..
        s = re.sub('[!#?]', '', s) # s에서 !#?를 ''로 바꾸고, s로 넣겠다)
        s = s.title() # 타이틀만든다.

        results.append(s) # 바뀐  s 값을 결과리스트에 추가한다.
    return results
result = clean_strings(states)
print(result)

def clean_strings2(strings, *funcs): # 펑크스는 하나씩 보겠다? 튜플?
    results = []
    for s in strings:  # 리스트 하나씩 돌아간다.
        for func in funcs:
            s = func(s)  # 함수에 넣는다.  # 함수작업들 하면서 s를 업데이트 하고,, 함수작업 다 하고 s를 리절트 리스트에 추가한다.
        results.append(s)
         # 바뀐  s 값을 결과리스트에 추가한다.
    return results

def strip(s):
    return s.strip()

def remove_specialchar(s):
    return re.sub('[!#?]', '', s)

print((lambda s: re.sub('[!#?]', '', s))("abc#4!!!!def"))  # 호출하기 위해서 괄호친거이다.
##clean_strings2(states, (strip)) #strip 함수 주소를 넘겨준다. # 전역으로 할려면,, str 클래스의 strip 객체 주면된다/??
clean_strings2(states,str.strip, str.title )  #람다,,

# 프린트가 리턴,,   # 프린트는 논이나와도 된다ㅏ?
print(print('abc'))
(lambda s: print(s))("abc")

result = (lambda  a, b: a*b)(10, 20)   # s:  다른언어는 s->  # 본문내용은 1줄만 가능..
#( a, b ) -> {
#    return a * b:
#}
# 한줄로 표현하기 위해서 람다를 쓴다..
result = clean_strings2(states, str.strip, str.title, lambda s: re.sub('[!#?]', '', s))  # 함수를 객체처럼 다룬다.

# 함수형 프로그래밍,, 람다.

#다음 헬프,,


print('-----------')
states = ['Alabama', ' Georgia!#?!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']

def clean_strings(strings):
    results = []
    for s in strings:
        s = s.strip() #함수작업들..
        s = re.sub('[!#?]', '', s)
        s = s.title()
        results.append(s)

    return results


result = clean_strings(states)
print(result)


def clean_strings2(strings, *funcs):
    results = []
    for s in strings:
        for func in funcs:
            s = func(s)

        results.append(s)

    return results


# def remove_specialchar(s):
#    return re.sub('[!#?]', '', s)
#print((lambda s: re.sub('[!#?]', '', s))("abc#4!!!!!def"))
# print((lambda s: re.sub('[!#?]', '', s) )("abc"))
# result = (lambda a, b: a*b)(10, 20)
# a, b -> a * b

result = clean_strings2(states, str.strip, str.title, lambda s: re.sub('[!#?]', '', s))
print(result)

print('---------')

def strlen(s):
    return len(s)

strings = ['foo']

strings.sort(key=strlen) # 길이순으로 정려하겠다.

strings.sort(key=lambda  s: len(s))  # lens(s) 하는 함수를 키로ㅗ 준다.. 주소인가보다..

# 헬프 ,, 함수사용할때 도움을 받을 수 있다..




