<div align="center">

# 🏋️ Gym Management System

**A full-stack Django web application for managing gym operations — members, plans, equipment, enquiries, and user registrations with real-time Supabase PostgreSQL database.**

[![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://supabase.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

[Live Demo](#-deployment) • [Report Bug](https://github.com/shivamchoudhary0110/Gym_Management_system/issues) • [Request Feature](https://github.com/shivamchoudhary0110/Gym_Management_system/issues)

</div>

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Screenshots](#-screenshots)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [Project Structure](#-project-structure)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## ✨ Features

### Admin Dashboard
- 📊 **Dashboard Overview** — Real-time stats for enquiries, plans, equipment, members, and registered users
- 👥 **Member Management** — Full CRUD operations for gym members with plan assignments
- 📦 **Plan Management** — Create, edit, and delete membership plans with pricing and duration
- 🏋️ **Equipment Tracking** — Track gym equipment with purchase details and descriptions
- ❓ **Enquiry Management** — Manage customer enquiries with status tracking
- 👤 **User Management** — View, edit, and manage registered users with staff/superuser toggle
- 📬 **Query Management** — Read and manage contact form submissions
- 🔐 **Password Management** — Secure password change functionality

### User Panel
- 🏠 **User Dashboard** — Welcome page with profile info and membership status
- 📝 **User Registration** — Full profile creation with personal details
- 💳 **Plan Subscription** — Browse and subscribe to available gym plans
- 👤 **Profile Management** — Edit personal information and contact details
- 📋 **Membership History** — View all active and past memberships

### General
- 📱 **Fully Responsive** — Optimized for desktop, tablet, and mobile devices
- 🎨 **Bold Gym Theme** — Dark UI with red/orange accents and smooth animations
- 📧 **EmailJS Integration** — Contact form with real-time email notifications
- 🔒 **Secure Authentication** — Django's built-in auth with role-based access control
- ⚡ **Real-time Sync** — All data changes reflect instantly via Supabase PostgreSQL

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Django 5.2, Python 3.10+ |
| **Database** | PostgreSQL (Supabase) |
| **Frontend** | HTML5, CSS3, JavaScript |
| **CSS Framework** | Custom Gym Theme (CSS Variables, Grid, Flexbox) |
| **Icons** | Font Awesome 5.15 |
| **Fonts** | Google Fonts (Montserrat) |
| **Email** | EmailJS |
| **Deployment** | Render / Railway / PythonAnywhere |

---

## 📸 Screenshots

> Add screenshots of your application here after deployment.

```
Homepage        |  Admin Dashboard  |  User Dashboard
----------------|-------------------|----------------
[Hero Section]  | [Stats Cards]     | [Profile Info]
[Features]      | [Quick Actions]   | [Plan Selection]
[Classes]       | [Data Tables]     | [Membership]
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git
- A [Supabase](https://supabase.com/) account (for PostgreSQL database)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shivamchoudhary0110/Gym_Management_system.git
   cd Gym_Management_system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your actual credentials
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Open in browser**
   ```
   http://127.0.0.1:8000/
   ```

### Quick Start (Windows)

Double-click `run_windows.bat` to automatically set up and launch the application.

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
# Django
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

# Supabase PostgreSQL
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your-supabase-password
DB_HOST=your-project.supabase.co
DB_PORT=5432

# EmailJS
EMAILJS_SERVICE_ID=your-service-id
EMAILJS_TEMPLATE_ID=your-template-id
EMAILJS_PUBLIC_KEY=your-public-key
```

> ⚠️ **Never commit the `.env` file.** It is already included in `.gitignore`.

---

## 📁 Project Structure

```
Gym_Management_system/
├── GymManagementDjango/       # Django project settings
│   ├── settings.py            # Configuration (reads from .env)
│   ├── urls.py                # Root URL configuration
│   ├── wsgi.py                # WSGI application
│   └── asgi.py                # ASGI application
├── gym/                       # Main application
│   ├── migrations/            # Database migrations
│   ├── static/                # Static files (CSS, images)
│   │   ├── css/
│   │   │   └── gym-theme.css  # Main stylesheet
│   │   └── images/            # Image assets
│   ├── templates/             # HTML templates (26 files)
│   ├── admin.py               # Admin panel configuration
│   ├── forms.py               # Django forms
│   ├── models.py              # Database models
│   ├── urls.py                # App URL routes
│   └── views.py               # View logic
├── .env                       # Environment variables (gitignored)
├── .gitignore                 # Git ignore rules
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── run_windows.bat            # Windows quick launcher
└── README.md                  # This file
```

---

## 🌐 Deployment

### Render (Recommended — Free)

1. Push your code to GitHub
2. Go to [render.com](https://render.com) and create a new **Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn GymManagementDjango.wsgi:application`
5. Add all environment variables from your `.env` file in the **Environment** section
6. Deploy — your app will be live at `https://your-app.onrender.com`

### Railway

1. Go to [railway.app](https://railway.app)
2. Deploy from GitHub repo
3. Add environment variables
4. Railway auto-detects Django and deploys

### PythonAnywhere

1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Upload your code or clone from GitHub
3. Set up a virtual environment and install requirements
4. Configure the WSGI file and static files
5. Set environment variables in the web app settings

> **Note:** Vercel is not ideal for Django apps as it's designed for static sites and serverless functions. Use Render, Railway, or PythonAnywhere for full Django deployment.

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

**Shivam Choudhary**

- GitHub: [@shivamchoudhary0110](https://github.com/shivamchoudhary0110)
- Email: info@gymmanagement.com

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

</div>
