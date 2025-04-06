import random
import tkinter as tk

# 隨機產生答案
answer = random.randint(1, 100)

#定義初始最小值
min_value = 1

#定義初始最大值
max_value = 100

# 檢查猜測數字的函式
def check_guess():
    global min_value, max_value
    guess = int(guess_entry.get())

    # 判斷猜測數字與答案的關係
    if guess < min_value or guess > max_value:
        result_label.config(text="輸入的數字超出範圍！請重新輸入。\n正確範圍: {} ~ {} 之間".format(min_value, max_value))
    elif guess < answer:
        result_label.config(text="答案比較大喔！\n答案在 {} ~ {} 之間".format(guess + 1, max_value))
        min_value = guess + 1
    elif guess > answer:
        result_label.config(text="答案比較小喔！\n答案在 {} ~ {} 之間".format(min_value, guess - 1))
        max_value = guess - 1
    else:
        result_label.config(text="恭喜，你答對了！")

    # 清除猜測數字的輸入框
    guess_entry.delete(0, tk.END)

# 建立主視窗，建立 Tk 物件
window = tk.Tk()

# 設定視窗標題
window.title("猜數字遊戲")

# 設定視窗大小
window.geometry("300x200")

# 建立標籤元件，用於顯示文字 "請輸入一個數字:"
guess_label = tk.Label(window, text="請輸入一個數字:")
guess_label.pack()

# 建立輸入框元件
guess_entry = tk.Entry(window)
guess_entry.pack()

# 建立提交按鈕元件，當按下時執行 check_guess 函式
submit_button = tk.Button(window, text="提交", command=check_guess)
submit_button.pack()

# 建立結果標籤元件，用於顯示猜測結果
result_label = tk.Label(window, text="")
result_label.pack()

# 設定視窗背景顏色為藍色
window.configure(background='blue')

# 啟動主視窗的事件迴圈
window.mainloop()

print("遊戲結束")
