# Phishing Website Detection

A Django-based web application for detecting phishing websites using machine learning. This system uses a Random Forest classifier trained on various URL features to classify websites as legitimate or phishing.

## Features

- **User Authentication**: Registration system with admin approval
- **Machine Learning Pipeline**: Train models and make real-time predictions
- **Admin Dashboard**: User management and oversight
- **Responsive Web Interface**: Clean, modern UI for easy interaction
- **Health Monitoring**: Built-in health check endpoint for deployment monitoring

## Setup Instructions

### Prerequisites

- Python 3.11+ (specifically tested with Python 3.11.x)
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd "phishing website detection"
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**
   ```bash
   # Windows PowerShell
   $env:SECRET_KEY="your-secret-key-here"
   $env:DEBUG="True"
   
   # Linux/Mac
   export SECRET_KEY="your-secret-key-here"
   export DEBUG="True"
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Homepage: http://127.0.0.1:8000/
   - Admin Login: http://127.0.0.1:8000/Adminlogin/ (admin/admin)
   - Health Check: http://127.0.0.1:8000/health/

### Running Tests

```bash
python manage.py test
```

## Deployment to Render

This application is configured for deployment on Render.com.

### Prerequisites

- Git repository pushed to GitHub/GitLab
- Render account

### Deployment Steps

1. **Push code to your repository**
   ```bash
   git add .
   git commit -m "Add Render deployment configuration"
   git push origin main
   ```

2. **Create Web Service on Render**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "Web Service"
   - Connect your repository
   - Configure settings:
     - **Name**: `phishing-detector` (or your preferred name)
     - **Environment**: `Python 3`
     - **Build Command**: `./build.sh`
     - **Start Command**: `gunicorn Phising_website_Detection.wsgi:application`
     - **Plan**: Free (or paid plan for better performance)

3. **Set Environment Variables**
   In the Render dashboard, add these environment variables:
   - `SECRET_KEY`: Generate a secure secret key
   - `DEBUG`: `False`
   - `WEB_CONCURRENCY`: `4`
   - `PYTHON_VERSION`: `3.11.11` (ensures correct Python version)
   - `PORT`: `10000`

4. **Deploy**
   - Click "Create Web Service"
   - Monitor the build logs for any issues
   - Once deployed, visit your app at `https://your-app-name.onrender.com`

### Post-Deployment Verification

- Visit your deployed URL
- Check `/health/` endpoint returns "OK"
- Test admin login (admin/admin)
- Test user registration and login flow
- Test ML prediction functionality

## Architecture

### Django Apps
- **Phising_website_Detection/**: Main project configuration
- **users/**: User management, ML training, and prediction
- **admins/**: Admin user management

### Machine Learning Pipeline
1. **Dataset**: Located in `media/dataset_phishing.csv`
2. **Training**: Feature correlation analysis → Feature selection → Random Forest training
3. **Prediction**: 23-feature input → Model inference → Classification result

### Key Files
- `manage.py`: Django management script
- `requirements.txt`: Python dependencies
- `build.sh`: Render build script
- `render.yaml`: Render service configuration
- `WARP.md`: Detailed development guide

## Usage

### Admin Workflow
1. Login with admin/admin
2. View registered users
3. Activate/deactivate user accounts
4. Monitor system usage

### User Workflow
1. Register for account
2. Wait for admin approval
3. Login and access ML features
4. View dataset
5. Train ML model (if needed)
6. Submit URLs for phishing detection

### ML Prediction Features
The model analyzes 23 features including:
- URL structure (length, dots, slashes)
- Domain properties (age, Google index, page rank)
- Content analysis (hyperlinks, title)
- Security indicators (IP usage, suspicious patterns)

## Technical Details

### Dependencies
- **Django 4.1.1**: Web framework
- **scikit-learn**: Machine learning
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **matplotlib/seaborn**: Visualization
- **gunicorn**: WSGI server
- **whitenoise**: Static file serving
- **django-environ**: Environment variable management

### Security Notes
- Change default admin credentials in production
- Use strong SECRET_KEY in production
- Set DEBUG=False in production
- Configure proper ALLOWED_HOSTS

### Performance
- SQLite database (upgrade to PostgreSQL for production scale)
- Whitenoise for efficient static file serving
- Gunicorn WSGI server with multiple workers

## Support

- Check `WARP.md` for detailed development guidance
- Review test files for usage examples
- Monitor Render deployment logs for troubleshooting