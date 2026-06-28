# Nilesh Yadav — Django Portfolio

A responsive personal portfolio built with Python & Django, replicating and enhancing the design from the screenshot.

## Features
- Fully responsive (mobile, tablet, desktop)
- Sticky animated navbar with active section highlighting
- Hero section with floating tech badges
- About section with info cards
- Skills grid with dot indicators
- Projects showcase with tags & links
- Contact form with AJAX submission (saves to SQLite via Django ORM)
- Smooth scroll & scroll-reveal animations
- Django Admin panel to manage contact messages

## Quick Start

### 1. Create & activate a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run database migrations
```bash
python manage.py migrate
```

### 4. (Optional) Create a superuser for Django Admin
```bash
python manage.py createsuperuser
```

### 5. Start the development server
```bash
python manage.py runserver
```

### 6. Open in your browser
- Portfolio: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## Project Structure
```
nilesh_portfolio/
├── config/               # Django project settings & URLs
│   ├── settings.py
│   └── urls.py
├── core/                 # Main app
│   ├── templates/core/
│   │   └── index.html    # Main template
│   ├── models.py         # Skill, Project, ContactMessage
│   ├── views.py          # Home view with contact form handling
│   ├── forms.py          # ContactForm
│   ├── admin.py          # Admin registrations
│   └── urls.py
├── static/
│   ├── css/style.css     # All styles
│   └── js/main.js        # Navbar, AJAX form, scroll effects
├── manage.py
└── requirements.txt
```

## Customisation
- **Personal info**: Edit `core/views.py` — update `SKILLS_DATA` and `PROJECTS_DATA`
- **Styles**: Edit `static/css/style.css` — CSS variables at the top control the whole palette
- **Template**: Edit `core/templates/core/index.html`
- **Contact messages**: View them in Django Admin at `/admin/`

## Production Notes
- Set `DEBUG = False` in `config/settings.py`
- Change `SECRET_KEY` to a strong random value
- Configure a real email backend (SMTP) instead of `console.EmailBackend`
- Run `python manage.py collectstatic` and serve static files via Nginx/WhiteNoise
