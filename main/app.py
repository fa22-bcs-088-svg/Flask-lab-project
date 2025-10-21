from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Example quiz questions
questions = [
    {"id": 1, "question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": "Paris"},
    {"id": 2, "question": "Which language runs in a web browser?", "options": ["Python", "C++", "JavaScript"], "answer": "JavaScript"},
    {"id": 3, "question": "What does CSS stand for?", "options": ["Cascading Style Sheets", "Computer Style System", "Colorful Style Sheets"], "answer": "Cascading Style Sheets"}
]

@app.route('/')
def quiz_home():
    return render_template('quiz.html', questions=questions)

@app.route('/health')
def health():
    return "OK", 200

@app.route('/data', methods=['POST'])
def get_quiz_data():
    user_answers = request.get_json().get('answers', {})
    score = 0
    for q in questions:
        if user_answers.get(str(q["id"])) == q["answer"]:
            score += 1

    return jsonify({
        "score": score,
        "total": len(questions),
        "message": f"You scored {score}/{len(questions)}"
    })

if __name__ == "__main__":
    app.run(debug=True)