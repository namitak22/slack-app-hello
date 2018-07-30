from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World Namita!"

@app.route('/hello', methods=['POST'])
def hello():
    return "Hello!"


