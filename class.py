from task import Flask

app = Flask(__name__)
@app.route("/key")

def display_word():
    return 'Hello'

if(__name__ == '__main__'):
    app.run(debug = True)