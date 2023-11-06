from flask import Flask, render_template, request

app = Flask(__name__)
chat_messages = []

@app.route('/')
def index():
    return render_template('index.html', chat_messages=chat_messages)

@app.route('/add_message', methods=['POST'])
def add_message():
    user_message = request.form['message']
    if user_message:
        chat_messages.append(f'USER: {user_message}')
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
