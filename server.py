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


@app.route('/step3')
def step3():
    listing = [
        {'name': 'Tote bag', 'definition': 'Mixtape church-key gentrify master cleanse polaroid fixie. Viral knausgaard butcher edison bulb tattooed ennui chicharrones salvia pop-up.'},
        {'name': 'Authentic', 'definition': 'Banjo food truck knausgaard put a bird on it, direct trade glossier iPhone hoodie tilde semiotics vinyl pop-up disrupt pinterest humblebrag.'},
        {'name': 'VHS', 'definition': 'Activated charcoal authentic raw denim fixie, prism man braid ennui taxidermy. Hashtag narwhal XOXO listicle poutine.'},
        {'name': 'Helvetica', 'definition': 'YOLO keytar freegan lomo adaptogen hoodie cold-pressed green juice kinfolk succulents cred.'},
        {'name': 'Banjo', 'definition': 'Bushwick live-edge distillery, quinoa gochujang skateboard squid la croix tbh wolf man braid tattooed YOLO four dollar toast.'}
    ]
    return render_template('step3.html', listing=listing)


if __name__ == "__main__":
    app.run(
        host="localhost",
        port=5000,
        debug=True
    )
