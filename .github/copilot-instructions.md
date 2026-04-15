---
description: "GitHub Copilot instructions for OctoFit Tracker development"
---

# OctoFit Tracker - GitHub Copilot Instructions

## 📱 Project Overview

**OctoFit Tracker** is a fitness tracking application for Mergington High School that enables students to log activities, earn achievement badges, and compete in friendly fitness challenges. The app is built with a modern full-stack architecture:

- **Frontend**: React.js with Bootstrap
- **Backend**: Python Django REST API
- **Database**: MongoDB
- **Environment**: GitHub Codespaces

### Core Features
- User authentication and profiles
- Activity logging and tracking (running, walking, strength training)
- Team creation and management
- Competitive leaderboard
- Personalized workout suggestions

---

## 🎯 Domain-Specific Instructions

Follow these instructions based on the area you're working on:

| Area | File | Scope |
|------|------|-------|
| **Project Setup** | [octofit_tracker_setup_project.instructions.md](.github/instructions/octofit_tracker_setup_project.instructions.md) | Entire project setup, virtual environments, dependencies, MongoDB |
| **Django Backend** | [octofit_tracker_django_backend.instructions.md](.github/instructions/octofit_tracker_django_backend.instructions.md) | `octofit-tracker/backend/**` - REST API, models, serializers, settings |
| **React Frontend** | [octofit_tracker_react_frontend.instructions.md](.github/instructions/octofit_tracker_react_frontend.instructions.md) | `octofit-tracker/frontend/**` - UI components, routing, styling |

---

## 🌐 Forwarded Ports

Always use these ports and visibility settings:

| Port | Service | Visibility |
|------|---------|------------|
| **8000** | Django Backend | Public |
| **3000** | React Frontend | Public |
| **27017** | MongoDB | Private |

**Do not propose any other ports.** Update Codespace port forwarding settings as needed.

---

## 🔧 Development Workflow

### 1. Initial Setup

```bash
# Create project structure
mkdir -p octofit-tracker/backend octofit-tracker/frontend

# Set up Python environment
python3 -m venv octofit-tracker/backend/venv
source octofit-tracker/backend/venv/bin/activate

# Install backend dependencies
pip install -r octofit-tracker/backend/requirements.txt

# Set up frontend
npx create-react-app octofit-tracker/frontend --template cra-template --use-npm
npm install bootstrap --prefix octofit-tracker/frontend
npm install react-router-dom --prefix octofit-tracker/frontend
```

### 2. Running the Application

**Backend** (from project root):
```bash
source octofit-tracker/backend/venv/bin/activate
python octofit-tracker/backend/manage.py runserver 8000
```

**Frontend** (from project root):
```bash
npm start --prefix octofit-tracker/frontend
```

**MongoDB**: Use `ps aux | grep mongod` to verify service is running.

### 3. Code Organization

```
octofit-tracker/
├── backend/
│   ├── venv/
│   ├── octofit_tracker/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── __init__.py
│   ├── requirements.txt
│   └── manage.py
└── frontend/
    ├── public/
    ├── src/
    │   ├── components/
    │   ├── pages/
    │   ├── App.js
    │   └── index.js
    ├── package.json
    └── .gitignore
```

---

## ⚙️ Agent Mode Conventions

### Directory Navigation
- **Never change directories** when running commands in agent mode
- Always use full paths relative to the workspace root:
  ```bash
  python octofit-tracker/backend/manage.py migrate
  npm install --prefix octofit-tracker/frontend
  ```

### Testing & Validation
- Use `curl` to test Django REST API endpoints
- Always validate MongoDB connection before running backend
- Test frontend component routing with React Router

### Environment Awareness
- Detect Codespace environment: `os.environ.get('CODESPACE_NAME')`
- Use dynamic URLs for API endpoints based on environment
- Codespace URL format: `https://{CODESPACE_NAME}-{PORT}.app.github.dev`

---

## 🚀 Common Commands

### Backend Management
```bash
# Run migrations
python octofit-tracker/backend/manage.py migrate

# Create superuser
python octofit-tracker/backend/manage.py createsuperuser

# Collect static files
python octofit-tracker/backend/manage.py collectstatic

# Run development server
python octofit-tracker/backend/manage.py runserver 8000
```

### Frontend Management
```bash
# Install dependencies
npm install --prefix octofit-tracker/frontend

# Start development server
npm start --prefix octofit-tracker/frontend

# Build for production
npm run build --prefix octofit-tracker/frontend
```

### Database Management
```bash
# Check MongoDB status
ps aux | grep mongod

# Open MongoDB shell
mongosh

# Use Django ORM for data creation (never use direct MongoDB scripts)
python octofit-tracker/backend/manage.py shell
```

---

## 📋 Backend Guidelines

### Django Settings (`settings.py`)
Always include:
```python
import os
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
if os.environ.get('CODESPACE_NAME'):
    ALLOWED_HOSTS.append(f"{os.environ.get('CODESPACE_NAME')}-8000.app.github.dev")
```

### Serializers
- Convert ObjectId fields to strings in serializers
- Use DRF serializers for API responses

### URLs (`urls.py`)
- Use environment-aware base URLs:
  ```python
  import os
  codespace_name = os.environ.get('CODESPACE_NAME')
  if codespace_name:
      base_url = f"https://{codespace_name}-8000.app.github.dev"
  else:
      base_url = "http://localhost:8000"
  ```

---

## 🎨 Frontend Guidelines

### Component Structure
- Organize components in `src/components/`
- Use Bootstrap classes for styling
- Use React Router for page navigation

### Images
- App logo/images: `docs/octofitapp-small.png`
- Always use relative paths from public folder

### Bootstrap Setup
- Import Bootstrap CSS at the top of `src/index.js`:
  ```javascript
  import 'bootstrap/dist/css/bootstrap.min.css';
  ```

---

## 🔄 MongoDB & Django ORM

### Best Practices
- **Always use Django's ORM** for database operations
- Never execute direct MongoDB scripts for data creation
- Use Django shell for interactive data creation:
  ```bash
  python octofit-tracker/backend/manage.py shell
  ```

### Verification
- Check MongoDB is running: `ps aux | grep mongond`
- Use official tools: `mongosh` (client), `mongodb-org` (package)

---

## 📚 Documentation

- **Project Story**: [docs/octofit_story.md](docs/octofit_story.md)
- **GitHub Copilot Chat Docs**: [Getting started with GitHub Copilot Chat](https://docs.github.com/en/copilot/how-tos/use-chat/get-started-with-chat?tool=vscode)
- **Prompt Engineering**: [Prompt engineering for GitHub Copilot Chat](https://docs.github.com/en/copilot/concepts/prompt-engineering)

---

## ✅ Quality Checklist

Before committing changes:

- [ ] Code follows project structure guidelines
- [ ] Backend uses Django ORM, not direct MongoDB
- [ ] Environment variables properly handled (CODESPACE_NAME)
- [ ] API endpoints tested with curl
- [ ] Frontend components properly organized
- [ ] No hardcoded URLs (use environment-aware patterns)
- [ ] Virtual environment activated for Python work
- [ ] Port forwarding settings verified (8000, 3000, 27017)

---

## 🆘 Common Issues

| Issue | Solution |
|-------|----------|
| Module not found | Verify venv is activated: `source octofit-tracker/backend/venv/bin/activate` |
| Port already in use | Check running processes: `lsof -i :8000` or `lsof -i :3000` |
| MongoDB connection failed | Verify running: `ps aux \| grep mongond` |
| CORS errors | Check Django `CORS_ALLOWED_ORIGINS` in settings.py |
| React app not loading | Verify frontend server running on port 3000 |

---

## 🎓 Next Steps

1. **Start with Setup**: Review [octofit_tracker_setup_project.instructions.md](.github/instructions/octofit_tracker_setup_project.instructions.md)
2. **Build Backend**: Follow [octofit_tracker_django_backend.instructions.md](.github/instructions/octofit_tracker_django_backend.instructions.md)
3. **Create Frontend**: Follow [octofit_tracker_react_frontend.instructions.md](.github/instructions/octofit_tracker_react_frontend.instructions.md)

---

**Last Updated**: April 14, 2026  
**Project**: OctoFit Tracker for Mergington High School
