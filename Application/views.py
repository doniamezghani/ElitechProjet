# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

import requests
from django.shortcuts import render


def recuperation(request):
    json_data = open('/jsonFile/course.json')
    data1 = json.load(json_data)
    data2 = json.dumps(data1)
    json_data.close()
    return data1
def recuperationCours(request):
    responseCours = requests.get("http://dev-training.elitech.fr/wp-json/wplms/v1/course")
    return responseCours
def recuperationChapitre(request):
    responseChapitre = requests.get("http://dev-training.elitech.fr/wp-json/wplms/v1/unit")
    return responseChapitre
def recuperationQuiz(request):
    responseQuiz = requests.get("http://dev-training.elitech.fr/wp-json/wplms/v1/quiz")
    return responseQuiz
def recuperationQuestion(request):
    responseQuestion = requests.get("http://dev-training.elitech.fr/wp-json/wplms/v1/question")
    return responseQuestion

def index(request):

    return render(request, 'index-4.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def coursedetail(request):
    return render(request, 'course-detail.html')
def courses(request):
    return render(request, 'courses.html')

