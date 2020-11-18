from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def sendmail_view(request):
	email=request.POST.get('email')
	subject=request.POST.get('subject')
	message=request.POST.get('message')
	

	print("*************************")
	print(message.split(','))
	print("*************************")

	send_mail(subject,'','Welcome User',[email],fail_silently=False,html_message='<h1>'+message+'</h1>')
	
	return render(request,'emailapp/index.html')