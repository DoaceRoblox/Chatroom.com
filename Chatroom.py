name = input()

while True:
    text = input()

    if text != "":
        print(f"{name}: {text}")

    elif text == "\end_chatroom":
        break