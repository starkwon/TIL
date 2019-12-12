#1. 불러오기
with open('mulcam.txt','r') as tex:
    lines = tex.readlines()

#2. 뒤집기
lines.reverse()

#3. 작성하기
with open('mulcam.txt','w') as tex:
    for line in lines:
        tex.write(line)
