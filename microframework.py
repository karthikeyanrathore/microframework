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
    # debug option
    self.debug = None
    # route these functions
    self.view_functions = {}
  
  def run(self, host='localhost', port=5000, **options):
    # https://werkzeug.palletsprojects.com/en/2.2.x/tutorial/#step-2-the-base-structure
    # run application on local developement server 
    from werkzeug.serving import run_simple
    if 'debug' in options:
      self.debug = options.pop('debug')
    options.setdefault('use_debugger', self.debug)
    options.setdefault('use_reloader', self.debug)
    return run_simple(host, port, self, **options)
  
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
    if os.getenv('DEBUG') is not None:
      app.run(debug=True)
    # run without debug mode.
    app.run()

  # Missing  ENV var
  else:
    print("ENV variables missing")
    print("FLASK=1 ./microframework.py")
    print("MICROFRAMEWORK=1 ./microframework.py")
