#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
from ollama import Client

if __name__ == '__main__':
    ollama_host = os.environ.get('OLLAMA_HOST')
    ollama_model = os.environ.get('OLLAMA_MODEL')
    
    client = Client(host=ollama_host)
    
    messages = []
    message = {
        'role': 'user',
        'content': '请你用Python编写一个功能强大的爬虫，功能至少要有图片爬取等',
    }
    messages.append(message)
    
    response = client.chat(model=ollama_model, messages=messages)
    messages.append(response.get('message'))
    
    message = {
        'role': 'user',
        'content': '使用其他爬虫工具库',
    }
    messages.append(message)
    
    response = client.chat(model=ollama_model, messages=messages)
    # print(response.get('message').get('content'))
    print(response)
