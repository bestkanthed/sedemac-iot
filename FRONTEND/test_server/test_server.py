from flask import Flask, render_template, redirect, send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css',path)

if __name__ == '__main__':
   app.run(debug = True)
