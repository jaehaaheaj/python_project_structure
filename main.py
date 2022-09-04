'''main 내부에 함수가 구현되어 있어서 해당 함수를 호출하여 연산을 진행.
다소 복잡한 알고리즘 문제를 풀때, 혹은 구현하고자 하는 기능이 몇 가지로
나뉘는 작은 프로젝트 코드를 짤때 이런 식으로 구조를 잡으면 편하다.
'''

# 복잡한 문제는 아니지만, fizzbuzz의 배수 체크 부분을 함수로 떼어냈다.
def fizzbuzzz_checker(i):
    if i%(3*5)==0: return 'fizzbuzz'
    elif i%3==0: return 'fizz'
    elif i%5==0: return 'buzz'
    else: return i

# 배수 체크가 끝나고 나온 결과물을 출력한다.
for i in range(1,101): print(fizzbuzzz_checker(i))
