# NAS Web Interface Prototype

A simple web application prototype for a Network Attached Storage (NAS) interface using FastAPI and Jinja2 templates.

## Features

- User authentication (login/signup)
- Dashboard with storage statistics
- File upload functionality
- File download functionality
- Clean, responsive UI

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python -m app.main
```

4. Open your browser and navigate to:
```
http://localhost:8000
```

## Default Users

The application comes with two pre-configured users:

- Username: admin, Password: admin123
- Username: user, Password: user123

## Project Structure

```
app/
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── upload.html
│   └── download.html
├── routers/
│   ├── __init__.py
│   ├── auth.py
│   ├── dashboard.py
│   └── files.py
├── main.py
└── models.py
```

## Notes

- This is a prototype application. In a production environment, you would implement:
  - Real database integration (e.g., PostgreSQL, MySQL, MongoDB)
  - Proper authentication with password hashing and secure sessions
  - Actual file storage and retrieval mechanisms
  - Error handling and logging
  - Input validation and security measures

## Adding Real Functionality

To replace the mocked functionality with real implementations:

1. Create a database connection in `app/database.py`
2. Replace mock models with ORM models (e.g., SQLAlchemy)
3. Implement actual file storage logic in the routers
4. Add proper user authentication and session management
5. Implement data validation 