import tkinter as tk
from tkinter import messagebox
import os
import tkinter as tk
from tkinter import filedialog
# 参考サイト https://murasan-itlab.com/python-tkinter-inputform/


def on_register():
    # 各エントリーフィールドから値を取得
    title = entry_title.get()
    user_name = entry_user_name.get()
    
    # 全てのフィールドが入力されているか確認
    if not (title and user_name):
        messagebox.showwarning("警告", "すべてのフィールドを入力してください。")
        return
     

    text_file_path = selected_file.get()
    fr = open(text_file_path,'r', encoding='UTF-8')
    fr_text= fr.read()
    fr.close()
    # テキストエリアに入力情報を表示
    info = f"""
タイトル: {title}
名前: {user_name}
text: {fr_text}
"""
    text_area.insert(tk.END, info)

def select_file():
    file = filedialog.askopenfilename(filetypes=[("","*")])
    out_path = os.path.abspath(os.path.join(file, os.pardir))+'/'

    if file:
        selected_file.set(file)
    

app = tk.Tk()
app.title("入力フォーム")

selected_file = tk.StringVar()

# 各ラベルとエントリーフィールドを作成し、gridで配置
text_title = tk.Label(app, text="必要情報を入力してください", anchor=tk.CENTER)
text_title.grid(row=0, column=0)

label_title = tk.Label(app, text="タイトル", anchor=tk.CENTER)
label_title.grid(row=1, column=0)

entry_title = tk.Entry(app)
entry_title.grid(row=1, column=1)

label_user_name = tk.Label(app, text="名前", anchor=tk.CENTER)
label_user_name.grid(row=2, column=0)

entry_user_name = tk.Entry(app)
entry_user_name.grid(row=2, column=1)


#ファイル選択ボタン
file_select = tk.Button(app, text="ファイルを選択", command=select_file)
file_select.grid(row=6, column=0, columnspan=2)

file_label = tk.Label(app, textvariable=selected_file)
file_label.grid(row=7, column=0, columnspan=2)

# 登録ボタンを作成し、クリックイベントをバインド
button_register = tk.Button(app, text="登録", command=on_register)
button_register.grid(row=8, column=0, columnspan=2)

# テキストエリアを作成
text_area = tk.Text(app, height=10, width=40)
text_area.grid(row=9, column=0, columnspan=2)

app.mainloop()