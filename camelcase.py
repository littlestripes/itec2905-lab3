def to_camel_case(input_string: str) -> str:
    words = input_string.split(" ")

    new_str = []
    new_str.append(words.pop(0).lower())
    for word in words:
        new_str.append(word.capitalize())

    return "".join(new_str)


def check_validity(input_string: str):
    if (
        input_string[0].isdigit() or
        not input_string.isalnum()
    ):
        print("Warning! Invalid variable name")


if __name__ == "__main__":
    pre_case = str(input("Enter your sentence: "))

    post_case = to_camel_case(pre_case)
    print("In camel case: {}".format(post_case))

    check_validity(post_case)
