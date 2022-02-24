

def message():
    message=input("Enter your message: ")
    for i in range(10):
        print(message)

def timesTable():
    num=int(input("Enter a number: "))
    for i in range(1,11):
        print(i*num)

def main():
    choice = ""
    while choice !="3":
        print("1. Message Repeater")
        print("2. Time Table")
        print("3. Powers")
        print("4. Quit")
        print("Enter your choice:  ")
        choice=input()
        if choice=="1":
            message()
        elif choice=="2":
            timesTable()
    print("Goodbye")

main()
