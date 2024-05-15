from datetime import datetime
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	return f'<h1>Hello, World!<br>Current Time: {current_time}</h1>'
