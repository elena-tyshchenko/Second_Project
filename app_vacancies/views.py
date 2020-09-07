from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class MainView(View):
    def get(self, request):
        return HttpResponse("Это главная")


class VacanciesView(View):
    def get(self, request):
        return HttpResponse("Здесь будет список вакансий")


class SpecializationView(View):
    def get(self, request, specialization):
        return HttpResponse("Здесь будет список вакансий по специализации")


class CompaniesView(View):
    def get(self, request, id):
        return HttpResponse("Здесь будет карточка компании")


class VacancyView(View):
    def get(self, request, id):
        return HttpResponse("Здесь будет описание вакансии")
