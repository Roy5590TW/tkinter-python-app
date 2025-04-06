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
