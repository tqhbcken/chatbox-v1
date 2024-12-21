from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Store conversation history
conversation_history = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    if data is None:
        return jsonify({'error': 'Invalid JSON received'}), 400
    user_message = data.get('message', '').lower()
    
    # Improved response logic
    if 'hello' in user_message or 'hi' in user_message:
        bot_response = "Hi there! How can I assist you today?"
    elif 'how are you' in user_message:
        bot_response = "I'm doing well, thank you for asking! How can I help you?"
    elif 'bye' in user_message or 'goodbye' in user_message:
        bot_response = "Goodbye! Have a great day!"
    else:
        bot_response = "I understand you said: '" + user_message + "'. How can I help you with that?"
    
    # Store the conversation
    conversation_history.append({"user": user_message, "bot": bot_response})
    
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    # Use this for local development
    app.run(debug=True)
    
    # Use this when deploying to production
    # app.run(host='0.0.0.0', port=8080)
