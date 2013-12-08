#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#from bottle import route, run

from bottle import * # or route
#from function import *

debug(True)

@get('/') # or @route(’/login’) 
@get('/login') # or @route(’/login’) 
def login():
	return '''
	<form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
	</form> '''


def check_logib(self, username, password):
	if(username == "admin" and password == "admin"):
		return True
	else:
		return False


@post('/login') # or @route(’/login’, method=’POST’) 
def do_login():
	username = request.forms.get('username') 
	password = request.forms.get('password') 
	if check_login(username, password):
		return "<p>Your login information was correct.</p>" 
	else:
		return "<p>Login failed.</p>"

@error(404)
def error404(error):
	return 'Nothing here, sorry'


run(host='localhost', port=8080, debug=True)
