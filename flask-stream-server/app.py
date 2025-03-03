#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
from flask import Flask, Response, json, render_template, request
from ollama import Client


app = Flask(__name__)

# 流式数据的生成器函数
def process_message(message):
    ollama_host = os.environ.get('OLLAMA_HOST')
    ollama_model = os.environ.get('OLLAMA_MODEL')
    
    client = Client(host=ollama_host)
    message = {
        'role': 'user',
        'content': message,
    }
    messages = [message]
    stream = client.chat(model=ollama_model, messages=messages, stream=True)
    for chunk in stream:
        print(chunk)
        yield f"data: {json.dumps({'content': chunk.message.content})}\n\n"
    

# 流式接口路由
@app.route('/stream', methods=['POST'])
def stream():
    data = json.loads(request.get_data(as_text=True))
    message = data.get('message')
    return Response(
        process_message(message),  # 调用生成器函数
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache'
            }
        )

# 前端页面路由
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)