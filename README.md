# Simple Chatbot

A simple Flask-based chatbot application with a clean web interface.

## Local Development

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

## Deployment Options

### Option 1: PythonAnywhere (Free)
1. Sign up at [PythonAnywhere](https://www.pythonanywhere.com)
2. Create a new web app with Flask
3. Upload your files or clone from GitHub
4. Set up your virtual environment
5. Install requirements
6. Configure WSGI file
7. Reload the web app

### Option 2: Heroku
1. Install Heroku CLI
2. Login to Heroku:
```bash
heroku login
```
3. Create a new Heroku app:
```bash
heroku create your-app-name
```
4. Deploy:
```bash
git push heroku main
```

### Option 3: Railway.app
1. Sign up at [Railway](https://railway.app)
2. Create a new project
3. Connect your GitHub repository
4. Deploy automatically

## Project Structure
```
chatbox/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Procfile           # For Heroku deployment
└── templates/
    └── index.html     # Frontend template
```
