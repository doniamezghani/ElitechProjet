from django.conf.urls import url
from. import views
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about$', views.about, name='about'),
	url(r'^contact$', views.contact, name='contact'),
	url(r'^coursedetail$', views.coursedetail, name='coursedetail'),
	url(r'^courses$', views.courses, name='courses'),
	url(r'^recuperationC', views.recuperationCours, name='recuperationC'),
	url(r'^recuperationChap', views.recuperationChapitre, name='recuperationChap'),
	url(r'^recuperationQ', views.recuperationQuestion, name='recuperationQ'),
	url(r'^recuperationQuiz', views.recuperationQuiz, name='recuperationQuiz'),
]