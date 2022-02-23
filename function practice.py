def calculate_double(amount):
    double = amount * 2
    return double


def calculate_half(amount):
    half = amount / 2
    return half


def calculate_ten_more(amount):
    ten_more = amount + 10
    return ten_more


question = int(input("how much?: "))
answer_1 = calculate_half(question)
answer_2 = calculate_double(question)
answer_3 = calculate_ten_more(question)
print(f"half {question} is {answer_1}")
print(f"double {question} is {answer_2}")
print(f"ten more than {question} is {answer_3}")
