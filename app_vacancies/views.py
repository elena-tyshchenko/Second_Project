from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class MainView(View):
    def get(self, request):
        return render(request, 'index.html')


class VacanciesView(View):
    def get(self, request):
        return render(request, 'vacancies.html')


class SpecializationView(View):
    def get(self, request, specialization):
        return render(request, 'vacancies.html')


class CompaniesView(View):
    def get(self, request, id):
        return render(request, 'company.html')


class VacancyView(View):
    def get(self, request, id):
        return render(request, 'vacancy.html')
