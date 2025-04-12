from flask import Flask, request, render_template_string, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>SINI MAS - Feedback</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2c3e50;
            }
            form {
                margin-top: 20px;
            }
            textarea {
                width: 100%;
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ddd;
                border-radius: 4px;
                min-height: 120px;
            }
            input[type="text"] {
                width: 100%;
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
            button {
                padding: 10px 15px;
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            button:hover {
                background-color: #2980b9;
            }
            .message {
                margin-top: 20px;
                padding: 15px;
                border-radius: 4px;
                background-color: #f9f9f9;
            }
            label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>SINI MAS - Feedback System</h1>
            <p>We value your feedback! Please let us know your thoughts.</p>
            
            <form action="/submit" method="post">
                <div>
                    <label for="name">Your Name:</label>
                    <input type="text" id="name" name="name" placeholder="Enter your name" required>
                </div>
                
                <div>
                    <label for="email">Your Email:</label>
                    <input type="text" id="email" name="email" placeholder="Enter your email" required>
                </div>
                
                <div>
                    <label for="feedback">Your Feedback:</label>
                    <textarea id="feedback" name="feedback" placeholder="Please share your feedback with us..." required></textarea>
                </div>
                
                <button type="submit">Submit Feedback</button>
            </form>
        </div>
    </body>
    </html>
    ''')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    feedback = request.form.get('feedback', '')
    
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>SINI MAS - Thank You</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2c3e50;
            }
            .message {
                margin-top: 20px;
                padding: 15px;
                border-radius: 4px;
                background-color: #f9f9f9;
            }
            .back {
                display: inline-block;
                margin-top: 20px;
                padding: 8px 15px;
                background-color: #3498db;
                color: white;
                text-decoration: none;
                border-radius: 4px;
            }
            .back:hover {
                background-color: #2980b9;
            }
            .feedback-details {
                margin-top: 20px;
                border-top: 1px solid #eee;
                padding-top: 15px;
            }
            .feedback-details p {
                margin: 5px 0;
            }
            .feedback-details strong {
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Thank You for Your Feedback!</h1>
            <div class="message">
                Hello ''' + name + ''', thank you for submitting your feedback! Our team will review it shortly.
            </div>
            
            <a href="/" class="back">Back to Feedback Form</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=False) 