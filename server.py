from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello!'


@app.route('/step1')
def step1():
    return render_template('step1.html')


@app.route('/step2/<id>')
@app.route('/step2/<id>/extra/<extra>')
def step2(id, extra=None):
    return render_template('step2.html', id=id, extra=extra)

if __name__ == "__main__":
    app.run(
        host="localhost",
        port=5000,
        debug=True
    )
