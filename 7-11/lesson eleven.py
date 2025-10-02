import time
print("im writing a story, can you give me your name and age?")
name = input('whats your name\n>')
age = int(input('how old are you\n>'))
def greetings():
    print(f'{name} walked down to the pier when he was {age - 4}')
time.sleep(0.3)
greetings()