class FraudDetectionApp {
    constructor() {
        this.initializeElements();
        this.bindEvents();
        this.updateStatus('Ready');
    }

    initializeElements() {
        this.transactionInput = document.getElementById('transaction');
        this.analyzeOpenAIBtn = document.getElementById('analyzeOpenAI');
        this.analyzeHFBtn = document.getElementById('analyzeHF');
        this.resultsContainer = document.getElementById('results');
        this.exampleBtns = document.querySelectorAll('.example-btn');
        this.statusIndicator = document.getElementById('statusIndicator');
        this.statusText = document.getElementById('statusText');
    }

    bindEvents() {
        this.analyzeOpenAIBtn.addEventListener('click', () => this.analyzeTransaction('openai'));
        this.analyzeHFBtn.addEventListener('click', () => this.analyzeTransaction('hf'));
        
        this.exampleBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const text = btn.getAttribute('data-text');
                this.transactionInput.value = text;
            });
        });

        // Allow Enter key to trigger analysis
        this.transactionInput.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 'Enter') {
                this.analyzeTransaction('openai');
            }
        });
    }

    async analyzeTransaction(provider) {
        const transaction = this.transactionInput.value.trim();
        
        if (!transaction) {
            this.showError('Please enter a transaction description');
            return;
        }

        if (transaction.length < 5) {
            this.showError('Transaction description must be at least 5 characters long');
            return;
        }

        this.setLoading(true);

        try {
            const endpoint = provider === 'openai' ? '/v1/score' : '/v1/score/hf';
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ transaction })
            });

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }

            const data = await response.json();
            this.displayResult(data, provider);
            this.updateStatus('Completed', 'completed');

        } catch (error) {
            this.showError(error.message);
            this.updateStatus('Failed', 'failed');
        } finally {
            this.setLoading(false);
        }
    }

    displayResult(data, provider) {
        const riskLevel = this.getRiskLevel(data.score);
        const riskColor = this.getRiskColor(data.score);
        const confidence = this.getConfidenceText(data.score);
        
        this.resultsContainer.innerHTML = `
            <div class="result-card">
                <div class="result-header">
                    <h3><i class="fas fa-${provider === 'openai' ? 'robot' : 'brain'}"></i> ${provider.toUpperCase()} Analysis</h3>
                    <div class="processing-time">
                        <i class="fas fa-clock"></i> ${data.processing_time_ms}ms
                    </div>
                </div>
                
                <div class="result-content">
                    <div class="fraud-indicator ${data.label.toLowerCase()}">
                        <div class="fraud-label">
                            <i class="fas fa-${data.label === 'FRAUD' ? 'exclamation-triangle' : 'check-circle'}"></i>
                            ${data.label}
                        </div>
                        <div class="fraud-score" style="color: ${riskColor}">
                            ${(data.score * 100).toFixed(1)}% ${confidence}
                        </div>
                    </div>
                    
                    <div class="risk-level">
                        <span class="risk-badge" style="background-color: ${riskColor}">
                            ${riskLevel} Risk
                        </span>
                    </div>
                    
                    <div class="transaction-preview">
                        <strong>Transaction:</strong>
                        <p>"${this.transactionInput.value}"</p>
                    </div>
                </div>
            </div>
        `;
    }

    getRiskLevel(score) {
        if (score >= 0.8) return 'Very High';
        if (score >= 0.6) return 'High';
        if (score >= 0.4) return 'Medium';
        if (score >= 0.2) return 'Low';
        return 'Very Low';
    }

    getRiskColor(score) {
        if (score >= 0.8) return '#dc3545';
        if (score >= 0.6) return '#fd7e14';
        if (score >= 0.4) return '#ffc107';
        if (score >= 0.2) return '#28a745';
        return '#6c757d';
    }

    getConfidenceText(score) {
        if (score >= 0.8) return 'Confidence';
        if (score >= 0.6) return 'Confidence';
        if (score >= 0.4) return 'Confidence';
        if (score >= 0.2) return 'Confidence';
        return 'Confidence';
    }

    setLoading(loading) {
        if (loading) {
            this.analyzeOpenAIBtn.disabled = true;
            this.analyzeHFBtn.disabled = true;
            this.analyzeOpenAIBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';
            this.analyzeHFBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';
            this.updateStatus('Processing', 'processing');
        } else {
            this.analyzeOpenAIBtn.disabled = false;
            this.analyzeHFBtn.disabled = false;
            this.analyzeOpenAIBtn.innerHTML = '<i class="fas fa-robot"></i> Analyze with OpenAI';
            this.analyzeHFBtn.innerHTML = '<i class="fas fa-brain"></i> Analyze with Rule-Based';
        }
    }

    showError(message, type = 'error') {
        this.resultsContainer.innerHTML = `
            <div class="error-message ${type}">
                <i class="fas fa-${type === 'error' ? 'exclamation-circle' : 'check-circle'}"></i>
                ${message}
            </div>
        `;
    }

    updateStatus(message, type = 'ready') {
        if (this.statusIndicator && this.statusText) {
            this.statusIndicator.className = `status-indicator ${type}`;
            this.statusText.textContent = message;
        }
        console.log(`Status: ${message}`);
    }
}

// Initialize the app when the page loads
let app;
document.addEventListener('DOMContentLoaded', () => {
    app = new FraudDetectionApp();
});