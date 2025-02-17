from flask import Flask, jsonify

app = Flask(__name__)

# Your data dictionary
data = {
    "Chicken": 76,
    "Computer Science (Major)": 11,
    "Computer Science (Special)": 37,
    "Fish": 6,
    "Information Technology (Major)": 26,
    "Information Technology (Special)": 18,
    "Vegetable": 10
}

@app.route('/')
def home():
    return "Welcome to the Flask API - Routes are /stats and /add/a/b, /subtract/a/b, /multiply/a/b, /divide/a/b"

@app.route('/stats')
def get_stats():
    meal_preferences = {
        "Chicken": data["Chicken"],
        "Fish": data["Fish"],
        "Vegetable": data["Vegetable"]
    }

    programmes = {
        "Computer Science": {
            "Major": data["Computer Science (Major)"],
            "Special": data["Computer Science (Special)"]
        },
        "Information Technology": {
            "Major": data["Information Technology (Major)"],
            "Special": data["Information Technology (Special)"]
        }
    }

    return jsonify({
        "meal_preferences": meal_preferences,
        "programmes": programmes
    })

@app.route('/add/<a>/<b>')
def add(a, b):
    try:
        return jsonify({"result": float(a) + float(b)})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide numbers"}), 400

@app.route('/subtract/<a>/<b>')
def subtract(a, b):
    try:
        return jsonify({"result": float(a) - float(b)})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide numbers"}), 400

@app.route('/multiply/<a>/<b>')
def multiply(a, b):
    try:
        return jsonify({"result": float(a) * float(b)})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide numbers"}), 400

@app.route('/divide/<a>/<b>')
def divide(a, b):
    try:
        b_float = float(b)
        if b_float == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400
        return jsonify({"result": float(a) / b_float})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide numbers"}), 400

app.run(host='0.0.0.0')