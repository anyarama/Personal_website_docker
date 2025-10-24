# Personal Portfolio Website - Flask Application

**Author:** Aneesh Yaramati  
**Course:** AiDD Assignment 05  
**Description:** Data Engineering & Analytics Professional Portfolio built with Flask

## 📁 Project Structure

```
AiDD_Assignment05/
├── app.py                    # Main Flask application with all routes
├── DAL.py                    # Data Access Layer for database operations
├── projects.db               # SQLite database (auto-created on first run)
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── SETUP_INSTRUCTIONS.md     # Detailed setup guide
├── static/                   # Static files (CSS, JS, Images)
│   ├── css/
│   │   └── styles.css       # Main stylesheet with glassmorphic theme
│   ├── js/
│   │   └── script.js        # JavaScript for navigation
│   └── images/              # Image assets
│       ├── favicon.svg
│       ├── headshot.jpg
│       ├── project-live-in-labs.svg
│       ├── project-mdm.svg
│       ├── project-pothole.svg
│       └── project-sap.svg
└── templates/               # HTML templates (Jinja2)
    ├── index.html           # Home page
    ├── about.html           # About page
    ├── resume.html          # Resume page
    ├── projects.html        # Projects page with database table
    ├── add_project.html     # Form to add new projects
    ├── contact.html         # Contact form
    └── thankyou.html        # Thank you page
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Docker (for containerized deployment)

---

## 🐳 Docker Deployment (Recommended)

### Quick Start with Docker

The application is containerized and ready to run with Docker.

#### Option 1: Use Existing Running Container

A Docker container is currently active and running:

```
Container ID: 098237f0f1a2
Container Name: my-website
Image: personal-website
Status: Up and running
Port Mapping: 0.0.0.0:8001->8001/tcp
Access URL: http://localhost:8001
```

**Container Management Commands:**
```bash
# View container status
docker ps

# View container logs
docker logs my-website
# or
docker logs 098237f0f1a2

# Access container shell
docker exec -it my-website /bin/bash

# Stop container
docker stop my-website

# Start container (if stopped)
docker start my-website

# Restart container
docker restart my-website

# Remove container
docker rm -f my-website
```

#### Option 2: Build and Run Fresh Docker Container

**Step 1: Build Docker Image**
```bash
cd AiDD_Assignment05
docker build -t personal-website .
```

**Step 2: Run Docker Container**
```bash
docker run -d -p 8001:8001 --name my-website personal-website
```

**Step 3: Verify Container is Running**
```bash
docker ps
```

**Step 4: Access the Application**
Open your browser and navigate to: http://localhost:8001

### Docker Configuration

The `Dockerfile` includes:
- Python 3.11 slim base image
- Automatic dependency installation from requirements.txt
- Port 8001 exposure
- Flask application with all templates and static files
- Environment variables configured for Flask

### Docker Best Practices

**Persistent Database with Volume (Optional):**
```bash
docker run -d -p 8001:8001 \
  -v $(pwd)/projects.db:/app/projects.db \
  --name my-website personal-website
```

**View Real-time Logs:**
```bash
docker logs -f my-website
```

**Rebuild After Code Changes:**
```bash
docker stop my-website
docker rm my-website
docker build -t personal-website .
docker run -d -p 8001:8001 --name my-website personal-website
```

---

## 💻 Local Development (Without Docker)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install Flask directly:
```bash
pip install Flask==3.0.0
```

### Step 2: Initialize Database

The database will be automatically created when you first run the application. It creates a `projects.db` file in the root directory with the following structure:

**Database Schema:**
```sql
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    image_filename TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Step 3: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:8001` (configured to avoid port conflicts on macOS)

**💡 Recommended: Use Virtual Environment**  
See `SETUP_INSTRUCTIONS.md` for complete setup with virtual environment (best practice).

### Step 4: Access the Website

Open your web browser and navigate to:
- **Home:** http://localhost:8001/
- **About:** http://localhost:8001/about
- **Resume:** http://localhost:8001/resume
- **Projects:** http://localhost:8001/projects (Database-driven)
- **Add Project:** http://localhost:8001/add_project (Add new projects)
- **Contact:** http://localhost:8001/contact

**📖 For detailed setup with virtual environment, see `SETUP_INSTRUCTIONS.md`**

## 📋 Features

### Pages
1. **Home (/)** - Hero section with introduction and feature highlights
2. **About (/about)** - Personal story and background
3. **Resume (/resume)** - Professional experience and education
4. **Projects (/projects)** - Database-driven projects showcase with HTML table
5. **Add Project (/add_project)** - Form to add new projects to database
6. **Delete Project (/delete_project/<id>)** - Remove projects from database
7. **Contact (/contact)** - Contact form with POST handling
8. **Thank You (/thankyou)** - Confirmation page after form submission

### Technical Features
- ✅ **Flask routing** with proper URL generation using `url_for()`
- ✅ **SQLite database integration** with Data Access Layer (DAL)
- ✅ **CRUD operations** - Create, Read, and Delete projects
- ✅ **Database-driven content** - Projects pulled from SQLite database
- ✅ **Data Access Layer (DAL.py)** - Separation of database logic
- ✅ **Form handling** - Contact form and project submission
- ✅ **Image management** - Projects linked to images in static/images/
- ✅ **Static file serving** (CSS, JavaScript, Images)
- ✅ **Template inheritance** with Jinja2
- ✅ **Dynamic year injection** in footer
- ✅ **Error handling** (404, 500)
- ✅ **Responsive design** with glassmorphic UI
- ✅ **Accessibility features** - WCAG compliant
- ✅ **Professional dark theme** - Premium glassmorphism aesthetic

## 🏗️ Flask Best Practices Implemented

1. **Project Structure**
   - Proper separation of static files and templates
   - Organized folder structure following Flask conventions
   - **Data Access Layer (DAL)** - Separation of database logic

2. **URL Routing**
   - All links use Flask's `url_for()` function
   - Clean, RESTful route names
   - Proper HTTP methods (GET, POST)

3. **Database Management**
   - **SQLite database** for persistent storage
   - **Parameterized queries** to prevent SQL injection
   - **Row factory** for dictionary-style data access
   - **Transaction handling** with proper commit/close

4. **Template Management**
   - Jinja2 templating with proper escaping
   - Dynamic content rendering from database
   - Context processors for global variables
   - Template loops for database records

5. **Static Files**
   - Organized in css/, js/, and images/ subdirectories
   - Served via Flask's static file handling
   - Proper URL generation with `url_for('static', filename=...)`
   - Images referenced from database records

6. **Configuration**
   - Secret key configuration
   - Debug mode for development
   - Host and port configuration
   - Database initialization on startup

7. **Error Handling**
   - Custom 404 error handler
   - Custom 500 error handler
   - Graceful error recovery
   - Form validation

## 🔧 Development

### Running in Debug Mode
The app.py file is configured to run in debug mode by default for development:
```python
app.run(debug=True, host='0.0.0.0', port=8001)
```

### For Production
For production deployment, use a WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn app:app
```

## 💾 Database Features (Assignment 05)

### Data Access Layer (DAL.py)
The `DAL.py` file provides a clean interface for all database operations:

**Available Functions:**
- `init_database()` - Creates the projects table if it doesn't exist
- `get_all_projects()` - Retrieves all projects from database
- `get_project_by_id(project_id)` - Gets a single project
- `insert_project(title, description, image_filename)` - Adds new project
- `delete_project(project_id)` - Removes a project
- `update_project(project_id, ...)` - Updates existing project

### Projects Management Workflow

1. **View Projects** - Navigate to `/projects` to see all projects in an HTML table
2. **Add Project** - Click "Add New Project" button or visit `/add_project`
3. **Fill Form** - Enter title, description, and image filename
4. **Upload Image** - Manually place image in `static/images/` folder
5. **Submit** - Project appears immediately in the table
6. **Delete** - Click delete button with confirmation dialog

### Database Table Structure

| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| title | TEXT | NOT NULL |
| description | TEXT | NOT NULL |
| image_filename | TEXT | NOT NULL |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

## 📝 Notes

- The contact form currently redirects to a thank you page without sending emails
- **Image Upload:** Currently requires manual upload to `static/images/` folder
- **Database:** SQLite database file (`projects.db`) is created automatically
- For production use, implement:
  - File upload functionality for images
  - Email sending functionality
  - Enhanced form validation
  - CSRF protection
  - Environment-based configuration
  - Proper secret key management
  - Database migrations tool (e.g., Flask-Migrate)

## 🎨 Design

- **Theme:** Premium glassmorphic dark theme
- **Colors:** Professional blue/purple gradient accent
- **Typography:** Inter font family
- **Responsive:** Mobile-first responsive design
- **Accessibility:** WCAG compliant with proper ARIA labels

## 📦 Dependencies

- **Flask 3.0.0** - Web framework
- **Werkzeug 3.0.1** - WSGI utilities (Flask dependency)
- **SQLite3** - Built-in Python database (no installation required)

**Note:** SQLite3 is included with Python standard library, no additional installation needed.

## 👤 Author

**Aneesh Yaramati**  
MSIS Candidate at Kelley School of Business  
Data Engineering & Analytics Professional

---

Built with Flask and modern web development best practices.
