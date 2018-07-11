from django.shortcuts import render
import eel

# Create your views here.
eel.init('examples/templates/examples')

@eel.expose
def say_hello_py(request):
	#print('Hello from %s' % x)
	eel.say_hello_js('Python3 and Django World!')
	return render(request, 'examples/hello.html')