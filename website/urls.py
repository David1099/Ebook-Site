from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name ="index"),
	path('FAQ.html', views.FAQ, name = "FAQ"),
	path('Thankyou.html', views.Thankyou, name = "Thankyou"),
]