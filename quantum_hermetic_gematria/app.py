import os
import torch
import numpy as np
from flask import Flask, render_template, request, jsonify, session, send_from_directory, url_for
import json
from datetime import datetime
import logging
import traceback

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create the Flask app with explicit static folder
current_dir = os.path.dirname(os.path.abspath(__file__))
static_folder = os.path.join(current_dir, 'static')
template_folder = os.path.join(current_dir, 'templates')

app = Flask(__name__, 
            static_folder=static_folder, 
            static_url_path='/static',
            template_folder=template_folder)
app.secret_key = os.urandom(24)  # For session management

# Debug info
logger.debug(f"App instance created. Static folder: {app.static_folder}")
logger.debug(f"Template folder: {app.template_folder}")
logger.debug(f"Static URL path: {app.static_url_path}")

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
        
        # Generate varying results based on actual input
        numerical_value = int(sum(ord(c) for c in text) % 100)
        text_length = len(text)
        vector_sum = sum(vector.tolist())
        
        # Calculate a normalized resonance value that varies with input
        resonance_base = float(torch.norm(vector).item())
        resonance = 0.5 + 0.5 * (hash(text) % 1000) / 1000.0
        
        # Pattern significance varies with text
        pattern_significance = round(0.5 + 0.4 * abs(hash(text) % 100) / 100.0, 2)
        
        # Generate interpretations based on input characteristics
        patterns = ["harmonic_resonance", "quantum_entanglement", "sacred_geometry", 
                   "hermetic_symmetry", "vibrational_matrix"]
        qualities = ["Strong", "Moderate", "Subtle", "Profound", "Complex"]
        geometries = ["vesica_piscis", "golden_spiral", "metatron_cube", 
                     "flower_of_life", "merkaba"]
        
        # Select interpretation elements based on text characteristics
        pattern_index = abs(hash(text)) % len(patterns)
        quality_index = (len(text) + sum(ord(c) for c in text)) % len(qualities)
        geometry_index = (abs(hash(text)) // 100) % len(geometries)
        
        # Generate explanations for each score
        explanations = {
            "quantum_resonance": "Measures the vibrational coherence of the phrase in quantum information space. Higher values indicate stronger resonance with fundamental universal patterns.",
            "pattern_significance": "Indicates how strongly this phrase connects to archetypal patterns. Higher values suggest greater alignment with hermetic principles.",
            "primary_pattern": {
                "harmonic_resonance": "Shows alignment with natural harmonic sequences, suggesting balance and flow.",
                "quantum_entanglement": "Indicates non-local connections across conceptual space-time.",
                "sacred_geometry": "Reveals alignment with fundamental geometric structures of creation.",
                "hermetic_symmetry": "Demonstrates balance across multiple hermetic principles.",
                "vibrational_matrix": "Shows strong connection to the underlying vibrational fabric of reality."
            },
            "resonance_quality": {
                "Strong": "Clear and powerful resonance that manifests consistently.",
                "Moderate": "Balanced resonance with noticeable but not overwhelming effects.",
                "Subtle": "Delicate resonance that works through nuance and refinement.",
                "Profound": "Deep resonance that affects fundamental levels of reality.",
                "Complex": "Multi-layered resonance with intricate patterns of manifestation."
            },
            "geometric_harmony": {
                "vesica_piscis": "The sacred intersection of dualities, representing creation and divine feminine energy.",
                "golden_spiral": "The pattern of perfect growth and proportion found throughout nature.",
                "metatron_cube": "The geometric blueprint containing all Platonic solids and creation patterns.",
                "flower_of_life": "The fundamental pattern of creation containing all geometric forms.",
                "merkaba": "The light-spirit-body vehicle representing balanced energy fields."
            }
        }
        
        # Select specific explanations based on the generated values
        selected_pattern = patterns[pattern_index]
        selected_quality = qualities[quality_index]
        selected_geometry = geometries[geometry_index]
        
        return {
            "text": text,
            "numerical_value": numerical_value,
            "quantum_resonance": round(resonance, 2),
            "energetic_properties": {
                "harmony": float(abs(vector[0]).item()),
                "power": float(abs(vector[1]).item()),
                "intelligence": float(abs(vector[2]).item()),
                "creativity": float(abs(vector[3]).item()),
                "balance": float(abs(vector[4]).item())
            },
            "patterns": {},
            "interpretation": {
                "primary_pattern": selected_pattern,
                "resonance_quality": selected_quality,
                "geometric_harmony": selected_geometry,
                "hermetic_influence": "vibration"
            },
            "pattern_significance": pattern_significance,
            "vector": vector.tolist(),
            "explanations": {
                "quantum_resonance": explanations["quantum_resonance"],
                "pattern_significance": explanations["pattern_significance"],
                "primary_pattern": explanations["primary_pattern"][selected_pattern],
                "resonance_quality": explanations["resonance_quality"][selected_quality],
                "geometric_harmony": explanations["geometric_harmony"][selected_geometry]
            }
        }
    
    def compare_phrases(self, phrase1, phrase2):
        similarity = self.calculate_similarity(phrase1, phrase2)
        
        # Calculate a compatibility score that varies with input
        phrase_sum = len(phrase1) + len(phrase2)
        hash_val = hash(phrase1 + phrase2)
        compatibility = int(max(30, min(95, (similarity + 1) * 30 + (hash_val % 40))))
        
        # Generate different interpretations based on compatibility
        if compatibility > 80:
            interpretation = "These phrases share significant energetic harmony."
        elif compatibility > 60:
            interpretation = "These phrases have strong resonance."
        elif compatibility > 40:
            interpretation = "These phrases have moderate harmonic connection."
        else:
            interpretation = "These phrases show limited energetic alignment."
        
        # Generate varied resonance patterns
        resonance_strength = round(0.3 + 0.7 * (hash_val % 100) / 100, 2)
        synergy_level = round(0.2 + 0.8 * ((hash_val // 100) % 100) / 100, 2)
        
        # Generate varied relationship patterns
        patterns = {
            "harmonic_resonance": {
                "strength": round(0.5 + 0.5 * (hash_val % 100) / 100, 2),
                "description": "Natural flow and mutual enhancement"
            },
            "quantum_entanglement": {
                "strength": round(0.3 + 0.6 * ((hash_val // 200) % 100) / 100, 2),
                "description": "Deep connection across conceptual space"
            }
        }
        
        # Generate recommendations based on compatibility
        recommendations = []
        if compatibility > 70:
            recommendations.append("These concepts share natural resonance.")
        else:
            recommendations.append("Consider exploring complementary elements.")
            
        if phrase_sum % 2 == 0:
            recommendations.append("Focus on harmonic aspects for best results.")
        else:
            recommendations.append("Balance opposing elements for optimal outcome.")
        
        return {
            "phrase1": phrase1,
            "phrase2": phrase2,
            "similarity": similarity,
            "compatibility": compatibility,
            "resonance_patterns": {"harmonic": resonance_strength},
            "energetic_interactions": {"synergy": synergy_level},
            "interpretation": interpretation,
            "overall_compatibility_score": compatibility,
            "resonance_compatibility": round(similarity, 2),
            "relationship_patterns": patterns,
            "recommendations": recommendations
        }

# Initialize QHG instance
qhg = QuantumHermeticGematria()

@app.route('/')
def index():
    logger.debug("Rendering index.html")
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    logger.debug(f"Serving static file: {filename} from {app.static_folder}")
    try:
        return send_from_directory(app.static_folder, filename)
    except Exception as e:
        logger.error(f"Error serving static file {filename}: {str(e)}")
        logger.error(traceback.format_exc())
        return f"Error serving static file: {str(e)}", 404

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        logger.debug("Analyze endpoint called")
        data = request.get_json()
        logger.debug(f"Received data: {data}")
        text = data.get('text', '')
        
        if not text:
            logger.warning("Empty text received")
            return jsonify({"error": "No text provided"}), 400
            
        # Perform analysis
        result = qhg.analyze_text(text)
        logger.debug(f"Analysis result: {result}")
        
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
        logger.error(f"Error in analyze: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({"error": str(e), "stack": traceback.format_exc()}), 500

@app.route('/compare', methods=['POST'])
def compare():
    try:
        logger.debug("Compare endpoint called")
        data = request.get_json()
        logger.debug(f"Received data: {data}")
        phrase1 = data.get('phrase1', '')
        phrase2 = data.get('phrase2', '')
        
        if not phrase1 or not phrase2:
            logger.warning("Empty phrases received")
            return jsonify({"error": "Both phrases are required"}), 400
        
        # Perform comparison
        result = qhg.compare_phrases(phrase1, phrase2)
        logger.debug(f"Comparison result: {result}")
        
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
        logger.error(f"Error in compare: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({"error": str(e), "stack": traceback.format_exc()}), 500

@app.route('/history')
def history():
    try:
        logger.debug("History endpoint called")
        history_data = {
            'analyses': session.get('history', []),
            'comparisons': session.get('comparisons', [])
        }
        logger.debug(f"History data: {history_data}")
        return jsonify(history_data)
    except Exception as e:
        logger.error(f"Error in history: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({"error": str(e), "stack": traceback.format_exc()}), 500

@app.route('/clear_history', methods=['POST'])
def clear_history():
    try:
        logger.debug("Clear history endpoint called")
        session.clear()
        return jsonify({'status': 'success'})
    except Exception as e:
        logger.error(f"Error in clear_history: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({"error": str(e), "stack": traceback.format_exc()}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port) 