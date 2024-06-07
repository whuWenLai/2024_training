words={
    "apple":"苹果",
    "balanan":"香蕉",
    "pine":"荔枝",
    "west":"西瓜",
    "rice":"大米饭"
}
for key,value in words.items():
    print(key,value)

words["hello"]="world"
words["hi"]="你好"

for key,value in words.items():
    print(key,value)
