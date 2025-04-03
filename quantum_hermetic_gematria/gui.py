import tkinter as tk
from tkinter import ttk, scrolledtext
import json
from qhg import QuantumHermeticGematria
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from matplotlib.gridspec import GridSpec

class QHGApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quantum Hermetic Gematria Analyzer")
        self.qhg = QuantumHermeticGematria()
        
        # Configure style for a mystical appearance
        style = ttk.Style()
        style.configure("Title.TLabel", font=("Helvetica", 18, "bold"))
        style.configure("Mystical.TLabel", font=("Helvetica", 12, "italic"))
        style.configure("Sacred.TFrame", background="#1a1a2e")
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame with sacred geometry background
        main_frame = ttk.Frame(self.root, padding="10", style="Sacred.TFrame")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title with mystical styling
        title = ttk.Label(main_frame, text="Quantum Hermetic Gematria", style="Title.TLabel")
        title.grid(row=0, column=0, columnspan=2, pady=10)
        
        subtitle = ttk.Label(main_frame, 
                           text="Unveiling Divine Patterns Through Sacred Mathematics",
                           style="Mystical.TLabel")
        subtitle.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Input section
        input_frame = ttk.LabelFrame(main_frame, text="Sacred Input", padding="5")
        input_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(input_frame, text="Enter Text:").grid(row=0, column=0, padx=5)
        self.text_input = ttk.Entry(input_frame, width=40)
        self.text_input.grid(row=0, column=1, padx=5)
        
        ttk.Label(input_frame, text="Gematria System:").grid(row=1, column=0, padx=5)
        self.system_var = tk.StringVar(value="quantum_hermetic")
        system_combo = ttk.Combobox(input_frame, textvariable=self.system_var)
        system_combo['values'] = ('quantum_hermetic', 'english_ordinal', 'english_qbl', 'greek', 'hebrew')
        system_combo.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        
        # Analyze button with sacred geometry
        analyze_btn = ttk.Button(main_frame, text="⚡ Analyze Divine Patterns ⚡", 
                               command=self.analyze_text)
        analyze_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Results section
        results_frame = ttk.LabelFrame(main_frame, text="Divine Revelations", padding="5")
        results_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Text results with mystical styling
        self.results_text = scrolledtext.ScrolledText(results_frame, width=50, height=10,
                                                    font=("Helvetica", 10))
        self.results_text.grid(row=0, column=0, padx=5, pady=5)
        
        # Visualization frame
        viz_frame = ttk.LabelFrame(main_frame, text="Sacred Geometry Visualization", padding="5")
        viz_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Create matplotlib figure with multiple subplots
        self.fig = plt.figure(figsize=(12, 8))
        gs = GridSpec(2, 2, figure=self.fig)
        
        # Sacred geometry plot
        self.ax_geometry = self.fig.add_subplot(gs[0, 0])
        self.ax_geometry.set_title("Sacred Geometry Resonance")
        
        # Hermetic principles plot
        self.ax_hermetic = self.fig.add_subplot(gs[0, 1])
        self.ax_hermetic.set_title("Hermetic Principle Alignment")
        
        # Quantum state plot
        self.ax_quantum = self.fig.add_subplot(gs[1, 0])
        self.ax_quantum.set_title("Quantum State Visualization")
        
        # Harmonic resonance plot
        self.ax_harmonic = self.fig.add_subplot(gs[1, 1])
        self.ax_harmonic.set_title("Harmonic Resonance Pattern")
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=viz_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5)
        
    def analyze_text(self):
        text = self.text_input.get()
        system = self.system_var.get()
        
        if not text:
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "Please enter sacred text to analyze.")
            return
        
        # Get analysis results
        results = self.qhg.analyze_text(text, system)
        
        # Display text results with formatting
        self.results_text.delete(1.0, tk.END)
        self.format_results(results)
        
        # Update visualizations
        self.update_visualization(results)
        
    def format_results(self, results):
        """Format results with mystical styling"""
        self.results_text.insert(tk.END, "✧ Divine Analysis Results ✧\n\n")
        
        self.results_text.insert(tk.END, f"Base Value: {results['base_value']}\n")
        self.results_text.insert(tk.END, f"Quantum Resonance: {results['quantum_resonance']:.2f}\n")
        self.results_text.insert(tk.END, f"Harmonic Resonance: {results['harmonic_resonance']:.2f}\n\n")
        
        self.results_text.insert(tk.END, "Sacred Geometry Patterns:\n")
        for pattern, value in results['geometry_resonance'].items():
            self.results_text.insert(tk.END, f"  • {pattern}: {value:.2f}\n")
        
        self.results_text.insert(tk.END, f"\nDominant Pattern: {results['dominant_pattern']}\n")
        self.results_text.insert(tk.END, f"Dominant Principle: {results['dominant_principle']}\n\n")
        
        self.results_text.insert(tk.END, "Hermetic Resonances:\n")
        for principle, value in results['hermetic_resonances'].items():
            self.results_text.insert(tk.END, f"  • {principle.title()}: {value:.2f}\n")
        
    def update_visualization(self, results):
        """Update all visualization plots"""
        # Clear the entire figure
        self.fig.clear()
        
        # Recreate subplots
        gs = GridSpec(2, 2, figure=self.fig)
        self.ax_geometry = self.fig.add_subplot(gs[0, 0])
        self.ax_hermetic = self.fig.add_subplot(gs[0, 1])
        self.ax_quantum = self.fig.add_subplot(gs[1, 0])
        self.ax_harmonic = self.fig.add_subplot(gs[1, 1])
            
        # Plot sacred geometry resonance
        patterns = list(results['geometry_resonance'].keys())
        values = list(results['geometry_resonance'].values())
        bars = self.ax_geometry.bar(patterns, values)
        self.ax_geometry.set_title("Sacred Geometry Resonance")
        plt.setp(self.ax_geometry.xaxis.get_majorticklabels(), rotation=45)
        
        # Highlight dominant pattern
        dominant_idx = patterns.index(results['dominant_pattern'])
        bars[dominant_idx].set_color('gold')
        
        # Plot hermetic principles
        principles = list(results['hermetic_resonances'].keys())
        values = list(results['hermetic_resonances'].values())
        self.ax_hermetic.plot(principles, values, 'o-', color='purple')
        self.ax_hermetic.set_title("Hermetic Principle Alignment")
        plt.setp(self.ax_hermetic.xaxis.get_majorticklabels(), rotation=45)
        
        # Plot quantum state
        quantum_state = np.array(results['quantum_state'])
        self.ax_quantum.plot(quantum_state, 'r--o')
        self.ax_quantum.set_title("Quantum State")
        
        # Plot harmonic resonance
        x = np.linspace(0, 2*np.pi, 100)
        y = np.sin(x * results['harmonic_resonance'])
        self.ax_harmonic.plot(x, y, color='blue')
        self.ax_harmonic.set_title("Harmonic Resonance")
        
        # Adjust layout and redraw
        plt.tight_layout()
        self.canvas.draw()
        self.canvas.flush_events()  # Force update

def main():
    root = tk.Tk()
    app = QHGApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 