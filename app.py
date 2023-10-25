from flask import Flask, render_template, session, jsonify, request
from apps.calculator.routes import calculator_bp
from apps.memory_game.routes import memory_game_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(calculator_bp, url_prefix='/calculator')
app.register_blueprint(memory_game_bp, url_prefix='/memory_game')

@app.route('/')
def home():
    return render_template('home.html', is_homepage=True)

@app.route('/fun')
def fun():
    return render_template('fun.html')

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