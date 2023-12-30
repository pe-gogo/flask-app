from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detail')
def detail():
    return render_template('detail.html')

@app.route('/public/<path:filename>')
def custom_static(filename):
    return send_from_directory('static', filename)
if __name__ == '__main__':
    app.run(debug=True)
