from flask import Flask, render_template, request, jsonify
import cohere
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
co = cohere.Client(os.getenv('COHERE_API_KEY'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    # Get response from Cohere
    response = co.chat(
        message=user_message,
        temperature=0.7,
    )
    
    return jsonify({
        'response': response.text
    })

if __name__ == '__main__':
    app.run(debug=True) 