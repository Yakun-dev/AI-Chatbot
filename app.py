from flask import Flask, render_template, request, jsonify, send_from_directory
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

@app.route('/static/service-worker.js')
def service_worker():
    response = app.make_response(send_from_directory('static', 'service-worker.js'))
    response.headers['Content-Type'] = 'application/javascript'
    return response

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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 