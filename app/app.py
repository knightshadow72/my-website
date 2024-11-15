from flask import Flask, render_template, request


app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)