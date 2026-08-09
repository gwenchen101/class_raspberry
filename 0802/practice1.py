import random

def get_computer_choice():
    """隨機產生電腦的選擇"""
    choices = ["剪刀", "石頭", "布"]
    return random.choice(choices)

def get_winner(player, computer):
    """判斷勝負"""
    if player == computer:
        return "平手"
    win_conditions = {
        "剪刀": "布",
        "石頭": "剪刀",
        "布": "石頭",
    }
    if win_conditions[player] == computer:
        return "玩家獲勝"
    return "電腦獲勝"

def play_game():
    """猜拳遊戲主流程"""
    options = {"1": "剪刀", "2": "石頭", "3": "布"}
    player_score = 0
    computer_score = 0
    round_num = 1

    print("===== 猜拳遊戲開始 =====")
    print("輸入 q 可以隨時離開遊戲\n")

    while True:
        print(f"--- 第 {round_num} 局 ---")
        print("請選擇：1) 剪刀  2) 石頭  3) 布")
        user_input = input("你的選擇：").strip()

        if user_input.lower() == "q":
            print("\n遊戲結束！")
            break

        if user_input not in options:
            print("輸入無效，請輸入 1、2、3 或 q\n")
            continue

        player_choice = options[user_input]
        computer_choice = get_computer_choice()

        print(f"你出了：{player_choice}")
        print(f"電腦出了：{computer_choice}")

        result = get_winner(player_choice, computer_choice)
        print(f"結果：{result}")

        if result == "玩家獲勝":
            player_score += 1
        elif result == "電腦獲勝":
            computer_score += 1

        print(f"目前比分 → 玩家 {player_score} : 電腦 {computer_score}\n")
        round_num += 1

    print(f"最終比分 → 玩家 {player_score} : 電腦 {computer_score}")
    if player_score > computer_score:
        print("恭喜你，最終贏得比賽！")
    elif player_score < computer_score:
        print("電腦獲勝，再接再厲！")
    else:
        print("旗鼓相當，平手收場！")

if __name__ == "__main__":
    play_game()
