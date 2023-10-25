from flask import Blueprint, render_template, jsonify, request, session
from random import shuffle

memory_game_bp = Blueprint('memory_game', __name__, template_folder='templates/memory_game')

@memory_game_bp.route('/')
def index():
    return render_template('memory_game/memory_game_template.html')

@memory_game_bp.route('/generate_sequence', methods=['GET'])
def generate_sequence():
    sequence = list(range(1, 8))  # creates a list [1, 2, 3, 4, 5, 6, 7]
    shuffle(sequence)  # shuffles the list
    session['sequence'] = sequence
    print("Generated sequence:", sequence)
    return jsonify(success=True, sequence=sequence)

@memory_game_bp.route('/check_sequence', methods=['POST'])
def check_sequence():
    user_sequence = request.json.get('sequence', [])
    print("User sequence:", user_sequence)
    print("Expected sequence:", session.get('sequence'))
    if user_sequence == session.get('sequence'):
        return jsonify(correct=True)
    return jsonify(correct=False)

