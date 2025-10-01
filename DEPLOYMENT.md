# 🚀 Deployment Guide

This guide shows you how to deploy the Fraud Detection Service to various platforms.

## 🌐 Heroku Deployment

### 1. Install Heroku CLI
Download from: https://devcenter.heroku.com/articles/heroku-cli

### 2. Login to Heroku
```bash
heroku login
```

### 3. Create Heroku App
```bash
heroku create your-app-name
```

### 4. Set Environment Variables (Optional)
```bash
heroku config:set OPENAI_API_KEY=your-api-key-here
```

### 5. Deploy
```bash
git add .
git commit -m "Deploy fraud detection service"
git push heroku main
```

### 6. Open Your App
```bash
heroku open
```

## 🐳 Docker Deployment

### 1. Build Docker Image
```bash
docker build -t fraud-detection .
```

### 2. Run Container
```bash
docker run -p 8000:8000 fraud-detection
```

### 3. With Environment Variables
```bash
docker run -p 8000:8000 -e OPENAI_API_KEY=your-key fraud-detection
```

## ☁️ Cloud Deployment (AWS/GCP/Azure)

### 1. Create Virtual Machine
- Choose Ubuntu 20.04 or similar
- Open port 8000 in security groups

### 2. Connect and Setup
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python
sudo apt install python3 python3-pip -y

# Clone repository
git clone https://github.com/yourusername/fraud-service-python.git
cd fraud-service-python

# Install dependencies
pip3 install -r requirements.txt

# Set environment variable (optional)
export OPENAI_API_KEY=your-api-key-here

# Run application
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 3. Use PM2 for Production (Optional)
```bash
# Install PM2
npm install -g pm2

# Start with PM2
pm2 start "uvicorn app.main:app --host 0.0.0.0 --port 8000" --name fraud-detection

# Save PM2 configuration
pm2 save
pm2 startup
```

## 🔧 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for AI analysis | No |
| `PORT` | Port to run the application | No (default: 8000) |

## 📊 Health Check

After deployment, check if your service is running:
```bash
curl https://your-app-url.herokuapp.com/health
```

## 🛠️ Troubleshooting

### Port Already in Use
```bash
# Find process using port 8000
lsof -i :8000

# Kill process
kill -9 <PID>
```

### Permission Denied
```bash
# Make start script executable
chmod +x start.py
```

### Dependencies Issues
```bash
# Update pip
pip install --upgrade pip

# Install with verbose output
pip install -r requirements.txt -v
```

## 📝 Production Tips

1. **Use HTTPS**: Always use HTTPS in production
2. **Environment Variables**: Never commit API keys to git
3. **Monitoring**: Set up health checks and monitoring
4. **Scaling**: Use load balancers for high traffic
5. **Logging**: Implement proper logging for debugging

---

**Your fraud detection service is now ready for production!** 🎉
