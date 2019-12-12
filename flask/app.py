from flask import Flask
from flask import render_template
from flask import request
import random
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/mulcam')
def mulcam():
    return 'this is mulcam!'

@app.route('/greeting/<string:name>')
def greeting(name):
    return f"Hello, {name}!"

@app.route('/cube/<int:num>')
def cube(num):
    result = num**3
    return str(result)

@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['김밥','우동','떡볶이','치킨']
    order = random.sample(menu, people)
    return str(order)

@app.route('/html') 
def html():
    return '<h1>안녕하세요!!</h1>'

@app.route('/html_file')
def html_file():
    return render_template('html_file.html')   

@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html', your_name=name)    

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('pong.html', name=name, message=message)    

@app.route('/god/<string:name>')
def god(name):
    menu = ['매력','체력','키','인성','재력','창의력','생명력','꿀잼','핵잼']
    order = random.sample(menu,3)
    return f"신이 {name} 님을 만들 때,{str(order)} 을 주었습니다!"

@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

@app.route('/vonvon_result')
def vonvon_result():
    name = request.args.get("name")
    features = ['똑똑함','유머','코딩','의리','멍청함']
    chosen = random.sample(features, 3)
    chosen = ' '.join(map(str, chosen))
    return render_template('vonvon_result.html', name=name, chosen=chosen)

@app.route('/ascii')
def ascii():
    return render_template('ascii.html')

@app.route('/ascii_result')
def ascii_result():
    #1. form 태그로 날린 데이터(word)를 받는다.
    word = request.args.get("word")
    #2. word를 가지고 ascii_art API 요청 주소로 요청을 보낸다.
    exp = requests.get(f'http://artii.herokuapp.com/make?text={word}')
    #3. API 응답 결과를 html 파일에 담아서 보여준다.
    return render_template('ascii_result.html',expp=exp.text)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    response = requests.get(f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}')
    lotto = response.json()
    #키 값 가져오는 두가지 방법

    winner = []
    # 1. for 문을 활용한다.
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])
    
    numbers = request.args.get('numbers') #string
    numbers = numbers.split() # list
    numbers_int = [] 

    for number in numbers:
        numbers_int.append(int(number)) #for문을 돌면서 하나씩 정수형으로 변경하여 리스트 안에 넣기

    matched = len(set(winner) & set(numbers_int))
    if matched ==6:
        result = '1등입니다!!!'
    elif matched == 5:
        if lotto['bnusNo'] in numbers_int: #보너스 번호 확인
            result = '2등입니다!!'
        else:
            result = '3등입니다!!'
    elif matched == 4:
        result = '4등입니다!!'
    elif matched == 3:
        result = '5등입니다!!'
    else:
        result = '꽝입니다!!'
        
    # 2. List Comprehension
    # winner = [lotto[f'drwtNo{i}'] for i in range(1,7)]
    return render_template('lotto_result.html',
        lotto_round=lotto_round, winner=winner, numbers=numbers_int, result=result
    )

if __name__ == '__main__':
    app.run(debug=True)