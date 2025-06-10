from flask import Flask, request
from pyexpat.errors import messages

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'Recruto')
    message = request.args.get ('message', 'Давай дружить')
    return f"Hello {name}! {message}!"

if __name__ == '__main__':
    app.run(debug=True)
