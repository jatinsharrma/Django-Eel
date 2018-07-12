from django.shortcuts import render
import eel
import random

# Create your views here.
eel.init('examples/templates/examples')

def hello_page(request):
	return render(request, 'examples/hello.html')

@eel.expose
def say_hello_py(x):
	print('Hello from %s' % x)
	eel.say_hello_js('Python3 and Django World!')

def callbacks_page(request):
	eel.js_random()(print_num)
	return render(request, 'examples/callbacks.html')

@eel.expose
def py_random():
	return random.random()

def print_num(n):
    print('Got this from Javascript:', n)

