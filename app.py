import os
from flask import Flask, render_template, request, session
from chatbot import append_interaction_to_chat_log, ask


if os.path.exists('config.env'):
    print('Importing environment from .env file')
    for line in open('config.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1].replace("\"", "")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.static_folder = 'static'


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    incoming_msg = request.args.get('msg')
    print(incoming_msg)
    chat_log = session.get('chat_log')
    # chat_log = None
    print("\n======================")
    print(chat_log)

    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
                                                         chat_log)
    return str(answer)


if __name__ == "__main__":
    app.run()