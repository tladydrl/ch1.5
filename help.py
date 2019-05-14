#help(print)

def plus(a, b):
    """  # 함수 변수 안에다가 독이란 변수를 만든것이다...  함수 내부에다가 주석처럼,,, 주석으로 써도 되고,, 함수 안에서만 보면 되니깐..
        return the sum of parameter a, b  # 함수 설명..   # 함수 실행하는데 주석은 아무문제가 없다. # 주석 겸 help(f) 할때 설명으로 쓴다..
        :param a: 1st parameter  # 파라미터 설명.
        :param b: 2nd parameter
        :return : sum
    """
    return a + b

#plus.__doc__ = """
#    return the sum of parameter a, b  # 함수 설명..
#    :param a: 1st parameter  # 파라미터 설명.
#    :param b: 2nd parameter
#    :return : sum
#"""

help(plus) # plus라는  함수이름..


