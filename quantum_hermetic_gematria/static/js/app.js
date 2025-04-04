document.addEventListener('DOMContentLoaded', () => {
    // Tab switching
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabId = btn.dataset.tab;
            
            // Update active states
            tabBtns.forEach(b => b.classList.remove('active'));
            tabContents.forEach(c => c.classList.remove('active'));
            
            btn.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        });
    });
    
    // Add info button to show formula visualization
    const header = document.querySelector('header');
    const infoBtn = document.createElement('button');
    infoBtn.classList.add('info-btn');
    infoBtn.innerHTML = '<span>ℹ️</span> How It Works';
    header.appendChild(infoBtn);
    
    // Create modal for formula visualization
    const modal = document.createElement('div');
    modal.classList.add('modal');
    modal.innerHTML = `
        <div class="modal-content">
            <span class="close-btn">&times;</span>
            <h2>Quantum Hermetic Gematria Formula</h2>
            
            <div class="formula-visualization">
                <div class="formula-step">
                    <h3>1. Text to Vector Transformation</h3>
                    <p>Your text is converted to a quantum vector by:</p>
                    <div class="formula-code">Text → Character mapping → Normalized vectors → Combined resonance field</div>
                </div>
                
                <div class="formula-step">
                    <h3>2. Pattern Recognition</h3>
                    <p>The vector is analyzed for hermetic patterns:</p>
                    <div class="formula-code">Vector → Pattern matching → Geometric alignment → Significance calculation</div>
                </div>
                
                <div class="formula-step">
                    <h3>3. Quantum Resonance</h3>
                    <p>The vibrational coherence is measured by:</p>
                    <div class="formula-code">Vector magnitude × Harmonic alignment × Divine proportions</div>
                </div>
                
                <div class="formula-step">
                    <h3>4. Interpretation Matrix</h3>
                    <p>Results are mapped to traditional hermetic principles:</p>
                    <div class="formula-code">Normalized vector → Hermetic correspondences → Pattern classification</div>
                </div>
            </div>
        </div>
    `;
    document.body.appendChild(modal);
    
    // Modal functionality
    infoBtn.addEventListener('click', () => {
        modal.style.display = 'block';
    });
    
    const closeBtn = modal.querySelector('.close-btn');
    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none';
    });
    
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });

    // Analysis functionality
    const analysisInput = document.getElementById('analysis-input');
    const analyzeBtn = document.getElementById('analyze-btn');
    const analysisResults = document.getElementById('analysis-results');

    analyzeBtn.addEventListener('click', async () => {
        const text = analysisInput.value.trim();
        if (!text) return;

        showLoading(analysisResults);
        try {
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text })
            });
            const result = await response.json();
            displayAnalysisResults(result, text);
        } catch (error) {
            showError(analysisResults, 'Analysis failed. Please try again.');
        }
    });

    // Comparison functionality
    const phrase1Input = document.getElementById('phrase1-input');
    const phrase2Input = document.getElementById('phrase2-input');
    const compareBtn = document.getElementById('compare-btn');
    const comparisonResults = document.getElementById('comparison-results');

    compareBtn.addEventListener('click', async () => {
        const phrase1 = phrase1Input.value.trim();
        const phrase2 = phrase2Input.value.trim();
        if (!phrase1 || !phrase2) return;

        showLoading(comparisonResults);
        try {
            const response = await fetch('/compare', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ phrase1, phrase2 })
            });
            const result = await response.json();
            displayComparisonResults(result, phrase1, phrase2);
        } catch (error) {
            showError(comparisonResults, 'Comparison failed. Please try again.');
        }
    });

    // History functionality
    const historyList = document.getElementById('history-list');
    const clearHistoryBtn = document.getElementById('clear-history-btn');

    async function loadHistory() {
        try {
            const response = await fetch('/history');
            const history = await response.json();
            displayHistory(history);
        } catch (error) {
            showError(historyList, 'Failed to load history.');
        }
    }

    clearHistoryBtn.addEventListener('click', async () => {
        try {
            await fetch('/clear_history', { method: 'POST' });
            historyList.innerHTML = '<p>History cleared.</p>';
        } catch (error) {
            showError(historyList, 'Failed to clear history.');
        }
    });

    // Display functions
    function displayAnalysisResults(result, text) {
        const html = `
            <div class="result-card">
                <h3>"${text}"</h3>
                <div class="metric-group">
                    <p>
                        <span class="metric-label">Quantum Resonance:</span> 
                        <span class="metric-value">${result.quantum_resonance}</span>
                        <span class="info-icon" title="${result.explanations.quantum_resonance}">ℹ️</span>
                    </p>
                    <p>
                        <span class="metric-label">Pattern Significance:</span>
                        <span class="metric-value">${result.pattern_significance}</span>
                        <span class="info-icon" title="${result.explanations.pattern_significance}">ℹ️</span>
                    </p>
                </div>

                <div class="metric-group">
                    <h4>Interpretation</h4>
                    <p>
                        <span class="metric-label">Primary Pattern:</span> 
                        ${result.interpretation.primary_pattern}
                        <span class="info-icon" title="${result.explanations.primary_pattern}">ℹ️</span>
                    </p>
                    <p>
                        <span class="metric-label">Resonance Quality:</span> 
                        ${result.interpretation.resonance_quality}
                        <span class="info-icon" title="${result.explanations.resonance_quality}">ℹ️</span>
                    </p>
                    <p>
                        <span class="metric-label">Geometric Harmony:</span> 
                        ${result.interpretation.geometric_harmony}
                        <span class="info-icon" title="${result.explanations.geometric_harmony}">ℹ️</span>
                    </p>
                </div>

                <div class="metric-group">
                    <h4>Energetic Properties</h4>
                    <div class="energy-bars">
                        <div class="energy-bar">
                            <span class="energy-label">Harmony</span>
                            <div class="bar-container">
                                <div class="bar-fill" style="width: ${result.energetic_properties.harmony * 100}%"></div>
                            </div>
                            <span class="energy-value">${(result.energetic_properties.harmony).toFixed(2)}</span>
                        </div>
                        <div class="energy-bar">
                            <span class="energy-label">Power</span>
                            <div class="bar-container">
                                <div class="bar-fill" style="width: ${result.energetic_properties.power * 100}%"></div>
                            </div>
                            <span class="energy-value">${(result.energetic_properties.power).toFixed(2)}</span>
                        </div>
                        <div class="energy-bar">
                            <span class="energy-label">Intelligence</span>
                            <div class="bar-container">
                                <div class="bar-fill" style="width: ${Math.abs(result.energetic_properties.intelligence) * 100}%"></div>
                            </div>
                            <span class="energy-value">${(Math.abs(result.energetic_properties.intelligence)).toFixed(2)}</span>
                        </div>
                        <div class="energy-bar">
                            <span class="energy-label">Creativity</span>
                            <div class="bar-container">
                                <div class="bar-fill" style="width: ${result.energetic_properties.creativity * 100}%"></div>
                            </div>
                            <span class="energy-value">${(result.energetic_properties.creativity).toFixed(2)}</span>
                        </div>
                        <div class="energy-bar">
                            <span class="energy-label">Balance</span>
                            <div class="bar-container">
                                <div class="bar-fill" style="width: ${Math.abs(result.energetic_properties.balance) * 100}%"></div>
                            </div>
                            <span class="energy-value">${(Math.abs(result.energetic_properties.balance)).toFixed(2)}</span>
                        </div>
                    </div>
                </div>
            </div>
        `;
        analysisResults.innerHTML = html;
        
        // Add tooltips
        const tooltips = document.querySelectorAll('.info-icon');
        tooltips.forEach(tooltip => {
            tooltip.addEventListener('mouseenter', function() {
                const tooltipText = document.createElement('div');
                tooltipText.classList.add('tooltip-text');
                tooltipText.textContent = this.getAttribute('title');
                this.appendChild(tooltipText);
            });
            
            tooltip.addEventListener('mouseleave', function() {
                const tooltipText = this.querySelector('.tooltip-text');
                if (tooltipText) {
                    tooltipText.remove();
                }
            });
        });
    }

    function displayComparisonResults(result, phrase1, phrase2) {
        const html = `
            <div class="result-card">
                <h3>Comparison Results</h3>
                <div class="metric-group">
                    <p><span class="metric-label">Overall Compatibility:</span>
                       <span class="metric-value">${result.overall_compatibility_score}%</span></p>
                    <p><span class="metric-label">Resonance Compatibility:</span>
                       <span class="metric-value">${result.resonance_compatibility.toFixed(2)}</span></p>
                </div>

                <div class="metric-group">
                    <h4>Relationship Patterns</h4>
                    ${Object.entries(result.relationship_patterns).map(([pattern, data]) => `
                        <p><span class="metric-label">${pattern.replace('_', ' ')}:</span>
                           <span class="metric-value">${data.strength.toFixed(2)}</span>
                           <br><small>${data.description}</small></p>
                    `).join('')}
                </div>

                <div class="recommendations">
                    <h4>Recommendations</h4>
                    ${result.recommendations.map(rec => `<p>• ${rec}</p>`).join('')}
                </div>
            </div>
        `;
        comparisonResults.innerHTML = html;
    }

    function displayHistory(history) {
        const html = `
            <div class="history-section">
                <h3>Recent Analyses</h3>
                ${history.analyses.map(entry => `
                    <div class="history-item">
                        <p class="timestamp">${entry.timestamp}</p>
                        <p><strong>${entry.text}</strong></p>
                        <p>Quantum Resonance: ${entry.result.quantum_resonance.toFixed(2)}</p>
                    </div>
                `).join('')}
            </div>
            <div class="history-section">
                <h3>Recent Comparisons</h3>
                ${history.comparisons.map(entry => `
                    <div class="history-item">
                        <p class="timestamp">${entry.timestamp}</p>
                        <p><strong>${entry.phrase1}</strong> vs <strong>${entry.phrase2}</strong></p>
                        <p>Compatibility: ${entry.result.overall_compatibility_score}%</p>
                    </div>
                `).join('')}
            </div>
        `;
        historyList.innerHTML = html;
    }

    function showLoading(element) {
        element.innerHTML = '<div class="loading"></div>';
    }

    function showError(element, message) {
        element.innerHTML = `<div class="error">${message}</div>`;
    }

    // Load history on startup
    loadHistory();
}); 