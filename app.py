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
        trello_api_secret = request.values.get("trello_api_secret")
        trello_token = request.values.get("trello_token")
        trello_api_key = request.values.get("trello_api_key")
        moodle_username = request.values.get("moodle_username")
        moodle_password = request.values.get("moodle_password")
        r = requests.post(os.environ.get("SIGNUP_HOST")+"?name=" + name + '&email=' + email + '&trello_api_key=' +
                          trello_api_key + '&trello_api_secret=' + trello_api_secret + '&trello_token=' + trello_token +
                          '&moodle_username=' + moodle_username + '&moodle_password=' + moodle_password)

        result = r.text.find('"status_code": "200"') != -1
        print(r.status_code)
        if r.status_code == 200 or result:
            return send_from_directory('templates', 'thankYou.html')
        else:
            return send_from_directory('templates', 'error.html')


@app.route('/favicon.ico')
def icon():
    return send_from_directory(app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(debug=True)
