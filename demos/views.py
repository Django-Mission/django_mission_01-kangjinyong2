from django.shortcuts import render
from django.http import HttpRequest,HttpResponse # 가져오기
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.
def calculator(reqeust): #reqeust는 요청 , 무조건 첫번째 인자로 들어와야 함
    #return HttpResponse('계산기 기능 구현 시작입니다.') # 응답
    print(f'reqeust = {reqeust}') # request의 정보 출력
    print(f'reqeust type = {type(reqeust)}') # request가 어떤 타입인지 정보출력
    
    #1. 데이터 확인
    num1 = reqeust.GET.get('num1') # 값1 요청받음
    num2 = reqeust.GET.get('num2') # 값2
    operators = reqeust.GET.get('operators') # 연산자
    print(num1)
    #2. 계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1)*int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0
        
    #3. 응답
    return render(reqeust,'calculator.html',{'result' : result}) # 두번째 인자에 calculator.html 파일명
    #html을 응답할 때는 render라는 함수를 쓴다.
    
def lotto(reqeust): # 로또 추출하기
        import random
        lotto_nums = random.sample(range(1,45),6) # 로또번호 섞기        
        return render(reqeust,'lotto.html',{'lotto_nums' : lotto_nums})
    
def lotto_CH(reqeust): 
        return render(reqeust, 'lotto_CH.html')


def lottoresult(reqeust): 
        import random
        #number = reqeust.GET.get('number',2)
        num = reqeust.POST.get('num',3)
        result2 = []
        r=0
        for i in range(int(num)):
            lotto = random.sample(range(1, 45), 6)
            lotto.sort()
            result2.append(lotto)
            r +=1
        return render(reqeust, 'lottoresult.html', { 'r':r , 'result2': result2})