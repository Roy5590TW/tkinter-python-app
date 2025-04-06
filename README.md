#問答申論
```
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
```
![](https://static.coderbridge.com/img/iwjudkdi/d6489e0f4c1e4433828edab2b5971bb0.png)
#程式實作
```
# 引入 Tkinter 模組
import tkinter as tk


# 定義一個函式為 convert_temperature，用於攝氏轉華氏溫度的計算和顯示結果
def convert_temperature():
  # 取得輸入的攝氏溫度，並轉換成浮點數型態
  celsius = float(celsius_entry.get())

  # 使用攝氏轉華氏的公式進行溫度轉換
  fahrenheit = (celsius * 9 / 5) + 32

  # 顯示轉換後的華氏溫度結果
  result_label.config(text="華氏溫度: {:.2f}".format(fahrenheit))

  # 在轉換後自動清除輸入內容，將攝氏溫度的輸入框清空
  celsius_entry.delete(0, tk.END)


# 建立主視窗，建立 Tk 物件
window = tk.Tk()

# 設定視窗標題
window.title("攝氏轉華氏溫度轉換器")

# 建立攝氏溫度標籤元件，用於顯示文字 "攝氏溫度:"
celsius_label = tk.Label(window, text="攝氏溫度:")
celsius_label.pack()

# 建立攝氏溫度輸入框元件
celsius_entry = tk.Entry(window)
celsius_entry.pack()

# 建立轉換按鈕元件，當按下時執行 convert_temperature 函式
convert_button = tk.Button(window, text="轉換", command=convert_temperature)
convert_button.pack()

# 建立結果標籤元件，用於顯示轉換後的華氏溫度結果
result_label = tk.Label(window, text="")
result_label.pack()

# 啟動主視窗的事件迴圈
window.mainloop()

```
[Replit](https://replit.com/@Roy5590TW/Di-17-Qi-Python-Cheng-Shi-She-Ji-Ru-Men-Gong-Xue-Ying#main.py)
