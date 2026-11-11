from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/About')
def about():
    return render_template('About.html')

@app.route('/Contact')
def contact():
    return render_template('Contact.html')


@app.route('/Services')
def services():
    return render_template('Services.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )