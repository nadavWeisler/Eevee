import os

from flask import Flask, request, send_from_directory
import requests
import os

import __data__ as data

app = Flask(data.__app_name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return send_from_directory('templates', 'index.html')
    else:
        name = request.form.get("name")
        email = request.values.get("email")
        trello1 = request.values.get("trello1")
        trello2 = request.values.get("trello2")
        trello3 = request.values.get("trello3")
        moodleUserName = request.values.get("moodleUserName")
        moodlePassword = request.values.get("moodlePassword")
        r = requests.post(os.environ.get("SIGNUP_HOST")+"?name=" + name + '&email=' + email + '&trello_api_key=' +
                          trello1 + '&trello_api_secret=' + trello2 + '&trello_token=' + trello3 + '&moodle_username=' + moodleUserName + '&moodle_password=' + moodlePassword)

        result = r.text.find('"rt": "1"') != -1
        if result:
            return send_from_directory('templates', 'thankYou.html')
        else:
            return send_from_directory('templates', 'error.html')


@app.route('/favicon.ico')
def icon():
    return send_from_directory(app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')


app.run(port=5000)
