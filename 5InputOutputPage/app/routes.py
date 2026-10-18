from flask import Blueprint, render_template, request
main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        message = f"Hello {username}, Welcome to our Flask!"
    return render_template('index.html', message=message)