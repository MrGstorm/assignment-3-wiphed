while True:
    grade = int(input("enter your grade\n>"))
    if grade >= 80:
        print(f"your mark '{grade}'is equal to a level 4")
    elif grade >= 70:
        print(f"your mark '{grade}'is equal to a level 3")
    elif grade >= 60:
        print(f"your mark '{grade}'is equal to a level 2")
    elif grade >= 50:
        print(f"your mark '{grade}'is equal to a level 1")
    else:
        print("you failed")

    again=input("have another test? (y/n)")
    if again == 'n':
        quit()
    if again == 'y':
        continue