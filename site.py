from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/certificate/python')
def python_certificate():
    return render_template('templates/certificate_python.html')

if __name__ == '__main__':
    app.run(debug=True)