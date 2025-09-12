# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a Django-based web application for detecting phishing websites using machine learning. The system includes user registration/authentication, admin functionality, dataset visualization, model training, and real-time phishing detection.

## Setup and Installation

### Prerequisites
Install required Python packages:
```bash
pip install django pandas matplotlib seaborn scikit-learn pickle-mixin
```

### Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

## Common Development Commands

### Running the Development Server
```bash
python manage.py runserver
```
The application will be available at http://127.0.0.1:8000/

### Database Operations
```bash
# Make migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Interactive shell
python manage.py shell

# Collect static files (if needed in production)
python manage.py collectstatic
```

### Testing
```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test users
python manage.py test admins
```

## Application Architecture

### Django Apps Structure
- **Phising_website_Detection/** - Main Django project configuration
- **users/** - User registration, authentication, ML training and prediction functionality
- **admins/** - Admin user management and oversight features

### Key Components

#### User Management Flow
- Users register via `UserRegistrationForm` with validation patterns
- Admin approval required (status: "waiting" → "activated")
- Session-based authentication for both users and admins

#### Machine Learning Pipeline
Located in `users/views.py`:

1. **Dataset Processing** (`DatasetView`):
   - Loads `media/dataset_phishing.csv` (first 100 rows for display)
   - Dataset contains URL features and phishing/legitimate labels

2. **Model Training** (`training`):
   - Feature correlation analysis with heatmap generation
   - Feature selection based on correlation threshold (0.2)
   - Random Forest Classifier (350 estimators)
   - Train/test split (80/20)
   - Model serialization with pickle

3. **Prediction** (`prediction`):
   - 23 feature inputs for URL analysis
   - Features include: length_url, nb_dots, ip, phish_hints, domain_age, etc.
   - Real-time classification: "Phishing" or "Legitimate"

#### Admin Features
- Hardcoded admin credentials (admin/admin)
- User activation/deletion capabilities
- View all registered users

### Database Models

#### UserRegistrationModel
- Comprehensive user profile with validation
- Status field for activation workflow
- Unique constraints on loginid, mobile, email

### Template Structure
- **templates/**: Base templates and main pages
- **templates/users/**: User-specific functionality pages
- **templates/admins/**: Admin interface templates

## File Locations

### Core Configuration
- `settings.py` - Django configuration, includes media/static file paths
- `urls.py` - URL routing for entire application
- `manage.py` - Django management script

### Machine Learning Assets
- `media/dataset_phishing.csv` - Training dataset
- `model_phishing_webpage_classifier` - Serialized Random Forest model
- `heatmap.png` - Feature correlation visualization

### Static Files
- `static/` - CSS, JavaScript, images
- `STATIC_DIR` and `MEDIA_ROOT` configured in settings

## Development Notes

### Security Considerations
- SECRET_KEY exposed in settings.py (development only)
- Admin credentials hardcoded
- DEBUG=True in current configuration
- ALLOWED_HOSTS set to ['*']

### Model Features
The ML model uses these 23 features for phishing detection:
- URL structure: length_url, length_hostname, nb_dots, nb_slash
- Content analysis: nb_hyperlinks, ratio_intHyperlinks, empty_title
- Domain properties: domain_age, google_index, page_rank
- Security indicators: ip, tld_in_subdomain, prefix_suffix, phish_hints

### Data Flow
1. User registers → Admin activates → User can access ML features
2. Dataset view → Model training → Feature selection → Model saving
3. Prediction form → Feature extraction → Model loading → Classification

## Current Environment Requirements

The system requires Django and ML libraries. Current environment missing Django installation, so first install:
```bash
pip install django==4.1.1
```

Then proceed with standard Django development commands.