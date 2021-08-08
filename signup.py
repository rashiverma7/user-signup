import database.models as db_connect


def new_user_signup(request):
    username = request.form['username']
    password = request.form['password']
    message = ""
    is_user_exists = False
    db_connect.create_table()
    user_list = db_connect.fetch_user(username)
    if not user_list:
        db_connect.insert_user(username, password)
        user_list = db_connect.fetch_user(username)
    else:
        is_user_exists = True
        message = "User already exists!"
    return user_list, message, is_user_exists
