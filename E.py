import requests
import json
import pprint
custom_headers = {
                   'Accept': 'application/json',
                   'Content-Type': 'application/json'
                 };
true = True;
false = False;
def get(url, data = None):
  generic_call('get', url, data);

def post(url, data= None):
  generic_call('post', url, data);

def put(url, data= None):
  generic_call('put', url, data);

def generic_call(call, url, data):
  if data:
    response = getattr(requests, call)(url, json.dumps(data), headers = custom_headers)
  else:
    response = getattr(requests, call)(url, headers = custom_headers);
  print_response(response)

def print_response(response):
  pprint.pprint(response.content, width = 2, indent = 2);
