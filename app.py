from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex']
    
    try:
        # Find all matches using the provided regex pattern
        matches = re.findall(regex_pattern, test_string)
    except re.error:  # In case the regex pattern is invalid
        return render_template('index.html', error="Invalid Regex Pattern", test_string=test_string, regex=regex_pattern)
    
    # Check if there are matches
    if not matches:  # If matches list is empty
        message = "No matches found"
        matches = None  # Ensure matches is None so the list doesn't render
    else:
        message = None  # No need for message if matches are found
    
    return render_template('index.html', matches=matches, message=message, test_string=test_string, regex=regex_pattern)

@app.route('/email')
def email_page():
    return render_template('email.html')  # Redirect to a new page for email validation

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    is_valid = re.match(email_regex, email) is not None
    return render_template('email.html', email=email, is_valid=is_valid)


if __name__ == '__main__':
    app.run(debug=True)