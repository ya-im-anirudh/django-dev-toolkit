# 📦 Django Development Project

This is a Django-based development project currently integrating the **[Django Dev Toolkit](https://github.com/yourusername/django-dev-toolkit)** to speed up backend–frontend collaboration and simplify database management during development.

---

## 🚀 Overview

The project is set up for rapid prototyping and testing, with the goal of:
- Allowing frontend teams to work independently using **mock APIs**.
- Providing clear insights into database relationships with an **auto-generated database mapper**.
- Testing planned future tools like **bulk data upload** and **performance monitoring**.

---

## 🛠 Tech Stack

- **Backend:** [Django](https://www.djangoproject.com/)  
- **Database:** PostgreSQL (or any supported DB)  
- **Toolkit:** [Django Dev Toolkit](https://github.com/yourusername/django-dev-toolkit)  
- **Frontend (optional):** React / Any API consumer

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/project-name.git
cd project-name
```

## ⚙️ Installation & Setup

### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```bash
python manage.py migrate
```

### 5️⃣ Create Superuser
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Development Server
```bash
python manage.py runserver
```

## 🔧 Integrating Django Dev Toolkit

Add the toolkit to INSTALLED_APPS in settings.py

```python
INSTALLED_APPS = [
    # ... other apps
    "django_dev_toolkit",
]
```

## ☕ Support the Project

If you find this project helpful, you can support development by buying me a coffee!  
<br>
<a href="https://www.buymeacoffee.com/anirudh_mk" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" width="200" />
</a>


