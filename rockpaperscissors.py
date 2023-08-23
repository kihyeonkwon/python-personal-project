import random

options = ["가위", "바위", "보"]

count_win = 0
count_draw = 0
count_lose = 0


while True:
    random_number = random.randint(0, 2)
    computer_select = options[random_number]

    user_select = input("가위 바위 보 중에서 골라주세요. 종료를 원하면 끝 이라고 입력해주세요")

    if user_select == "끝":
        break
    if user_select not in options:
        print("가위 바위 보 중에서 똑바로 좀 고르세요")
        continue

    if computer_select == user_select:
        print("비겼습니다!")
        count_draw = count_draw + 1
    else:
        if user_select == "가위":
            if computer_select == "보":
                print("플레이어가 이겼습니다.")
                count_win = count_win + 1
            else:
                print("플레이어가 졌습니다.")
                count_lose = count_lose + 1
        elif user_select == "바위":
            if computer_select == "가위":
                print("플레이어가 이겼습니다.")
                count_win = count_win + 1
            else:
                print("플레이어가 졌습니다.")
                count_lose = count_lose + 1
        else:
            if computer_select == "바위":
                print("플레이어가 이겼습니다.")
                count_win = count_win + 1
            else:
                print("플레이어가 졌습니다.")
                count_lose = count_lose + 1


print(f"승리 : {count_win}  무승부 : {count_draw} 패배: {count_lose}")
