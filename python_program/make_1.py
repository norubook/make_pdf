import tkinter as tk
from tkinter import messagebox
# 参考サイト https://murasan-itlab.com/python-tkinter-inputform/

def on_register():
    # 各エントリーフィールドから値を取得
    title = entry_title.get()
    gender = gender_var.get()
    
    # 全てのフィールドが入力されているか確認
    if not (title and gender):
        messagebox.showwarning("警告", "すべてのフィールドを入力してください。")
        return
    
    # 登録成功のメッセージボックスを表示
    messagebox.showinfo("情報", "情報が登録されました。")
    
    # テキストエリアに入力情報を表示
    info = f"""
タイトル: {title}
性別: {gender}
"""
    text_area.insert(tk.END, info)

app = tk.Tk()
app.title("入力フォーム")

# 各ラベルとエントリーフィールドを作成し、gridで配置
label_title = tk.Label(app, text="タイトル", anchor=tk.CENTER)
label_title.grid(row=0, column=0)

entry_title = tk.Entry(app)
entry_title.grid(row=0, column=1)


label_gender = tk.Label(app, text="性別", anchor=tk.CENTER)
label_gender.grid(row=5, column=0)

# 性別のラジオボタンを作成
gender_var = tk.StringVar()
gender_var.set(None)
radio_male = tk.Radiobutton(app, text="男性", variable=gender_var, value="男性")
radio_male.grid(row=5, column=1, sticky=tk.W)
radio_female = tk.Radiobutton(app, text="女性", variable=gender_var, value="女性")
radio_female.grid(row=6, column=1, sticky=tk.W)

# 登録ボタンを作成し、クリックイベントをバインド
button_register = tk.Button(app, text="登録", command=on_register)
button_register.grid(row=7, column=0, columnspan=2)

# テキストエリアを作成
text_area = tk.Text(app, height=10, width=40)
text_area.grid(row=8, column=0, columnspan=2)

app.mainloop()