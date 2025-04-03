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
                    <p><span class="metric-label">Quantum Resonance:</span> 
                       <span class="metric-value">${result.quantum_resonance.toFixed(2)}</span></p>
                    <p><span class="metric-label">Pattern Significance:</span>
                       <span class="metric-value">${result.pattern_significance.toFixed(2)}</span></p>
                </div>

                <div class="metric-group">
                    <h4>Interpretation</h4>
                    <p><span class="metric-label">Primary Pattern:</span> ${result.interpretation.primary_pattern}</p>
                    <p><span class="metric-label">Resonance Quality:</span> ${result.interpretation.resonance_quality}</p>
                    <p><span class="metric-label">Geometric Harmony:</span> ${result.interpretation.geometric_harmony}</p>
                </div>

                ${result.egyptian_technology ? `
                    <div class="metric-group">
                        <h4>Aligned Egyptian Technology</h4>
                        <p><span class="metric-label">Device:</span> ${result.interpretation.aligned_egyptian_tech.device}</p>
                        <p><span class="metric-label">Purpose:</span> ${result.interpretation.aligned_egyptian_tech.purpose}</p>
                    </div>
                ` : ''}

                ${result.modern_equivalents ? `
                    <div class="metric-group">
                        <h4>Modern Equivalent</h4>
                        <p><span class="metric-label">Device:</span> ${result.interpretation.modern_equivalent.device}</p>
                        <p><span class="metric-label">Form:</span> ${result.interpretation.modern_equivalent.common_form}</p>
                    </div>
                ` : ''}
            </div>
        `;
        analysisResults.innerHTML = html;
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