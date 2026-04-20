# 📚 School Management System (Django)

## 📌 Project Overview

This is a **School Management System** built using **Django** to help manage students, classes, subjects, and academic reports efficiently.

The system is designed to simplify school operations such as:

* Student registration
* Class management
* Report generation
* Admin control

---

## 🚀 Features

### 👨‍🎓 Student Management

* Register new students
* Store student details (name, age, gender, parent info)
* Assign students to classes

### 🏫 Class & Subject Management

* Create and manage classes
* Assign subjects to classes
* Organize academic structure

### 📊 Report System

* Input classwork and exam scores
* Automatically calculate totals
* Generate student reports per term
* View reports per class or student

### 🔐 Authentication System

* Admin login/logout
* Secure access to system features

### ⚙️ Admin Dashboard

* Manage users
* Manage students, classes, and reports
* Central control panel

---

## 🛠️ Technologies Used

* **Python**
* **Django**
* **HTML & CSS**
* **SQLite (default database)**

---

## 📂 Project Structure

```
project_root/
│
├── app_staff/        # Main application logic
├── templates/        # HTML templates
├── static/           # CSS, JS, assets
├── db.sqlite3        # Database
├── manage.py         # Django management script
└── README.md         # Project documentation
```

---

## ⚡ Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/Alalar32/gps.git
cd your-repo-name
```

2. Create a virtual environment:

```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

3. Install dependencies:

```bash
pip install django
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start the server:

```bash
python manage.py runserver
```

6. Open in browser:

```
http://127.0.0.1:8000/
```

---

## 💡 Usage

* Login as admin
* Add classes and subjects
* Register students
* Input scores and generate reports

---

## 🎯 Future Improvements

* SMS notification system
* Better UI/UX design
* Export reports (PDF/Excel)
* Role-based access (teachers, admins)
* Online access for parents

---

## 🤝 Contribution

Contributions are welcome! Feel free to fork the project and submit a pull request.

---

## 📄 License

This project is for educational purposes.

---

## 👤 Author

**Elijah Tawiah Dotse**

---
