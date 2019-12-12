12.12 Morning Assignment

## 1. 웹 스크래핑

### (1) python에서의 웹 스크래핑 방법

- request 패키지 설치

  ```
  pip install requests
  ```

  > 기본적인 requests 기능을 먼저 살펴보면, requests는 HTTP GET, POST, PUT, DELETE 등을 사용할 수 있으며, 편리한 데이타 인코딩 기능을 제공하고 있다. 즉, 데이타를 Dictionary로 만들어 GET, POST 등에서 사용하면 필요한 Request 인코딩을 자동으로 처리해 준다.

  ```
  import requests
  from bs4 import BeautifulSoup
  ```

  > requests는 정말 좋은 라이브러리이지만, html을 '의미있는', 즉 Python이 이해하는 객체 구조로 만들어주지는 못한다. BeautifulSoup은 html 코드를 Python이 이해하는 객체 구조로 변환하는 Parsing을 맡고 있고, 이 라이브러리를 이용해 우리는  '의미있는' 정보를 추출해 낼 수 있다

  ```
  response = requests.get('https://www.naver.com')
  print(response.text)
  ```

  > requests.get(url) 함수를 사용하면 해당 웹페이지 호출 결과를 가진 Response 객체를 리턴한다. Response 객체는 여러 attribute들을 가지고 있는데, 예를 들어, Response의 status_code 속성을 체크하여 HTTP Status 결과를 체크할 수 있고, Response 에서 리턴된 데이타를 문자열로 리턴하는 text 속성이 있다.





