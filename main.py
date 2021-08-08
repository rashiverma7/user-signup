from flask import Flask
from flask import request, render_template
import database.models as db_connect

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db_connect.create_table()
        db_connect.insert_user(username, password)
        current_user = db_connect.fetch_user(username)
        return render_template('index.html', users=current_user)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1')
