# 복잡한 문제는 아니지만, fizzbuzz의 배수 체크 부분을 함수로 떼어냈다.
def fizzbuzzz_checker(i):
    if i%(3*5)==0: return 'fizzbuzz'
    elif i%3==0: return 'fizz'
    elif i%5==0: return 'buzz'
    else: return i