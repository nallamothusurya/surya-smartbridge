# app.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the Home page
@app.route('/')
def home():
    return render_template('index.html', active_page='home')

# Route for the About page
@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

# Route for the Dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', active_page='dashboard')

# Route for the Story page
@app.route('/story')
def story():
    return render_template('story.html', active_page='story')

# Route for the Contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process the form data
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # For this example, we'll just print it to the console.
        # In a real application, you would email this or save it to a database.
        print(f"New Contact Form Submission:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        
        # You could redirect to a 'thank you' page or back to the contact page
        return redirect(url_for('contact'))
        
    return render_template('contact.html', active_page='contact')

if __name__ == '__main__':
    app.run(debug=True)