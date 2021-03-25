from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
	return render(request, 'index.html', {})

def FAQ(request):
	return render(request, 'FAQ.html', {})


def Thankyou(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

	 send_mail(
                        message_name + ' ' +  message_email,
                        message,
                        message_email,
                        ['lxdavidxl639@gmail.com'],
                        )



		return render(request, 'Thankyou.html',{'message_name':message_name})

	else:
		return render(request, 'index.html', {})