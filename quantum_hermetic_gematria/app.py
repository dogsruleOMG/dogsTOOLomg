from flask import Flask, render_template, request, jsonify, session
from qhg import QuantumHermeticGematria
import json
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

# Initialize QHG
qhg = QuantumHermeticGematria()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    
    # Perform analysis
    result = qhg.analyze_text(text)
    
    # Store in session history
    if 'history' not in session:
        session['history'] = []
    
    analysis_entry = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'text': text,
        'result': result
    }
    
    session['history'] = [analysis_entry] + session['history'][:9]  # Keep last 10 entries
    
    return jsonify(result)

@app.route('/compare', methods=['POST'])
def compare():
    data = request.get_json()
    phrase1 = data.get('phrase1', '')
    phrase2 = data.get('phrase2', '')
    
    # Perform comparison
    result = qhg.compare_phrases(phrase1, phrase2)
    
    # Store in session history
    if 'comparisons' not in session:
        session['comparisons'] = []
    
    comparison_entry = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'phrase1': phrase1,
        'phrase2': phrase2,
        'result': result
    }
    
    session['comparisons'] = [comparison_entry] + session['comparisons'][:9]
    
    return jsonify(result)

@app.route('/history')
def history():
    return jsonify({
        'analyses': session.get('history', []),
        'comparisons': session.get('comparisons', [])
    })

@app.route('/clear_history', methods=['POST'])
def clear_history():
    session.clear()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 