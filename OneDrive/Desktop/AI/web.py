from flask import Flask, render_template, request
from src.agent import chat_with_ai

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':
        message = request.form['message']
        response = chat_with_ai(message)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)