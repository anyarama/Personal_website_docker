# Personal Website Docker Repository

**Author:** Aneesh Yaramati  
**MSIS Candidate** - Kelley School of Business  
**Repository:** Personal Website Projects with Docker Integration

---

## 📚 Repository Overview

This repository contains Flask-based personal portfolio website projects developed as part of the Applied Internet and Database Development (AiDD) course. Each assignment demonstrates progressive web development skills, database integration, and Docker containerization.

### 🎯 Purpose

- Showcase professional portfolio and projects
- Demonstrate Flask web development best practices
- Implement database-driven applications with SQLite
- Containerize applications using Docker
- Practice CI/CD with GitHub Actions

---

## 📁 Repository Structure

```
Personal_website_docker/
├── README.md                    # This file - Repository overview
├── .github/
│   └── workflows/
│       └── python-app.yml      # CI/CD pipeline configuration
│
├── AiDD_Assignment05/           # Assignment 5 - Database Integration
│   ├── app.py                   # Flask application
│   ├── DAL.py                   # Data Access Layer
│   ├── Dockerfile              # Docker configuration
│   ├── README.md               # Assignment-specific documentation
│   ├── requirements.txt        # Python dependencies
│   ├── static/                 # CSS, JS, Images
│   └── templates/              # HTML templates
│
└── AiDD_Assignment07/           # Assignment 7 - Advanced Features
    ├── app.py                   # Enhanced Flask application
    ├── DAL.py                   # Data Access Layer
    ├── Dockerfile              # Docker configuration
    ├── README.md               # Assignment-specific documentation
    ├── requirements.txt        # Python dependencies
    ├── static/                 # CSS, JS, Images
    └── templates/              # HTML templates
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** - Programming language
- **Docker Desktop** - Container platform
- **Git** - Version control
- **pip** - Python package manager

### Clone the Repository

```bash
git clone https://github.com/anyarama/Personal_website_docker.git
cd Personal_website_docker
```

---

## 🐳 Docker Deployment

### Option 1: Run Assignment 5

```bash
cd AiDD_Assignment05
docker build -t personal-website-05 .
docker run -d -p 8001:8001 --name website-05 personal-website-05
```

Access at: **http://localhost:8001**

### Option 2: Run Assignment 7

```bash
cd AiDD_Assignment07
docker build -t personal-website-07 .
docker run -d -p 8002:8001 --name website-07 personal-website-07
```

Access at: **http://localhost:8002**

### Docker Management Commands

```bash
# View running containers
docker ps

# View all containers (including stopped)
docker ps -a

# View container logs
docker logs <container-name>

# Stop a container
docker stop <container-name>

# Start a stopped container
docker start <container-name>

# Remove a container
docker rm -f <container-name>

# Remove an image
docker rmi <image-name>
```

---

## 📂 Assignments

### Assignment 5 - Database Integration

**Location:** `AiDD_Assignment05/`

**Features:**
- Flask web application with routing
- SQLite database integration
- Data Access Layer (DAL) pattern
- CRUD operations for projects
- Responsive glassmorphic UI design
- Docker containerization
- GitHub Actions CI/CD

**[View Assignment 5 README](./AiDD_Assignment05/README.md)**

**Run Locally:**
```bash
cd AiDD_Assignment05
pip install -r requirements.txt
python app.py
```

---

### Assignment 7 - Advanced Features

**Location:** `AiDD_Assignment07/`

**Features:**
- Enhanced Flask application
- Advanced database operations
- Improved user interface
- Additional functionality
- Docker support
- Comprehensive testing

**[View Assignment 7 README](./AiDD_Assignment07/README.md)**

**Run Locally:**
```bash
cd AiDD_Assignment07
pip install -r requirements.txt
python app.py
```

---

## 🛠️ Development Setup

### Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies for specific assignment
cd AiDD_Assignment05  # or AiDD_Assignment07
pip install -r requirements.txt

# Run the application
python app.py
```

### Without Docker

Each assignment can be run directly with Python:

1. Navigate to the assignment directory
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Access in browser: `http://localhost:8001`

---

## 🧪 Testing

### Run Tests for Assignment 5

```bash
cd AiDD_Assignment05
pytest -v
```

### Run Tests for Assignment 7

```bash
cd AiDD_Assignment07
pytest -v
```

### Run Tests with Coverage

```bash
pytest -v --cov=. --cov-report=term-missing
```

---

## 🔄 CI/CD Pipeline

### GitHub Actions

This repository uses GitHub Actions for continuous integration and deployment.

**Workflow includes:**
- ✅ Python 3.10 setup
- ✅ Dependency installation
- ✅ Code linting with flake8
- ✅ Unit testing with pytest
- ✅ Code coverage reporting
- ✅ Automated on push/pull request

**Configuration:** `.github/workflows/python-app.yml`

View workflow runs on GitHub Actions tab.

---

## 🎨 Tech Stack

### Backend
- **Flask 3.0.0** - Python web framework
- **SQLite3** - Lightweight database
- **Python 3.8+** - Programming language

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling (Glassmorphic design)
- **JavaScript** - Interactivity
- **Jinja2** - Template engine

### DevOps
- **Docker** - Containerization
- **GitHub Actions** - CI/CD
- **pytest** - Testing framework
- **flake8** - Code linting

---

## 📋 Features Across Assignments

### Common Features
- ✅ Flask routing and URL handling
- ✅ Jinja2 template rendering
- ✅ Static file serving (CSS, JS, images)
- ✅ Responsive design
- ✅ Error handling (404, 500)
- ✅ Docker containerization
- ✅ CI/CD integration

### Database Features
- ✅ SQLite database integration
- ✅ Data Access Layer (DAL)
- ✅ CRUD operations
- ✅ Parameterized queries (SQL injection prevention)
- ✅ Transaction handling

### UI/UX Features
- ✅ Professional glassmorphic theme
- ✅ Mobile-first responsive design
- ✅ WCAG accessibility compliance
- ✅ Modern gradient aesthetics
- ✅ Smooth animations and transitions

---

## 📚 Documentation

Each assignment has its own detailed README:

- **[Assignment 5 Documentation](./AiDD_Assignment05/README.md)** - Comprehensive setup and features
- **[Assignment 7 Documentation](./AiDD_Assignment07/README.md)** - Advanced features and improvements

Additional documentation files:
- `SETUP_INSTRUCTIONS.md` - Detailed setup guides
- `TESTING.md` - Testing documentation
- `GITHUB_CI_SETUP.md` - CI/CD configuration guide

---

## 🔐 Environment Variables

### Flask Configuration

```bash
# Optional: Set environment variables
export FLASK_APP=app.py
export FLASK_ENV=development
export SECRET_KEY=your-secret-key-here
```

### Docker Environment

Environment variables are configured in the Dockerfile:
- `FLASK_APP=app.py`
- `PYTHONUNBUFFERED=1`

---

## 🚨 Troubleshooting

### Docker Daemon Not Running

**Error:** `Cannot connect to the Docker daemon`

**Solution:**
1. Open Docker Desktop application
2. Wait for Docker to fully start
3. Verify with: `docker ps`

### Port Already in Use

**Error:** `port is already allocated`

**Solution:**
```bash
# Find and stop container using the port
docker ps
docker stop <container-name>

# Or use a different port
docker run -d -p 8080:8001 --name my-website personal-website
```

### Module Not Found Error

**Error:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
```bash
# Install dependencies
pip install -r requirements.txt

# Or in Docker, rebuild the image
docker build -t personal-website .
```

---

## 🤝 Contributing

This is a personal academic project, but suggestions and feedback are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📄 License

This project is created for educational purposes as part of the MSIS program at Kelley School of Business.

---

## 👤 Author

**Aneesh Yaramati**  
MSIS Candidate - Kelley School of Business  
Data Engineering & Analytics Professional

### Connect
- **GitHub:** [@anyarama](https://github.com/anyarama)
- **Repository:** [Personal_website_docker](https://github.com/anyarama/Personal_website_docker)

---

## 📅 Project Timeline

- **Assignment 5** - Database Integration & Docker Setup
- **Assignment 7** - Advanced Features & Enhancements
- **Ongoing** - Continuous improvements and updates

---

## ⭐ Acknowledgments

- Indiana University - Kelley School of Business
- Applied Internet and Database Development (AiDD) Course
- Flask Documentation & Community
- Docker Documentation

---

**Built with Flask, Docker, and modern web development best practices** 🚀
