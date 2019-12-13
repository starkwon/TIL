import requests
from decouple import config

# 기본 설정
token = config('TELEGRAM_BOT_TOKEN')
app_url = f'https://api.telegram.org/bot{token}'

# 응답 내용 저장하기
update_url = f'{app_url}getUpdates'
response = requests.get(update_url)
response= response.json()

#chat_id 찾아서 꺼내기
#chat_id = response.get("result")[0].get("message").get("chat").get("ID")
chat_id = config("CHAT_ID")

# 메시지 보내기 ?chat_id=882388579&text=반가워
# 메세지 보내기
message_url = f"{app_url}/sendMessage?chat_id={chat_id}&text=반가워"
print(requests.get(message_url))