import tkinter as tk
from tkinter import messagebox
import os
import tkinter as tk
from tkinter import filedialog
# 参考サイト https://murasan-itlab.com/python-tkinter-inputform/


def make_html(file,title,text,user_name):
    out_path = os.path.abspath(os.path.join(file, os.pardir))+'/'


    a=0
    output='''
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>新聞スタイルのページ</title>
    <style>
        body {
            font-family: 'Georgia', serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }

        /* ヘッダー */
        header {
            text-align: center;
            padding: 10px;
            background-color: #333;
            color: white;
        }

        /* 2カラムレイアウト */
        .container {
            display: flex;
            flex-wrap: wrap;
        }

        /* 左のメイン記事 */
        .main-article {
            padding: 20px;
            background-color: white;
            margin: 10px;
        }

        /* フッター */
        footer {
            text-align: center;
            padding: 10px;
            background-color: #333;
            color: white;
            margin-top: 20px;
        }

        /* 画像スタイル */
        img {
            max-width: 100%;
            height: auto;
        }

        /* 見出しスタイル */
        h1, h2, h3 {
            margin: 0 0 10px 0;
        }

        p {
            text-align: justify;
        }
    </style>
</head>
<body>

    <!-- ヘッダー -->
    <header>
        <h1>今日のニュース</h1>
        <p>最新のニュースをお届けします</p>
    </header>

    <!-- コンテンツ領域 -->
    <div class="container">
        <!-- メイン記事 -->
        <article class="main-article">
            <h2>'''+title+'''</h2>
            <!--img src="main-article.jpg" alt="メイン記事の画像"-->
            <p>'''+text+'''</p>
        </article>
    </div>


    <footer>
        <h2>記事制作者</h2>
        <p>'''+user_name+'''</p>
    </footer>

</body>
</html>
'''
    while 1:
     try:
      if a==0:
       f = open('{}test.html'.format(out_path), 'x', encoding='UTF-8')
       break
      else:
        f = open('{}test_{}.html'.format(out_path,str(a)), 'x', encoding='UTF-8')
        break

     except:
      a+=1

    f.write(output)
    f.close()





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
    # 登録成功のメッセージボックスを表示
    #messagebox.showinfo("ファイル選択", "次に変換するファイルを選択してください")
    make_html(text_file_path,title,fr_text,user_name)
    # テキストエリアに入力情報を表示
    info = f"""
タイトル: {title}
性別: {user_name}
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

label_user_name = tk.Label(app, text="筆者の名前", anchor=tk.CENTER)
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