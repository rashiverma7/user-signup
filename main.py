from flask import Flask
from flask import render_template
from flask import request
import database.models as db_handler

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        print(username)
        password = request.form['password']
        print(password)
        db_handler.create_table()
        db_handler.insert_user(username, password)
        users = db_handler.fetch_user()
        print(users)
        return render_template('index.html', users=users)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1')
