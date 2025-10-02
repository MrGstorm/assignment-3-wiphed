import time
try:
    while True:
        password = input("enter the right word to exit!")
        if password == 'exit':
            print("you got it!")
            time.sleep(0.3)
            quit()
        else:
            print("wrong. try again")
            continue
except ValueError:
    print("unsupported input")