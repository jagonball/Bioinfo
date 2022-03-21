from random import randint

def get_input(): # 接受玩家猜測並檢查是否為有效值
    global guess_num
    try:
        guess_num = int(input()) # 將玩家的猜測轉成數值資料，存在guess_num
        if 0 < guess_num < 101:
            pass
        else:
            print("無效答案，請輸入1~100之間的任一整數:")
            get_input()
    except ValueError: # 若無法轉換，玩家輸入的非數值
        print("無效答案，請輸入1~100之間的任一整數:")
        get_input()

print("[猜數字遊戲]六次機會，請輸入1~100之間的任一整數:")
get_input()
secret_num = randint(1,100) # 隨機挑選1~100間的一個數字當答案
guess_count = 1 # 猜測次數
chances = 5 # 猜測機會-1

### 當 (玩家猜測 不等於 答案)與(猜測次數 小於等於 猜測機會) 兩者皆符合時，進入這個迴圈
while guess_num != secret_num and guess_count <= chances:
    guess_count += 1
    if guess_num > secret_num: # 若 玩家猜測 大於 答案 時
        print("猜得太大了！請再猜一次:")
        get_input()
    elif guess_num < secret_num: # 或當 玩家猜測 小於 答案 時
        print("猜得太小了！請再猜一次:")
        get_input()
### 沒進入上面迴圈時 (也就是 (當 玩家猜測 等於 答案)或(猜測次數 大於 猜測機會) 時)
##這裡要判斷是哪個原因造成沒有進入上面迴圈
if guess_num == secret_num: # 猜中答案了
    print("恭喜猜中了！正確答案是" + str(secret_num))
else: # 其他 (超過猜測次數)
    print("很抱歉！正確答案是" + str(secret_num) + "，請重新挑戰")