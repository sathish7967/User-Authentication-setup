# User Authentication Setup using Django

## Project Overview
This project is a Django-based authentication system with a Custom User Model, separate login functionality for Admin and Distributor users, OTP-based password recovery, role-based dashboard access, and secure password management.

**Technology:** Python with Django  
**Company:** Brainybeam Info-Tech PVT LTD

---

## Features
- Custom User Model
- Admin Login
- Distributor Login
- Role-Based Dashboard Redirect
- Forgot Password with OTP
- OTP Verification
- Password Reset
- Logout Functionality
- Secure Password Hashing

---

## Technologies Used
- Python
- Django
- SQLite
- HTML

---

## Project Structure

auth_project/
│
├── accounts/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── utils.py
│
├── auth_project/
│   ├── settings.py
│   └── urls.py
│
├── templates/
│   ├── login.html
│   ├── forgot_password.html
│   ├── verify_otp.html
│   ├── reset_password.html
│   ├── admin_dashboard.html
│   └── distributor_dashboard.html
│
├── manage.py
└── db.sqlite3

---

## Installation Steps

### 1. Create Virtual Environment

```bash
python -m venv venv
2. Activate Environment
Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate
3. Install Django
pip install django
4. Run Migrations
python manage.py makemigrations
python manage.py migrate
5. Create Superuser
python manage.py createsuperuser
6. Run Server
python manage.py runserver

Open:

http://127.0.0.1:8000/
Email Backend Configuration

Add in settings.py:

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

OTP will appear in terminal during testing.

Login Flow
Login
   ↓
Authenticate User
   ↓
Check Role
   ↓
Redirect Dashboard
Password Recovery Flow
Forgot Password
      ↓
Generate OTP
      ↓
Verify OTP
      ↓
Reset Password
URLs
URL	Description
/	Login Page
/admin-dashboard/	Admin Dashboard
/distributor-dashboard/	Distributor Dashboard
/forgot-password/	Forgot Password
/verify-otp/	Verify OTP
/reset-password/	Reset Password
/logout/	Logout
Testing
Login Testing
Login as Admin → Admin Dashboard
Login as Distributor → Distributor Dashboard
OTP Testing
Enter registered email
Check OTP in terminal
Verify OTP
Reset password
Login with new password
Future Enhancements
JWT Authentication
SMS OTP
OTP Expiry
Two-Factor Authentication
Email Verification
Learning Outcomes
Django Authentication
Custom User Models
Role-Based Access
OTP Verification
Session Management
Secure Password Handling
