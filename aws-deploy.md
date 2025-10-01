# 🚀 AWS Deployment Guide

## Deploy Your Fraud Detection Service to AWS

### Option 1: AWS App Runner (Recommended)

1. **Go to AWS Console**
   - Visit [console.aws.amazon.com](https://console.aws.amazon.com)
   - Sign in to your AWS account

2. **Navigate to App Runner**
   - Search for "App Runner" in the services
   - Click "Create service"

3. **Configure Service**
   - **Service name**: `fraud-detection-service`
   - **Source**: GitHub
   - **Repository**: `nravi7/Fraud-Detection-Service-with-AI-powered-analysis-and-web-interface`
   - **Branch**: `main`

4. **Build Settings**
   - **Configuration file**: Use `apprunner.yaml`
   - **Port**: `8000`

5. **Deploy**
   - Click "Create & deploy"
   - Wait for deployment (5-10 minutes)
   - Get your live URL!

### Option 2: AWS Elastic Beanstalk

1. **Go to Elastic Beanstalk**
   - Search for "Elastic Beanstalk" in AWS Console
   - Click "Create application"

2. **Configure Application**
   - **Application name**: `fraud-detection`
   - **Platform**: Python 3.9
   - **Platform branch**: Python 3.9 running on 64bit Amazon Linux 2

3. **Upload Code**
   - Create application version
   - Upload your code as ZIP file
   - Deploy

### Option 3: AWS Lambda + API Gateway

1. **Create Lambda Function**
   - Go to Lambda service
   - Create function with Python 3.9 runtime
   - Upload your code

2. **Create API Gateway**
   - Create REST API
   - Connect to Lambda function
   - Deploy API

### Option 4: AWS ECS (Container)

1. **Create ECS Cluster**
   - Go to ECS service
   - Create cluster

2. **Create Task Definition**
   - Use your Dockerfile
   - Configure container settings

3. **Create Service**
   - Deploy to ECS cluster
   - Configure load balancer

## 🎯 Recommended: AWS App Runner

**Why App Runner?**
- ✅ **Easiest deployment**
- ✅ **Automatic scaling**
- ✅ **GitHub integration**
- ✅ **Free tier available**
- ✅ **No server management**

## 📊 AWS Free Tier Limits

- **App Runner**: 2,000 build minutes/month
- **Data transfer**: 1 GB/month
- **Compute**: 750 hours/month

## 🔧 Environment Variables

Set these in AWS App Runner:
- `OPENAI_API_KEY`: Your OpenAI API key (optional)
- `PORT`: 8000

## 🌐 Your Live URL

After deployment, you'll get a URL like:
`https://your-app-name.region.awsapprunner.com`

## 💡 Tips

1. **Use App Runner** for easiest deployment
2. **Set up monitoring** with CloudWatch
3. **Configure custom domain** if needed
4. **Set up CI/CD** with GitHub Actions

---

**Your fraud detection service will be live on AWS!** 🛡️☁️
