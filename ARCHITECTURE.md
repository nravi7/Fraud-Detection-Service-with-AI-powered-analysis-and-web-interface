# 🏗️ Fraud Detection Service Architecture

## System Architecture Overview

```mermaid
graph TB
    subgraph "Frontend Layer"
        A[Web Interface<br/>HTML/CSS/JavaScript] --> B[User Input<br/>Transaction Text]
    end
    
    subgraph "API Gateway"
        C[FastAPI Server<br/>Port 8000] --> D[CORS Middleware]
        D --> E[Authentication<br/>JWT Tokens]
    end
    
    subgraph "Core Services"
        F[OpenAI Provider<br/>GPT-4 Analysis] --> G[AI Fraud Detection]
        H[Rule-Based Provider<br/>Pattern Matching] --> I[Heuristic Analysis]
    end
    
    subgraph "Data Processing"
        J[Transaction Parser] --> K[Risk Scoring<br/>0.0 - 1.0]
        K --> L[Fraud Classification<br/>FRAUD/LEGIT]
    end
    
    subgraph "Response Layer"
        M[Result Formatter] --> N[JSON Response]
        N --> O[Status Indicators<br/>Ready/Processing/Completed]
    end
    
    subgraph "Deployment Options"
        P[Local Development<br/>localhost:8000] --> Q[GitHub Pages<br/>Static Landing]
        R[Railway<br/>Free Deployment] --> S[Render<br/>Free Deployment]
        T[AWS App Runner<br/>Cloud Deployment] --> U[Docker<br/>Containerized]
    end
    
    B --> C
    C --> F
    C --> H
    G --> J
    I --> J
    L --> M
    O --> A
    
    style A fill:#e1f5fe
    style C fill:#f3e5f5
    style F fill:#fff3e0
    style H fill:#e8f5e8
    style P fill:#fce4ec
    style R fill:#f1f8e9
    style T fill:#e3f2fd
```

## 🎯 Component Details

### **Frontend Layer**
- **Web Interface**: Modern, responsive HTML/CSS/JavaScript
- **User Experience**: Real-time status indicators and example transactions
- **Design**: Professional gradient design with Font Awesome icons

### **API Gateway**
- **FastAPI Server**: High-performance Python web framework
- **CORS Middleware**: Cross-origin resource sharing for web access
- **Authentication**: JWT-based security (optional for demo)

### **Core Services**
- **OpenAI Provider**: AI-powered fraud detection using GPT-4
- **Rule-Based Provider**: Pattern matching for fraud indicators
- **Fallback System**: Works without API keys using demo mode

### **Data Processing**
- **Transaction Parser**: Analyzes transaction text for fraud patterns
- **Risk Scoring**: Generates confidence scores from 0.0 to 1.0
- **Classification**: Determines FRAUD or LEGIT status

### **Response Layer**
- **Result Formatter**: Structures response data
- **Status System**: Real-time processing indicators
- **Error Handling**: Graceful error management

## 🚀 Deployment Architecture

```mermaid
graph LR
    subgraph "Development"
        A[Local Machine<br/>Python + FastAPI] --> B[localhost:8000]
    end
    
    subgraph "Source Control"
        C[GitHub Repository<br/>nravi7/Fraud-Detection-Service] --> D[Version Control]
    end
    
    subgraph "Static Hosting"
        E[GitHub Pages<br/>Landing Page] --> F[nravi7.github.io]
    end
    
    subgraph "Cloud Deployment"
        G[Railway<br/>Free Tier] --> H[railway.app domain]
        I[Render<br/>Free Tier] --> J[render.com domain]
        K[AWS App Runner<br/>Free Tier] --> L[awsapprunner.com domain]
    end
    
    subgraph "Container Deployment"
        M[Docker<br/>Containerized] --> N[Any Platform]
    end
    
    A --> C
    C --> E
    C --> G
    C --> I
    C --> K
    C --> M
    
    style A fill:#e8f5e8
    style C fill:#e3f2fd
    style E fill:#fff3e0
    style G fill:#f1f8e9
    style I fill:#fce4ec
    style K fill:#e1f5fe
    style M fill:#f3e5f5
```

## 🔧 Technology Stack

### **Backend**
- **FastAPI**: Modern Python web framework
- **Uvicorn**: ASGI server for production
- **Pydantic**: Data validation and serialization
- **OpenAI API**: AI-powered fraud detection
- **Python 3.9+**: Runtime environment

### **Frontend**
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with gradients
- **JavaScript ES6+**: Interactive functionality
- **Font Awesome**: Professional icons
- **Responsive Design**: Mobile-friendly interface

### **Deployment**
- **GitHub**: Source code repository
- **GitHub Pages**: Static site hosting
- **Railway**: Free cloud deployment
- **Render**: Alternative cloud platform
- **AWS App Runner**: Enterprise cloud deployment
- **Docker**: Containerization

## 📊 Data Flow

```mermaid
sequenceDiagram
    participant U as User
    participant W as Web Interface
    participant F as FastAPI
    participant O as OpenAI
    participant R as Rule-Based
    participant D as Database
    
    U->>W: Enter transaction text
    W->>F: POST /v1/score
    F->>O: Analyze with AI
    O-->>F: AI response
    F->>R: Fallback analysis
    R-->>F: Rule-based result
    F->>D: Log transaction
    F-->>W: JSON response
    W->>U: Display results
```

## 🛡️ Security Features

- **Input Validation**: Pydantic models for data validation
- **CORS Protection**: Cross-origin request handling
- **Error Handling**: Graceful error management
- **Rate Limiting**: Built-in FastAPI protection
- **Environment Variables**: Secure API key management

## 📈 Performance Features

- **Async Processing**: FastAPI async/await support
- **Response Caching**: Efficient data handling
- **Status Indicators**: Real-time user feedback
- **Error Recovery**: Fallback mechanisms
- **Scalable Architecture**: Cloud-ready design

## 🎯 Key Benefits

- ✅ **AI-Powered**: Advanced fraud detection
- ✅ **Rule-Based Fallback**: Works without API keys
- ✅ **Multiple Deployment**: Various hosting options
- ✅ **Professional UI**: Modern, responsive design
- ✅ **Easy Setup**: Simple installation process
- ✅ **Portfolio Ready**: Perfect for showcasing skills

---

**Built with ❤️ by Ravi N using modern web technologies**
