from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'HELLO WORLD - my name is sourav you are visiting my website'
app.run(host="0.0.0.0", port=5000)