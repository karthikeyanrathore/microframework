#!/usr/bin/env python3
print("Hello Microframework")

class Microframework(object):
  
  # if secret key is set, cryptographic components can use this
  # to sign cookies.
  # secure cookie
  secret_key = None
  
  # session cookie
  # https://www.techopedia.com/definition/4910/session-cookie
  session_cookie_name = 'session'
  
  def __init__(self):
    self.view_functions = {}
  
  def run(self):
    print('running microframework application here')
  
  def __call__(self):
    print("call function starts here")


if __name__ == "__main__":
  import os 

  # Flask application
  if os.getenv('FLASK') is not None:
    # checking flask behaviour
    from flask import Flask
    app = Flask(__name__)
    # start WSGI server
    app.run()
  
  # Microframework application
  elif os.getenv('MICROFRAMEWORK') is not None:
    app = Microframework()
    app.run()

  # Missing  ENV var
  else:
    print("ENV variables missing")
    print("FLASK=1 ./microframework.py")
    print("MICROFRAMEWORK=1 ./microframework.py")
