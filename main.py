'''가장 간단한 구조의 파이썬 프로젝트.
필요한 연산이 main 파일에 그대로 들어있다.
간단한 알고리즘 문제를 풀때 주로 이렇게 코드 작성함.
'''

# 숏코딩에 절여져서 띄어쓰기가 다소 생략되어있다.
for i in range(1,int(input())+1):
    s=''
    if i%3==0:s+='fizz'
    if i%5==0:s+='buzz'
    print(s if s else i)