import random

max_try = 0

while True:
    print(f"현재까지 최대 시도 횟수는 {max_try}입니다.")
    answer_number = random.randint(1, 100)
    print(answer_number)
    count = 0

    while True:
        my_guess = int(input("1~100사이의 숫자를 입력해주세요!"))

        if my_guess > 100 or my_guess < 1:
            print("1과 100사이라고!!")
            continue

        count = count + 1
        print(f"{count}번째 시도입니다!")
        if answer_number == my_guess:
            print("정답입니다!")
            print(f"{count}번째 만에 정답을 맞췄습니다!")
            if count > max_try:
                max_try = count
            break
        elif answer_number < my_guess:
            print("더 작은수가 답입니다! down!")
        else:
            print("더 큰수가 답입니다! UP!!!")

    will_continue = input("계속하고 싶으시면 yes를 입력해주세요")

    if will_continue == "yes":
        continue
    else:
        break
