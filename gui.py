def get_file(message: str) -> str:
    # return input(message)
    return ""


def menu(options: list):
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
    selection = int(input("> "))
    return selection
