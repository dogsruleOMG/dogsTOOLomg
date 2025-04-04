import os
import torch
import numpy as np
from flask import Flask, render_template, request, jsonify, session
import json
from datetime import datetime

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

# Simple QuantumHermeticGematria implementation
class QuantumHermeticGematria:
    def __init__(self, dimension=10, seed=42):
        self.dimension = dimension
        self.seed = seed
        torch.manual_seed(seed)
        np.random.seed(seed)
        self.initialize_vectors()
    
    def initialize_vectors(self):
        self.vectors = {}
        for i, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
            vec = torch.randn(self.dimension)
            self.vectors[char] = vec / torch.norm(vec)
    
    def calculate(self, text):
        text = text.upper()
        result = torch.zeros(self.dimension)
        for char in text:
            if char in self.vectors:
                result += self.vectors[char]
        if torch.norm(result) > 0:
            result = result / torch.norm(result)
        return result
    
    def calculate_similarity(self, text1, text2):
        vec1 = self.calculate(text1)
        vec2 = self.calculate(text2)
        similarity = torch.dot(vec1, vec2)
        return similarity.item()
    
    def analyze_text(self, text):
        vector = self.calculate(text)
        return {
            "text": text,
            "numerical_value": int(torch.sum(vector * 100).item()),
            "quantum_resonance": float(torch.norm(vector).item()),
            "energetic_properties": {
                "harmony": float(abs(vector[0]).item()),
                "power": float(abs(vector[1]).item()),
                "intelligence": float(abs(vector[2]).item()),
                "creativity": float(abs(vector[3]).item()),
                "balance": float(abs(vector[4]).item())
            },
            "patterns": {},
            "interpretation": f"The quantum signature of '{text}' reveals a unique energetic pattern with special harmonic qualities.",
            "vector": vector.tolist()
        }
    
    def compare_phrases(self, phrase1, phrase2):
        similarity = self.calculate_similarity(phrase1, phrase2)
        compatibility = int((similarity + 1) * 50)  # Convert from [-1,1] to [0,100]
        
        if similarity > 0.5:
            interpretation = "These phrases share significant energetic harmony."
        elif similarity > 0:
            interpretation = "These phrases have moderate resonance."
        elif similarity > -0.5:
            interpretation = "These phrases have limited harmonic connection."
        else:
            interpretation = "These phrases show energetic opposition."
        
        return {
            "phrase1": phrase1,
            "phrase2": phrase2,
            "similarity": similarity,
            "compatibility": compatibility,
            "resonance_patterns": {},
            "energetic_interactions": {},
            "interpretation": interpretation
        }

# Initialize QHG instance
qhg = QuantumHermeticGematria()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
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
        
        session['history'] = [analysis_entry] + session['history'][:9]
        
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/compare', methods=['POST'])
def compare():
    try:
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
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port) 