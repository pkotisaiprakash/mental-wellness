from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from pymongo import MongoClient
from bson import ObjectId
import bcrypt
import os
from datetime import datetime, timezone
from dotenv import load_dotenv
import random

load_dotenv()




app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')
app.config['SESSION_TYPE'] = 'filesystem'



client = ['mongodb+srv://mentalUser:<57XRTkXQJAtUgETz>@cluster1.64hb1bb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1']

db = client['mental_wellness']
users_collection = db['users']
feedback_collection = db['feedback']
counselor_requests_collection = db['counselor_requests']
videos_collection = db['videos']
playlists_collection = db['playlists']
mood_entries_collection = db['mood_entries']
goals_collection = db['goals']

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Sample video data
SAMPLE_VIDEOS = [
    {
        'title': '5-Minute Meditation for Stress Relief',
        'description': 'Quick meditation techniques perfect for busy students',
        'duration': '5:30',
        'category': 'mindfulness',
        'difficulty': 'beginner',
        'thumbnail': '🧘',
        'video_url': 'https://www.youtube.com/embed/inpok4MKVLM',  # Good meditation video
        'views': 15420,
        'likes': 892
    },
    {
        'title': 'Better Sleep Habits for Students',
        'description': 'Science-backed tips for improving sleep quality',
        'duration': '8:15',
        'category': 'sleep',
        'difficulty': 'intermediate',
        'thumbnail': '😴',
        'video_url': 'https://www.youtube.com/embed/1nZEdqcGVzo',  # Sleep tips
        'views': 8920,
        'likes': 456
    },
    {
        'title': 'How to Build Mental Resilience',
        'description': 'Strategies to bounce back from academic stress',
        'duration': '12:45',
        'category': 'resilience',
        'difficulty': 'advanced',
        'thumbnail': '💪',
        'video_url': 'https://www.youtube.com/embed/WWloIAQpMcQ',  # Resilience
        'views': 23410,
        'likes': 1234
    },
    {
        'title': 'Anxiety Management Techniques',
        'description': 'Practical strategies for managing anxiety in daily life',
        'duration': '10:20',
        'category': 'anxiety',
        'difficulty': 'intermediate',
        'thumbnail': '😰',
        'video_url': 'https://www.youtube.com/embed/ZToicYcHIOU',  # Anxiety
        'views': 18750,
        'likes': 987
    },
    {
        'title': 'Self-Care for Busy Students',
        'description': 'Simple self-care practices that fit into your schedule',
        'duration': '7:30',
        'category': 'self-care',
        'difficulty': 'beginner',
        'thumbnail': '💖',
        'video_url': 'https://www.youtube.com/embed/6kJgTouHHeE',  # Self-care
        'views': 12340,
        'likes': 678
    },
    {
        'title': 'Time Management for Mental Health',
        'description': 'Balancing academics and wellness effectively',
        'duration': '9:45',
        'category': 'stress',
        'difficulty': 'intermediate',
        'thumbnail': '⏰',
        'video_url': 'https://www.youtube.com/embed/oTugjssqOT0',  # Time management
        'views': 9870,
        'likes': 543
    }
]

# Sample playlists
SAMPLE_PLAYLISTS = [
    {
        'title': 'Anxiety Management Series',
        'description': 'Complete guide to managing anxiety for students',
        'video_count': 6,
        'total_duration': '45 minutes',
        'videos': [
            'Understanding Anxiety Triggers',
            'Breathing Techniques for Panic Attacks',
            'Cognitive Behavioral Therapy Basics',
            'Progressive Muscle Relaxation',
            'Mindfulness for Anxiety',
            'Building a Support System'
        ]
    },
    {
        'title': 'Student Life Balance',
        'description': 'Achieving balance between academics and personal life',
        'video_count': 8,
        'total_duration': '60 minutes',
        'videos': [
            'Time Management Strategies',
            'Setting Healthy Boundaries',
            'Social Life vs Academic Life',
            'Dealing with FOMO',
            'Self-Care for Students',
            'Building Healthy Relationships',
            'Financial Stress Management',
            'Career Planning Without Overwhelm'
        ]
    }
]

class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data['_id'])
        self.name = user_data['name']
        self.email = user_data['email']
        self.role = user_data.get('role', 'student')

@login_manager.user_loader
def load_user(user_id):
    try:
        # Convert string user_id back to ObjectId for MongoDB query
        user_data = users_collection.find_one({'_id': ObjectId(user_id)})
        if user_data:
            return User(user_data)
    except Exception as e:
        print(f"Error loading user: {e}")
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Check if user already exists
        if users_collection.find_one({'email': email}):
            flash('Email already registered!', 'error')
            return render_template('register.html')
        
        # Hash password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        # Create user
        user_data = {
            'name': name,
            'email': email,
            'password': hashed_password,
            'opassword':password,
            'role': 'student',
            'created_at': datetime.now(timezone.utc)
        }
        
        result = users_collection.insert_one(user_data)
        print(f"User registered with ID: {result.inserted_id}")
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        print(f"Login attempt for email: {email}")
        
        user_data = users_collection.find_one({'email': email})
        
        if user_data:
            print(f"User found: {user_data['name']}")
            if bcrypt.checkpw(password.encode('utf-8'), user_data['password']):
                user = User(user_data)
                login_user(user)
                print(f"User logged in successfully: {user.name}")
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                print("Password check failed")
                flash('Invalid email or password!', 'error')
        else:
            print("User not found")
            flash('Invalid email or password!', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    print(f"Dashboard accessed by: {current_user.name}")
    return render_template('dashboard.html')

@app.route('/contact_counselor', methods=['GET', 'POST'])
@login_required
def contact_counselor():
    """Contact counselor and access government support & mental health helplines"""
    if request.method == 'POST':
        subject = request.form['subject']
        message = request.form['message']
        urgency = request.form['urgency']
        
        request_data = {
            'user_id': current_user.id,
            'user_name': current_user.name,
            'user_email': current_user.email,
            'subject': subject,
            'message': message,
            'urgency': urgency,
            'status': 'pending',
            'created_at': datetime.now(timezone.utc)
        }
        
        counselor_requests_collection.insert_one(request_data)
        flash('Your request has been sent to counselors. You will be contacted soon!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('contact_counselor.html')

@app.route('/submit_feedback', methods=['POST'])
@login_required
def submit_feedback():
    rating = request.form['rating']
    feedback_text = request.form['feedback']
    category = request.form['category']
    
    feedback_data = {
        'user_id': current_user.id,
        'user_name': current_user.name,
        'rating': int(rating),
        'feedback': feedback_text,
        'category': category,
        'created_at': datetime.now(timezone.utc)
    }
    
    feedback_collection.insert_one(feedback_data)
    flash('Thank you for your feedback!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/videos')
def videos():
    # Get videos from database or use sample data
    videos = list(videos_collection.find()) if videos_collection.count_documents({}) > 0 else SAMPLE_VIDEOS
    print(f"Videos route accessed. Found {len(videos)} videos")
    print(f"Sample videos: {SAMPLE_VIDEOS[:2]}")  # Print first 2 videos for debugging
    return render_template('videos.html', videos=videos)

@app.route('/video/<video_id>')
def video_detail(video_id):
    # Get video details from database or sample data
    video = videos_collection.find_one({'_id': ObjectId(video_id)}) if ObjectId.is_valid(video_id) else None
    if not video:
        # Use sample video for demo
        video = SAMPLE_VIDEOS[0] if SAMPLE_VIDEOS else None
    
    return render_template('video_detail.html', video=video)

@app.route('/playlists')
def playlists():
    # Get playlists from database or use sample data
    playlists = list(playlists_collection.find()) if playlists_collection.count_documents({}) > 0 else SAMPLE_PLAYLISTS
    return render_template('playlists.html', playlists=playlists)

@app.route('/api/videos')
def api_videos():
    """API endpoint for video data"""
    category = request.args.get('category')
    videos = SAMPLE_VIDEOS
    
    if category:
        videos = [v for v in videos if v['category'] == category]
    
    return jsonify(videos)

@app.route('/api/playlists')
def api_playlists():
    """API endpoint for playlist data"""
    return jsonify(SAMPLE_PLAYLISTS)

@app.route('/watch/<video_id>')
def watch_video(video_id):
    """Video player page"""
    # In a real application, you would fetch video details from database
    video = next((v for v in SAMPLE_VIDEOS if str(SAMPLE_VIDEOS.index(v)) == video_id), SAMPLE_VIDEOS[0])
    return render_template('watch.html', video=video)

@app.route('/mood_tracker')
@login_required
def mood_tracker():
    """Mood tracker page"""
    from datetime import timedelta
    week_ago = datetime.now(timezone.utc) - timedelta(days=7)
    mood_entries = list(mood_entries_collection.find({
        'user_id': current_user.id,
        'created_at': {'$gte': week_ago}
    }).sort('created_at', -1))
    mood_analysis = analyze_mood_patterns(mood_entries)
    motivational_msg = session.pop('motivational_msg', None)
    return render_template('mood_tracker.html', mood_entries=mood_entries, mood_analysis=mood_analysis, motivational_msg=motivational_msg)

def analyze_mood_patterns(mood_entries):
    """Analyze mood entries and generate personalized suggestions"""
    if not mood_entries:
        return {
            'average_mood': None,
            'mood_trend': 'neutral',
            'suggestions': [
                "Start tracking your mood daily to identify patterns",
                "Try different activities and see how they affect your mood",
                "Set a reminder to check in with yourself regularly"
            ],
            'insights': "Begin your mood tracking journey to better understand your emotional patterns."
        }
    
    # Calculate average mood
    total_mood = sum(entry['mood_level'] for entry in mood_entries)
    average_mood = total_mood / len(mood_entries)
    
    # Determine mood trend
    if len(mood_entries) >= 2:
        recent_mood = mood_entries[0]['mood_level']
        older_mood = mood_entries[-1]['mood_level']
        if recent_mood > older_mood:
            mood_trend = 'improving'
        elif recent_mood < older_mood:
            mood_trend = 'declining'
        else:
            mood_trend = 'stable'
    else:
        mood_trend = 'neutral'
    
    # Generate personalized suggestions based on mood level and trend
    suggestions = []
    insights = ""
    
    if average_mood <= 2:  # Low mood
        suggestions.extend([
            "Consider reaching out to a counselor or trusted friend",
            "Try gentle physical activity like walking or stretching",
            "Practice deep breathing exercises for 5-10 minutes",
            "Listen to calming music or nature sounds",
            "Write down three things you're grateful for today"
        ])
        insights = "Your mood has been consistently low. Remember that it's okay to ask for help and that difficult emotions are temporary."
        
    elif average_mood <= 3:  # Neutral to slightly low
        suggestions.extend([
            "Try a new hobby or activity you've been curious about",
            "Connect with friends or family members",
            "Spend time outdoors in nature",
            "Practice mindfulness or meditation",
            "Set small, achievable goals for the day"
        ])
        insights = "Your mood has been moderate. Small positive changes can make a big difference in how you feel."
        
    elif average_mood <= 4:  # Good mood
        suggestions.extend([
            "Build on your positive momentum with new challenges",
            "Share your good mood with others",
            "Document what's working well for you",
            "Set goals that align with your current energy",
            "Practice gratitude to maintain your positive outlook"
        ])
        insights = "Great job maintaining a positive mood! Keep doing what's working for you."
        
    else:  # Excellent mood
        suggestions.extend([
            "Use your high energy to help others",
            "Document your successful strategies for future reference",
            "Set ambitious but realistic goals",
            "Share your positive experiences with friends",
            "Practice self-care to maintain your excellent state"
        ])
        insights = "Excellent! You're in a great place. Use this energy to build lasting positive habits."
    
    # Add trend-specific suggestions
    if mood_trend == 'declining':
        suggestions.extend([
            "Consider what might be causing the decline in your mood",
            "Reach out to your support network",
            "Review your recent activities and identify potential stressors",
            "Practice self-compassion - mood fluctuations are normal"
        ])
        insights += " Your mood has been trending downward. This is a good time to be extra kind to yourself."
    elif mood_trend == 'improving':
        suggestions.extend([
            "Celebrate your progress and positive changes",
            "Identify what's helping and continue those practices",
            "Share your improvement with supportive people",
            "Use this momentum to build healthy habits"
        ])
        insights += " Your mood has been improving - great work!"
    
    # Add time-based suggestions
    if len(mood_entries) >= 3:
        suggestions.append("You're building a great habit of mood tracking!")
    
    return {
        'average_mood': round(average_mood, 1),
        'mood_trend': mood_trend,
        'suggestions': suggestions[:6],  # Limit to 6 suggestions
        'insights': insights,
        'total_entries': len(mood_entries),
        'days_tracked': len(set(entry['created_at'].date() for entry in mood_entries))
    }

@app.route('/submit_mood', methods=['POST'])
@login_required
def submit_mood():
    """Submit a new mood entry"""
    mood_level = request.form['mood_level']
    mood_note = request.form.get('mood_note', '')
    
    mood_data = {
        'user_id': current_user.id,
        'user_name': current_user.name,
        'mood_level': int(mood_level),
        'mood_note': mood_note,
        'created_at': datetime.now(timezone.utc)
    }
    
    mood_entries_collection.insert_one(mood_data)
    # Motivational messages by mood level
    mood_level = int(mood_level)
    motivational_msgs = {
        1: [
            "It's okay to have tough days. Remember, you are stronger than you think!",
            "Reach out to someone you trust. You're not alone.",
            "Take a deep breath and be kind to yourself today."
        ],
        2: [
            "Every step forward counts, no matter how small.",
            "Try to do one thing you enjoy today.",
            "You are making progress, even if it doesn't feel like it."
        ],
        3: [
            "Keep going! Balance is key, and you're doing your best.",
            "Take a moment to appreciate yourself.",
            "A little self-care goes a long way."
        ],
        4: [
            "Great job! Celebrate your wins, big or small.",
            "Share your positive energy with someone today!",
            "Keep up the good work and stay motivated!"
        ],
        5: [
            "Amazing! Spread your happiness and inspire others.",
            "Keep shining and enjoy your day!",
            "Your positivity is contagious!"
        ]
    }
    msg = random.choice(motivational_msgs.get(mood_level, ["Keep going, you're doing great!"]))
    session['motivational_msg'] = msg
    flash('Mood entry saved successfully!', 'success')
    return redirect(url_for('mood_tracker'))

@app.route('/goals')
@login_required
def goals():
    """Goals page"""
    # Get user's goals
    user_goals = list(goals_collection.find({
        'user_id': current_user.id
    }).sort('created_at', -1))
    
    return render_template('goals.html', goals=user_goals)

@app.route('/add_goal', methods=['POST'])
@login_required
def add_goal():
    """Add a new goal"""
    title = request.form['title']
    description = request.form.get('description', '')
    target_date = request.form.get('target_date', '')
    category = request.form.get('category', 'general')
    
    goal_data = {
        'user_id': current_user.id,
        'user_name': current_user.name,
        'title': title,
        'description': description,
        'target_date': target_date,
        'category': category,
        'status': 'active',
        'progress': 0,
        'created_at': datetime.now(timezone.utc)
    }
    
    goals_collection.insert_one(goal_data)
    flash('Goal added successfully!', 'success')
    return redirect(url_for('goals'))

@app.route('/update_goal_progress', methods=['POST'])
@login_required
def update_goal_progress():
    """Update goal progress"""
    goal_id = request.form['goal_id']
    progress = int(request.form['progress'])
    
    goals_collection.update_one(
        {'_id': ObjectId(goal_id), 'user_id': current_user.id},
        {'$set': {'progress': progress}}
    )
    
    return jsonify({'success': True})

if __name__ == "__main__":
    app.run()

