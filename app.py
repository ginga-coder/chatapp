from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# チャットのメッセージを格納するリスト（最大10件まで）
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        message = request.form['message']
        if message.strip():  # メッセージが空でない場合のみ追加
            if len(messages) >= 10:
                messages.pop(0)  # 最古のメッセージを削除
            messages.append(message)
    return render_template('chat.html', messages=messages)

if __name__ == '__main__':
    app.run()
