#!/usr/bin/env python3
"""
Simple test script to verify the Mental Wellness Portal application
"""

import os
import sys

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        from flask import Flask
        print("✅ Flask imported successfully")
    except ImportError as e:
        print(f"❌ Flask import failed: {e}")
        return False
    
    try:
        from pymongo import MongoClient
        print("✅ PyMongo imported successfully")
    except ImportError as e:
        print(f"❌ PyMongo import failed: {e}")
        return False
    
    try:
        import bcrypt
        print("✅ bcrypt imported successfully")
    except ImportError as e:
        print(f"❌ bcrypt import failed: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv imported successfully")
    except ImportError as e:
        print(f"❌ python-dotenv import failed: {e}")
        return False
    
    return True

def test_app_creation():
    """Test if the Flask app can be created"""
    print("\nTesting Flask app creation...")
    
    try:
        # Temporarily set environment variables for testing
        os.environ['SECRET_KEY'] = 'test-secret-key'
        os.environ['MONGODB_URI'] = 'mongodb://localhost:27017/'
        
        # Import the app
        from app import app
        print("✅ Flask app created successfully")
        return True
    except Exception as e:
        print(f"❌ Flask app creation failed: {e}")
        return False

def test_templates():
    """Test if all template files exist"""
    print("\nTesting template files...")
    
    required_templates = [
        'templates/base.html',
        'templates/index.html',
        'templates/register.html',
        'templates/login.html',
        'templates/dashboard.html',
        'templates/contact_counselor.html',
        'templates/resources.html'
    ]
    
    missing_templates = []
    for template in required_templates:
        if os.path.exists(template):
            print(f"✅ {template} exists")
        else:
            print(f"❌ {template} missing")
            missing_templates.append(template)
    
    return len(missing_templates) == 0

def main():
    """Main test function"""
    print("🧠 Mental Wellness Portal - Application Test")
    print("=" * 50)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed. Please install dependencies:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    
    # Test app creation
    if not test_app_creation():
        print("\n❌ App creation failed. Check your configuration.")
        sys.exit(1)
    
    # Test templates
    if not test_templates():
        print("\n❌ Template tests failed. Check template files.")
        sys.exit(1)
    
    print("\n🎉 All tests passed!")
    print("\nThe application is ready to run.")
    print("To start the server, run: python app.py")

if __name__ == "__main__":
    main() 