# 🛡️ Fraud Detection Service

A simple AI-powered fraud detection service that analyzes transactions for suspicious activity using OpenAI and rule-based detection.

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/fraud-service-python.git
cd fraud-service-python
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python start.py
```

### 4. Open in Browser
Go to: `http://localhost:8000`

## 🎯 How to Use

1. **Enter a transaction** in the text box
2. **Click example buttons** to try pre-built examples
3. **Click "Analyze"** to get fraud detection results
4. **View results** with fraud score and risk level

## 🔧 Features

- **AI Analysis**: Uses OpenAI GPT for intelligent fraud detection
- **Rule-Based Detection**: Works without API keys using pattern matching
- **Web Interface**: Beautiful, responsive design
- **Real-Time Results**: Instant fraud scoring
- **Example Transactions**: Pre-built test cases

## 🔑 Optional: OpenAI API Key

For enhanced AI analysis, set your OpenAI API key:

**Windows:**
```bash
set OPENAI_API_KEY=your-api-key-here
python start.py
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY=your-api-key-here
python start.py
```

**Get API Key:** [OpenAI Platform](https://platform.openai.com/api-keys)

## 📊 Example Transactions

- **Normal**: "User u99 spent $129.99 at local store" → LEGIT
- **Suspicious**: "User u99 made urgent wire transfer of $5000 at 3am" → FRAUD
- **High-Risk**: "User u99 purchased bitcoin worth $2000" → FRAUD

## 🌐 API Endpoints

- `GET /` - Web interface
- `GET /health` - Health check
- `POST /v1/score` - OpenAI analysis
- `POST /v1/score/hf` - Rule-based analysis
- `GET /docs` - API documentation

## 🚀 Deployment Options

### Heroku
1. Create `Procfile`:
```
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```
2. Deploy to Heroku

### Docker
1. Create `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```
2. Build and run:
```bash
docker build -t fraud-detection .
docker run -p 8000:8000 fraud-detection
```

### VPS/Cloud
```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 📁 Project Structure

```
fraud-service-python/
├── app/
│   ├── main.py              # FastAPI application
│   ├── schemas.py           # Data models
│   └── providers/
│       ├── openai_provider.py    # OpenAI integration
│       └── hf_provider.py        # Rule-based detection
├── static/
│   ├── index.html           # Web interface
│   ├── style.css            # Styling
│   └── script.js            # Frontend logic
├── requirements.txt         # Dependencies
├── start.py                 # Easy startup script
└── README.md               # This file
```

## 🛠️ Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- OpenAI API key (optional)

## 📝 License

MIT License - feel free to use this project for learning and development!

## 📄 Copyright

© 2024 Ravi N. All rights reserved.

Built with ❤️ using FastAPI, OpenAI, and modern web technologies.

---

**Ready to detect fraud? Start the service and analyze your first transaction!** 🚀