# 🔐 Flask Portfolio Web Application

A full-featured Flask-based portfolio web application with user authentication, personalized dashboard, admin panel, and project showcase. Designed to highlight the developer's background, experience, and technical capabilities in a professional format.

---

## 🚀 Features

- ✅ **User Authentication**: Sign up, login, logout, session management
- ✅ **Password Reset**: Email-based secure password reset with token validation
- ✅ **Admin Dashboard**: View and manage registered users (admin only)
- ✅ **User Portal**: Personalized dashboard with professional experience and project highlights
- ✅ **Responsive UI**: Bootstrap 5-powered modern UI with custom animations
- ✅ **Project Pages**: Separate pages for detailed project demos and GitHub links
- ✅ **Environment-Safe Setup**: `.env` support for credentials and secure configs

---

## 🛠️ Tech Stack

- **Frontend**: Bootstrap 5, HTML5, Jinja2
- **Backend**: Flask, Flask-Login, Flask-WTF, Flask-Mail, Flask-Migrate
- **Database**: SQLite (via SQLAlchemy ORM)
- **Auth & Security**: JWT, OAuth 2.0 (conceptual), Email Verification
- **DevOps**: Git, Python Virtual Environment, `.env` config

---

## 📚 Key Modules

| Module         | Description                                  |
|----------------|----------------------------------------------|
| `auth`         | Handles login, signup, reset password        |
| `routes`       | Renders home, portal, project, and admin     |
| `models.py`    | SQLAlchemy models (User, reset tokens)       |
| `forms.py`     | Flask-WTF forms with validators              |

---

## 🔧 Prerequisites

- Python 3.8+
- pip
- Virtualenv (recommended)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/flask_portfolio_auth.git
cd flask_portfolio_auth
