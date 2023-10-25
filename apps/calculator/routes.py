from flask import Blueprint, jsonify, request, render_template

calculator_bp = Blueprint('calculator', __name__, template_folder='templates/calculator', static_folder='css')

@calculator_bp.route('/')
def index():
    return render_template('calculator/calculator_template.html')

@calculator_bp.route('/calculate', methods=['POST'])
def calculate():
    # get the operation and values from the post request
    operation = request.json['operation']
    value1 = float(request.json['value1'])
    value2 = float(request.json['value2'])
    
    # perform the calculation based on the operation
    if operation == 'add':
        result = value1 + value2
    elif operation == 'subtract':
        result = value1 - value2
    elif operation == 'multiply':
        result = value1 * value2
    elif operation == 'divide':
        result = value1 / value2
    else:
        return jsonify(success=False, error="Invalid operation")
    
    # return the result as json
    return jsonify(success=True, result=result)