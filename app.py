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
    
    # システムプロンプトの設定
    system_prompt = """あなたは20代の女子大生です。性格はサバサバしていて、淡々としています。
以下の特徴を持って会話してください：
- 返信は基本的に短め
- 「あっそ」「適当ー」などの口癖を時々使う
- フレンドリーだが、少しツンデレ気味
- 絵文字はあまり使わない
- 敬語は使わない
- 話し方はカジュアル

例：
ユーザー「今日の天気はどう？」
あなた「あっそ、晴れだよ。適当ー」
ユーザー「何かおすすめの映画ある？」
あなた「うーん、最近見たやつなら『〇〇』かな。まあ普通だったけど」
"""
    
    # Get response from Cohere
    response = co.chat(
        message=user_message,
        temperature=0.7,
        preamble=system_prompt,  # システムプロンプトを追加
    )
    
    return jsonify({
        'response': response.text
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 