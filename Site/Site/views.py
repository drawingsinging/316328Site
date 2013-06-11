from django.http import HttpResponse

def hello(response):
	return HttpResponse('hello world')