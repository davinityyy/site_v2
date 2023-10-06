from flask import Flask, render_template, jsonify, request, session

app = Flask(__name__)
app.secret_key = 'sudos_mama'

@app.route('/')
def home():
    return render_template('home.html', is_homepage=True)

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/certification')
def certification():
    return render_template('certification.html')

if __name__ == "__main__":
    app.run(debug=True)
