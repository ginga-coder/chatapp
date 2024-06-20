from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# チャットのメッセージを格納するリスト（最大10件まで）
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    if message.strip():  # メッセージが空でない場合のみ追加
        if len(messages) >= 10:
            messages.pop(0)  # 最古のメッセージを削除
        messages.append(message)
    return jsonify({'result': 'success'})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    app.run()
