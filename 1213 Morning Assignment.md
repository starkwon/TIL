# 1213 Morning Assignment

## 1.가상환경 구축 및 실행

#### (1) 폴더생성

```
mkdir venv
python -m venv  [생성한 폴더 이름]
```

#### (2) 진입 방법 

```
source venv/Scripst/activate
```

#### (3) 탈출 방법 

``` 
deactivate
```

#### (4) 진입 방법 단축키 생성

``` 
vi ~/.bashrc
alias activate "source venv/Scripst/activate"
/.bashrc
```

#### (5) Esc 두번 눌러서 :rq 후 저장

​	venv가 있는 곳에서만 activate 해야 함!

## 2. github 업로드 시에 무시하는 방법

## 	(deactivate 하는 법을 잊어버렸을 때)

gitignore.io 사이트에 접속, 내가 무시하려는 개발환경을 입력, 소스 복사

vi.gitignore에 들어간 후 shift+insert 하여 복사 



## 3. Flask

### (1) Flask란?

Flask는 Python으로 구동되는 웹 어플리케이션 프레임워크다. 우선 가상환경을 만들고 Flask를 설치

```
# Flask 설치
$ pip install flask

# Flask 확인
$ flask --version
```

### (2) Flask 사용법

​	`flask` 폴더 생성 후 `app.py` 생성

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/info')
def info():
    return 'Info'
```

### (3) 템플릿 추가하기

`flask` 폴더 내에 `templates`폴더 추가, 이 곳에는 html 파일들을 넣어준다.

app.py에 템플릿 코드 추가

```
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
```

