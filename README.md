# جمعية HTAP Algérie

موقع تعريفي رسمي لجمعية **HTAP Algérie**، يهدف إلى تقديم الجمعية بشكل احترافي، التعريف برسالتها وأهدافها، ونشر المعلومات والتوعية حول ارتفاع ضغط الدم الشرياني الرئوي (HTAP).

يوفر الموقع منصة رقمية حديثة تساعد المرضى وعائلاتهم والزوار على الوصول بسهولة إلى المعلومات، خدمات التوجيه والمساعدة، أخبار الجمعية وأنشطتها، بالإضافة إلى طرق التواصل والانضمام ودعم الجمعية.

## أهداف المشروع

- التعريف بالجمعية وتاريخها ورسالتها.
- نشر التوعية والمعلومات حول HTAP.
- تقديم التوجيه والمساعدة للمرضى.
- عرض المقالات والمحتوى التوعوي.
- توثيق أنشطة وفعاليات الجمعية.
- التعريف بأعضاء الجمعية.
- تسهيل التواصل مع الجمعية.
- توفير معلومات حول العضوية ودعم الجمعية.
- تقديم الموقع بثلاث لغات: العربية، الفرنسية والإنجليزية.

## التقنيات

تم تطوير المشروع باستخدام:

- **Django** للواجهة الخلفية وإدارة المحتوى.
- **Tailwind** لتصميم الواجهة وتجعلها متجاوبة مع مختلف الأجهزة.
- **Django Templates** لبناء صفحات الموقع.
- **SQLite / PostgreSQL** حسب بيئة التشغيل.
- نظام ترجمة متعدد اللغات يدعم **العربية RTL والفرنسية والإنجليزية**.

## أقسام الموقع

يتكون الموقع من عدة أقسام رئيسية:

- الرئيسية
- من نحن
- HTAP
- المقالات
- النشاطات والفعاليات
- المساعدة والتوجيه
- العضوية ودعم الجمعية
- التواصل

كما يتضمن لوحة تحكم Django لإدارة محتوى الموقع، مثل المقالات، النشاطات، الأعضاء، الإحصائيات ورسائل التواصل.

## حالة المشروع

المشروع **قيد التطوير** ويتم العمل حاليًا على تطوير الواجهة، المحتوى، نظام إدارة المحتوى وتجربة المستخدم للوصول إلى موقع احترافي حديث يناسب جمعية صحية بمستوى دولي.





أكيد. بما أن المشروع حقيقي وسيتم تطويره وتسليمه للجمعية، الأفضل أن يكون الـ`README.md` أقرب إلى **documentation احترافي للمشروع** وليس مجرد تعليمات تشغيل.

هذه نسخة أكثر احترافية ومنظمة:

````markdown
# HTAP Algérie

> Official website of HTAP Algérie — Association dedicated to awareness,
> information, guidance, and support for people affected by pulmonary arterial hypertension.

---

## Table of Contents

- [Overview](#overview)
- [Project Goals](#project-goals)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Applications](#applications)
- [Content Management](#content-management)
- [Internationalization](#internationalization)
- [URL Structure](#url-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Environment Configuration](#environment-configuration)
- [Database Setup](#database-setup)
- [Django Administration](#django-administration)
- [Development](#development)
- [Testing](#testing)
- [Static and Media Files](#static-and-media-files)
- [Security](#security)
- [Production Deployment](#production-deployment)
- [Maintenance](#maintenance)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

HTAP Algérie is a multilingual institutional website developed for the
association to provide reliable information about the association,
pulmonary arterial hypertension, patient support, activities, events,
articles, membership, and ways to support the association.

The platform provides a public-facing website combined with a
Django-powered administration interface allowing authorized users to
manage the website content without modifying the source code.

---

## Project Goals

The main objectives of the platform are:

- Present the association and its mission.
- Provide reliable educational information.
- Publish articles and awareness content.
- Present association activities and events.
- Highlight interviews, campaigns, and conferences.
- Provide guidance and support information.
- Explain membership and support opportunities.
- Provide clear contact channels.
- Present association members.
- Display association statistics.
- Support Arabic, French, and English content.
- Provide a responsive experience across devices.
- Make content management simple through Django Admin.

---

# Features

## Public Website

### Home

The homepage provides an overview of the association and highlights:

- Association introduction
- Key statistics
- Latest articles
- Featured activities
- Main support services
- Membership and support
- Contact information

### About the Association

Contains:

- Association history
- Mission
- Objectives
- Responsibilities
- Association members

### HTAP

Educational information about pulmonary arterial hypertension.

The section can contain:

- General information
- Symptoms
- Diagnosis
- Treatment information
- Awareness content
- Useful guidance

> Medical content should be reviewed and approved by qualified healthcare
> professionals before publication.

### Articles

The article platform supports:

- Categories
- Featured articles
- Publication status
- Publication dates
- Authors
- Featured images
- Multilingual content
- SEO metadata
- Structured content blocks

Supported content blocks include:

- Heading
- Paragraph
- Image
- Quote

### Activities

The activities section presents the association's activities and events.

Supported activity types:

- Events
- Interviews
- Campaigns
- Meetings
- Conferences
- Other activities

Activities support:

- Date
- Location
- Featured image
- Gallery
- Multilingual content
- Structured content blocks
- Publication status

### Help and Guidance

Provides information about:

- Services provided by the association
- Patient guidance
- Available support
- How to request assistance
- How to contact the association

### Membership and Support

Provides information about:

- Joining the association
- Membership process
- Ways to support the association
- Volunteer opportunities
- Other forms of participation

### Contact

Provides:

- Address
- Phone
- Email
- Social media
- Map
- Contact form

---

# Technology Stack

## Backend

- Python
- Django
- PostgreSQL

## Frontend

- Django Templates
- HTML5
- CSS3
- JavaScript

## Media

- Pillow

## Administration

- Django Admin

## Internationalization

- Django i18n
- Django translation framework
- RTL support for Arabic

---

# Architecture

The project follows a modular Django architecture.

```text
                    ┌────────────────────┐
                    │    Public Website  │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │   Django Views     │
                    │      (CBV)         │
                    └─────────┬──────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
           Core            Articles        Activities
              │               │               │
              └───────────────┼───────────────┘
                              ▼
                    ┌────────────────────┐
                    │    PostgreSQL      │
                    └────────────────────┘
````

The project uses Class-Based Views (CBV) for reusable and maintainable
request handling.

---

# Project Structure

```text
htap_algerie/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── core/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── articles/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── activities/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── templates/
│   ├── base.html
│   ├── components/
│   ├── core/
│   ├── articles/
│   └── activities/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/
│
├── locale/
│
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

# Applications

## `core`

Contains shared and association-level functionality.

### Models

```text
AssociationInfo
Statistic
Member
ContactMessage
```

### Responsibilities

* Association information
* Contact information
* Social media
* Statistics
* Members
* Contact messages
* Static informational pages

---

# Articles

The `articles` application manages all educational and informational
content.

### Models

```text
Article
ArticleCategory
ArticleTranslation
ArticleBlock
```

### Relationships

```text
Article
│
├── Category
│
├── Featured Image
│
├── French Translation
│   └── Content Blocks
│
├── Arabic Translation
│   └── Content Blocks
│
└── English Translation
    └── Content Blocks
```

---

# Activities

The `activities` application manages association events and activities.

### Models

```text
Activity
ActivityTranslation
ActivityBlock
ActivityImage
```

### Relationships

```text
Activity
│
├── Activity Type
├── Date
├── Location
├── Featured Image
├── Gallery
│
├── French Translation
│   └── Content Blocks
│
├── Arabic Translation
│   └── Content Blocks
│
└── English Translation
    └── Content Blocks
```

---

# Content Management

Content is managed through Django Admin.

Administrators can manage:

```text
Association
├── General information
├── Contact information
├── Social media
└── Statistics

Members
├── Name
├── Role
├── Photo
└── Biography

Articles
├── Categories
├── Translations
├── Content blocks
├── Images
├── Publication
└── SEO

Activities
├── Type
├── Translations
├── Content blocks
├── Gallery
├── Date
├── Location
└── Publication

Messages
├── Sender
├── Subject
├── Message
└── Status
```

---

# Internationalization

The website supports three languages:

| Code | Language |
| ---- | -------- |
| `fr` | Français |
| `ar` | العربية  |
| `en` | English  |

Django's internationalization framework is used for interface
translations.

Model labels use:

```python
from django.utils.translation import gettext_lazy as _
```

Example:

```python
name = models.CharField(_("name"), max_length=200)
```

Content itself is stored using dedicated translation models.

Example:

```text
Article
├── ArticleTranslation (fr)
├── ArticleTranslation (ar)
└── ArticleTranslation (en)
```

Arabic pages must support RTL layout.

---

# URL Structure

```text
/                           Home
/about/                     About
/htap/                      HTAP
/articles/                  Articles
/articles/<slug>/           Article details
/activities/                Activities
/activities/<slug>/         Activity details
/help/                      Help and guidance
/membership/                Membership and support
/contact/                   Contact
/admin/                     Administration
```

---

# Requirements

Recommended environment:

```text
Python 3.12+
PostgreSQL 15+
Django
Pillow
```

The exact Python packages are defined in:

```text
requirements.txt
```

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd htap_algerie
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Configuration

Create a `.env` file:

```env
DEBUG=True

SECRET_KEY=change-me

DB_NAME=htap_algerie
DB_USER=postgres
DB_PASSWORD=change-me
DB_HOST=localhost
DB_PORT=5432
```

For email configuration:

```env
EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=
```

Never commit `.env` to Git.

Add it to `.gitignore`:

```text
.env
```

---

# Database Setup

Create the PostgreSQL database:

```sql
CREATE DATABASE htap_algerie;
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create the administrator:

```bash
python manage.py createsuperuser
```

---

# Development Server

Run:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Administration:

```text
http://127.0.0.1:8000/admin/
```

---

# Django Checks

Run the Django system check:

```bash
python manage.py check
```

For deployment checks:

```bash
python manage.py check --deploy
```

---

# Static Files

Static assets are stored in:

```text
static/
```

Recommended structure:

```text
static/
├── css/
├── js/
└── images/
```

Collect static files for production:

```bash
python manage.py collectstatic
```

---

# Media Files

Uploaded content is stored under:

```text
media/
```

Examples:

```text
media/
├── association/
├── members/
├── articles/
└── activities/
```

Media files must not be committed to Git unless explicitly required.

Add to `.gitignore`:

```text
media/
```

---

# Contact Form

The contact form uses the `ContactMessage` model.

Submitted messages are stored in the database and can be managed
through Django Admin.

Available statuses:

```text
New
Read
Replied
Archived
```

The form contains:

```text
First name
Last name
Email
Phone
Subject
Message
```

The contact form should include CSRF protection and server-side
validation.

---

# Security

The application should follow Django security best practices.

Production configuration must include:

```python
DEBUG = False
```

Configure:

```text
ALLOWED_HOSTS
CSRF_TRUSTED_ORIGINS
SECURE_SSL_REDIRECT
SESSION_COOKIE_SECURE
CSRF_COOKIE_SECURE
```

Sensitive configuration must be stored in environment variables.

Never expose:

* `SECRET_KEY`
* Database credentials
* Email credentials
* API credentials

---

# SEO

The platform is designed to support:

* Page titles
* Meta descriptions
* Semantic URLs
* Slugs
* Open Graph metadata
* Social sharing metadata
* Sitemap
* Robots configuration
* Multilingual SEO

Articles and activities contain:

```text
meta_title
meta_description
```

SEO fields should be populated for published content.

---

# Accessibility

The frontend should follow accessibility best practices:

* Semantic HTML
* Proper heading hierarchy
* Alt text for images
* Keyboard navigation
* Sufficient contrast
* Accessible forms
* Clear focus states
* RTL support for Arabic

---

# Performance

Recommended practices:

* Use `select_related()` for foreign keys.
* Use `prefetch_related()` for translations and galleries.
* Paginate articles and activities.
* Optimize uploaded images.
* Use appropriate image dimensions.
* Minimize unnecessary database queries.
* Cache suitable public content when required.

Example:

```python
Article.objects.select_related("category").prefetch_related("translations")
```

---

# Development Guidelines

## Class-Based Views

The project uses Django CBVs.

Example:

```python
class ArticleListView(ListView):
    model = Article
```

## URL Namespaces

Each application defines its namespace:

```python
app_name = "articles"
```

Use named URLs:

```python
reverse("articles:detail", kwargs={"slug": article.slug})
```

## Code Style

Use compact tuples:

```python
fields = ("title", "excerpt", "meta_title", "meta_description")
```

Avoid unnecessary formatting changes.

---

# Git Workflow

Recommended branch structure:

```text
main
develop
feature/*
fix/*
```

Examples:

```text
feature/articles
feature/activities
feature/i18n
feature/contact-form
fix/article-slug
```

Commit messages should be clear:

```text
feat: add article translations
feat: add activity gallery
feat: add contact form
fix: handle missing article translation
refactor: improve article queries
```

---

# Testing

Run the test suite:

```bash
python manage.py test
```

Tests should cover:

* Models
* URLs
* Views
* Forms
* Language fallback
* Published content
* Contact form validation
* Admin permissions

---

# Deployment

A production deployment should include:

```text
                    Internet
                       │
                       ▼
                 Reverse Proxy
                  Nginx / CDN
                       │
                       ▼
                    Gunicorn
                       │
                       ▼
                    Django
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
        PostgreSQL             Media
```

Production requirements:

* PostgreSQL
* Gunicorn
* Nginx or equivalent reverse proxy
* HTTPS
* Static file serving
* Media file storage
* Database backups
* Application logging
* Environment variables

---

# Backup Strategy

The production database should be backed up regularly.

Recommended backup scope:

```text
PostgreSQL database
Media files
Environment configuration
```

At minimum:

* Daily database backups
* Regular media backups
* Off-server backup storage

---

# Maintenance

Common Django commands:

```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
python manage.py test
```

Before deployment:

```bash
python manage.py check --deploy
```

---

# Project Status

Current development areas:

* [x] Django project setup
* [x] Core models
* [x] Article models
* [x] Activity models
* [x] Contact form model
* [x] Django Admin
* [x] Application URLs
* [x] Class-Based Views
* [ ] Final i18n routing
* [ ] Templates
* [ ] Frontend UI
* [ ] Arabic RTL interface
* [ ] SEO implementation
* [ ] Sitemap
* [ ] Email notifications
* [ ] Automated tests
* [ ] Production deployment

---

# Content Policy

The website is an institutional platform for HTAP Algérie.

All medical and health-related information must be reviewed and approved
by the association and/or qualified healthcare professionals before
publication.

The website should not present general educational content as a
substitute for professional medical advice.

---

# Ownership

This project is developed for HTAP Algérie.

The association retains ownership of its:

* Logo
* Brand identity
* Textual content
* Images
* Videos
* Documents
* Publications

Third-party libraries remain subject to their respective licenses.

---

# License

The application source code is proprietary unless otherwise specified
by the project owner.

Association content and media remain the property of HTAP Algérie or
their respective owners.

---

# Contact

For project-related inquiries, contact the project administrator
through the official HTAP Algérie communication channels.

```

هذه النسخة أفضل كـREADME فعلي للمشروع لأنها أصبحت تشمل **Architecture + Development + Security + Deployment + SEO + Accessibility + Testing + Content management**، وليس فقط أوامر تثبيت Django.
```
