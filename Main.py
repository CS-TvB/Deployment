from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Pls work my dude'

if __name__ == '__main__':
    # Run the app when the program starts!
    app.run(debug=True)