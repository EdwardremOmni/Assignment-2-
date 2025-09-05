# Premier League Records - README

## Installation

### 1. Clone the Repository

```bash
git clone <repo-url>
cd premier_league_records
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Database Setup

### 1. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Create Superuser (Optional for Admin Access)

```bash
python manage.py createsuperuser
```

## Running the Project

### Start Development Server

```bash
python manage.py runserver
```

### Access the Application

Open your browser and navigate to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## API Documentation

### Swagger UI

Interactive API documentation is available at:
[http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

It provides full details of all endpoints, request/response formats, and data models.
