#!/usr/bin/env python
# coding: utf-8
# License: MIT
# Author: Chris Ward <chris@zeroknowledge.fm>
# Credits : https://github.com/MichaelSolati/typeform-python-examples/blob/master/webhooks/main.py
# Airtable Interface for ZKDB (Zero Knowledge Podcast DB)

__app_name__ = "webhooks"
__version__ = "0.1"
'''
0.1: 
'''

import json
import requests
import flask
import hashlib
from time import time

# Variables, feel free to change them
formURL = 'https://9lcje6jbgv1.typeform.com/to/eOCXPfIy'

# Message Board Handler
def webhooksMessageBoard(request: flask.Request):
  # We only accept POST and GET requests for our demo
  if request.method == 'POST':
    return post(request)
  elif request.method == 'GET':
    return get()
  else:
    flask.abort(405)

# Handle a POST request for our webhook demo
# Handles the webhook
def post(request: flask.Request):
  data = request.get_json()
  payload = {
  }

  # And let's ensure we actually have answers in our response
  if data is None or 'form_response' not in data.keys() or 'answers' not in data['form_response'].keys():
    flask.abort(400)

  # Simplify the data structure just a little bit
  formResponse = data['form_response']
  
  # post payload #{'event_id': ..., 'event_type': ..., # 'form_response': {
  #  'form_id', 'token', 'landed_at', 'submitted_at', 
  #  'definition': {  'id', 'ref', 'type', 'title', 'properties': {}} # } #}

  payload['email'] = formResponse['answers'][0]['email'].lower()

  payload['displayName'] = payload['email']
  payload['thumbnailUrl'] = 'https://api.adorable.io/avatars/285/%s.png' % payload['email']
  
  # Stringify our payload
  payload = json.dumps(payload)
  print ('POST payload received')
  return payload

def get():
  return flask.render_template('index.html', formURL=formURL)

app = flask.Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if flask.request.method == "GET":
        # This is for "ping" purposes only" not useful otherwise
        return "Webhook received!"

    if flask.request.method == "POST":
        return post(flask.request)

# Development
app.run(host='127.0.0.1', port=9000)
# Production - flask server isn't the same as nginx/apache...
#app.run(host='0.0.0.0', port=9000)
