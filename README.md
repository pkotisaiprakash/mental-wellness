# Mental Wellness Portal for Students

A comprehensive web application designed to support student mental health and well-being through accessible resources, professional counseling connections, and educational materials.

## 🎯 Project Goals

- Help students access mental health resources
- Provide a platform to share concerns anonymously
- Connect students with mental health professionals
- Offer educational content about mental wellness
- Create a safe, supportive community for students

## 🛠️ Technology Stack

- **Frontend**: HTML, Tailwind CSS
- **Backend**: Python Flask
- **Database**: MongoDB
- **Authentication**: Flask-Login with bcrypt
- **Styling**: Tailwind CSS (CDN)

## ✨ Features

### 🔐 User Authentication
- Student registration and login
- Secure password hashing with bcrypt
- Session management with Flask-Login

### 🏠 Home Page
- Welcoming interface with clear navigation
- Quick access to key features
- Emergency contact information
- Statistics and testimonials

### 📊 Dashboard
- Personalized welcome message
- Quick action buttons
- Feedback submission form with star ratings
- Daily wellness tips
- Emergency contact information
- Recent activity tracking

### 💬 Counselor Contact & Support
- Form to reach mental health professionals
- Government support resources and helplines
- National crisis resources (988, Crisis Text Line)
- SAMHSA and CDC mental health resources
- Additional specialized support lines
- Urgency level selection
- Response time expectations
- Professional counselor information
- Emergency support resources

### 📚 Resources Library
- Comprehensive mental health articles
- Categorized content (Anxiety, Depression, Stress, etc.)
- Interactive tools (Mood Tracker, Goal Setter, etc.)
- External resource links
- Search and filter functionality

### 📝 Feedback System
- Multi-category feedback submission
- Star rating system
- Anonymous feedback options
- Admin dashboard for feedback review

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7+
- MongoDB (local or Atlas)
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd mental-wellness-portal
```

### Step 2: Set Up Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
1. Copy `env_example.txt` to `.env`
2. Update the configuration:
   ```bash
   # For local MongoDB
   MONGODB_URI=mongodb://localhost:27017/
   
   # For MongoDB Atlas
   MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/mental_wellness?retryWrites=true&w=majority
   
   SECRET_KEY=your-secret-key-here
   ```

### Step 5: Set Up MongoDB

#### Option A: Local MongoDB
1. Install MongoDB Community Edition
2. Start MongoDB service
3. Create database: `mental_wellness`

#### Option B: MongoDB Atlas
1. Create a free MongoDB Atlas account
2. Create a new cluster
3. Get your connection string
4. Update `.env` file with the connection string

### Step 6: Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 📁 Project Structure

```
mental-wellness-portal/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── env_example.txt        # Environment variables template
├── README.md             # Project documentation
└── templates/            # HTML templates
    ├── base.html         # Base template with navigation
    ├── index.html        # Home page
    ├── register.html     # User registration
    ├── login.html        # User login
    ├── dashboard.html    # User dashboard
    ├── contact_counselor.html  # Counselor contact & support page
    └── resources.html    # Mental health resources
```

## 🔧 Configuration

### Environment Variables
- `SECRET_KEY`: Flask secret key for session management
- `MONGODB_URI`: MongoDB connection string
- `FLASK_ENV`: Flask environment (development/production)
- `FLASK_DEBUG`: Enable/disable debug mode

### Database Collections
- `users`: User accounts and authentication data
- `feedback`: User feedback and ratings
- `counselor_requests`: Counselor contact requests

## 🎨 Customization

### Styling
The application uses Tailwind CSS via CDN. To customize:
1. Modify the Tailwind configuration in `templates/base.html`
2. Update color schemes and styling classes
3. Add custom CSS as needed

### Content
- Update resource articles in `templates/resources.html`
- Modify wellness tips in `templates/dashboard.html`
- Customize emergency contact information

## 🔒 Security Features

- Password hashing with bcrypt
- Session-based authentication
- CSRF protection (Flask-WTF)
- Input validation and sanitization
- Secure MongoDB connections

## 🚨 Emergency Support

The application includes emergency contact information:
- National Suicide Prevention Lifeline: 988
- Crisis Text Line: Text HOME to 741741
- Emergency Services: 911

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For technical support or questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

## 🔮 Future Enhancements

- Real-time chat with counselors
- Mobile application
- Advanced analytics and reporting
- Integration with university systems
- Peer support groups
- Video counseling sessions
- AI-powered mental health assessments

---

**Important**: This application is designed for educational purposes and should not replace professional mental health care. Always seek professional help for serious mental health concerns. 