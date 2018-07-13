from django.shortcuts import render
import django_eel as eel
import os, random

# Create your views here.
eel.init('examples/templates/examples')

###########################
# Hello example
###########################
def hello_page(request):
	return render(request, 'examples/hello.html')

@eel.expose
def say_hello_py(x):
	print('Hello from %s' % x)
	eel.say_hello_js('Python3 and Django World!')

###########################
# Callbacks example
###########################
def callbacks_page(request):
	eel.js_random()(print_num)
	return render(request, 'examples/callbacks.html')

@eel.expose
def py_random():
	return random.random()

def print_num(n):
    print('Got this from Javascript:', n)

###########################
# Sync_Callbacks example
###########################
def sync_callbacks_page(request):
	n = eel.js_random()()
	print('Got this from Javascript:', n)
	return render(request, 'examples/sync_callbacks.html')

###########################
# File_Access example
###########################
@eel.expose
def pick_file(folder):
	if os.path.isdir(folder):
		return random.choice(os.listdir(folder))
	else:
		return 'Not valid folder'

def file_access_page(request):
	return render(request, 'examples/file_access.html')

###########################
# Input example
###########################
@eel.expose
def handleinput(x):
    print('%s' % x)

def input_page(request):
	eel.say_hello_js('connected!')
	return render(request, 'examples/main.html')

###########################
# Open local page
###########################

eel.start('examples/hello', size=(300, 200))
#eel.start('examples/callbacks', size=(300, 200))
#eel.start('examples/sync_callbacks', size=(300, 200))
#eel.start('examples/file_access', size=(300, 200))
#eel.start('examples/input', size=(300, 200))