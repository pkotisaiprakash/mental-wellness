#!/usr/bin/env python3
"""
Setup script for Mental Wellness Portal
This script helps configure the application and create necessary files.
"""

import os
import secrets
import sys

def create_env_file():
    """Create .env file with configuration"""
    env_content = f"""# Flask Configuration
SECRET_KEY={secrets.token_hex(32)}
FLASK_ENV=development
FLASK_DEBUG=True

# MongoDB Configuration
# For local MongoDB:
MONGODB_URI=mongodb://localhost:27017/

# For MongoDB Atlas (replace with your connection string):
# MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/mental_wellness?retryWrites=true&w=majority

# Database Name
DB_NAME=mental_wellness
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("✅ Created .env file with default configuration")

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import flask
        import pymongo
        import bcrypt
        import dotenv
        print("✅ All required packages are available")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def create_directories():
    """Create necessary directories"""
    directories = ['logs', 'uploads']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✅ Created directory: {directory}")

def main():
    """Main setup function"""
    print("🧠 Mental Wellness Portal Setup")
    print("=" * 40)
    
    # Check if .env already exists
    if os.path.exists('.env'):
        print("⚠️  .env file already exists. Skipping creation.")
    else:
        create_env_file()
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Configure MongoDB (local or Atlas)")
    print("2. Update .env file with your MongoDB connection string")
    print("3. Run: python app.py")
    print("4. Open http://localhost:5000 in your browser")
    
    print("\n📚 For detailed instructions, see README.md")

if __name__ == "__main__":
    main() 