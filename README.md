# AniConnect Website Setup Guide

## About AniConnect

AniConnect is a Django-based anime community platform where users can browse anime entries, search titles, write reviews, and participate in forum discussions. It also includes user profiles, watch-status tracking, and moderation/reporting features for community content.

This guide helps you verify a clean setup of the project from scratch.

## 1) Clone the repository into the folder you want

```bash
git clone https://github.com/ankitgawade/AniConnect-Website.git
cd AniConnect-Website
```

## 2) Create and activate a virtual environment (Windows – Command Prompt)

### Command Prompt

```
python -m venv venv
venv\Scripts\Activate
```

## 3) Install packages

```bash
pip install -r requirements.txt
```

## 4) Create database (MySQL)

Open MySQL and run:

```sql
CREATE DATABASE aniconnect;
```

## 5) Run migrations

```
python manage.py migrate
```

After this, database tables should be created.

## 6) Load fixtures

Load anime data:

```
python manage.py loaddata anime_data.json
```

Load categories data:

```
python manage.py loaddata categories.json
```

If both run without error, your project setup is correct.

## 7) Run the server

```
python manage.py runserver
```

Open your browser and check that anime and category data appears in the app.

---

## Quick troubleshooting

- If MySQL connection fails, confirm DB credentials in `website/settings.py`.
- If `python` is not found, try `python3`.
- If fixture loading fails, make sure migrations completed successfully first.
