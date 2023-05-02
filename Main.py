from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'It finaly works jaaayy!!'

if __name__ == '__main__':
    # Run the app when the program starts!
    #comment
    app.run(debug=True)