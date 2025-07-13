# 🚀 Quick Start Guide - Mental Wellness Portal

Get your Mental Wellness Portal up and running in minutes!

## 📋 Prerequisites

- Python 3.7 or higher
- MongoDB (local or Atlas)
- Internet connection (for Tailwind CSS CDN)

## ⚡ Quick Setup (5 minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Environment
```bash
# Run the setup script
python setup.py

# Or manually create .env file
cp env_example.txt .env
```

### 3. Configure MongoDB

#### Option A: Local MongoDB
1. Install MongoDB Community Edition
2. Start MongoDB service
3. No additional configuration needed

#### Option B: MongoDB Atlas (Recommended)
1. Go to [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Create free account and cluster
3. Get connection string
4. Update `.env` file:
   ```
   MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/mental_wellness?retryWrites=true&w=majority
   ```

### 4. Run the Application
```bash
python app.py
```

### 5. Access the Portal
Open your browser and go to: **http://localhost:5000**

## 🎯 What You'll See

### Home Page (`/`)
- Welcome message and feature overview
- Quick action buttons
- Emergency contact information
- Statistics and testimonials

### Registration (`/register`)
- Student registration form
- Name, email, and password fields
- Privacy notice and terms

### Login (`/login`)
- User authentication
- Remember me functionality
- Links to resources and crisis support

### Dashboard (`/dashboard`)
- Personalized welcome message
- Quick action buttons
- Feedback submission form with star ratings
- Daily wellness tips
- Emergency contacts
- Recent activity

### Contact Counselor (`/contact_counselor`)
- Form to reach mental health professionals
- Urgency level selection
- Response time expectations
- Professional counselor information

### Resources (`/resources`)
- Comprehensive mental health articles
- Categorized content (Anxiety, Depression, Stress, etc.)
- Interactive tools
- External resource links

## 🔧 Configuration Options

### Environment Variables (`.env`)
```bash
# Flask Configuration
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True

# MongoDB Configuration
MONGODB_URI=mongodb://localhost:27017/
DB_NAME=mental_wellness
```

### Customization
- **Styling**: Modify `templates/base.html` for Tailwind CSS changes
- **Content**: Update resource articles in `templates/resources.html`
- **Emergency Contacts**: Edit contact information in templates

## 🧪 Testing

Run the test script to verify everything works:
```bash
python test_app.py
```

## 🚨 Emergency Support

The application includes emergency contact information:
- **National Suicide Prevention Lifeline**: 988
- **Crisis Text Line**: Text HOME to 741741
- **Emergency Services**: 911

## 📱 Features Overview

### ✅ Implemented Features
- [x] User registration and login
- [x] Secure password hashing
- [x] Dashboard with feedback form
- [x] Counselor contact system
- [x] Comprehensive resources library
- [x] Responsive design with Tailwind CSS
- [x] MongoDB database integration
- [x] Session management
- [x] Emergency contact information

### 🔮 Future Enhancements
- [ ] Real-time chat with counselors
- [ ] Mobile application
- [ ] Advanced analytics
- [ ] Video counseling sessions
- [ ] AI-powered assessments

## 🆘 Troubleshooting

### Common Issues

**Import Errors**
```bash
pip install -r requirements.txt
```

**MongoDB Connection Error**
- Check if MongoDB is running
- Verify connection string in `.env`
- Ensure network access (for Atlas)

**Port Already in Use**
```bash
# Change port in app.py
app.run(debug=True, port=5001)
```

**Template Not Found**
- Ensure all template files are in `templates/` directory
- Check file permissions

### Getting Help
1. Check the full [README.md](README.md)
2. Run `python test_app.py` for diagnostics
3. Verify MongoDB connection
4. Check Flask debug output

## 🎉 Success!

Once running, you'll have a fully functional Mental Wellness Portal with:
- Beautiful, responsive UI
- Secure user authentication
- Professional counselor contact system
- Comprehensive mental health resources
- Feedback and rating system
- Emergency support information

**Ready to help students with their mental wellness journey!** 🧠💙 