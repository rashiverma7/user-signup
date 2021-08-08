from flask import Flask
from flask import request, render_template
from signup import new_user_signup

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        user_list, message, is_user_exists = new_user_signup(request)
        return render_template('index.html', users=user_list,
                               message=message, user_flag=is_user_exists)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1')
