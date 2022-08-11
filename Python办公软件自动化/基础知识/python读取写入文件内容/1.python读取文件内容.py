# 书写人：胡高远
# 书写时间：2022/7/13  15:46
f = open('note.txt', 'r', encoding='utf-8')
text = f.readlines()
print(text)
f.close()

with open('note.txt', 'r', encoding='utf-8') as f:
    print(f.readlines())