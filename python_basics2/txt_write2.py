with open('mulcam.txt','r') as text:
    lines = text.readlines()
    for line in reversed(lines):
        print(line.strip())