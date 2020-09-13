from django.http import Http404, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View

from app_vacancies.models import Company, Specialty, Vacancy


class MainView(View):
    def get(self, request):
        specialties = Specialty.objects.all()
        companies = Company.objects.all()
        context = {
            'specialties': specialties,
            'companies': companies,
        }
        return render(request, 'index.html', context=context)


class VacanciesView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        context = {
            'vacancies': vacancies,
            'title': 'Все вакансии',
        }

        return render(request, 'vacancies.html', context=context)


class SpecializationView(View):
    def get(self, request, specialization):
        try:
            category = Specialty.objects.get(code=specialization)
        except Specialty.DoesNotExist:
            raise Http404
        vacancies = Vacancy.objects.filter(specialty=category)
        context = {
            'vacancies': vacancies,
            'title': category.title,
        }
        return render(request, 'vacancies.html', context=context)


class CompaniesView(View):
    def get(self, request, id):
        try:
            data_company = Company.objects.get(pk=id)
        except Company.DoesNotExist:
            raise Http404
        vacancies = Vacancy.objects.filter(company=data_company)
        context = {
            'vacancies': vacancies,
            'title': data_company.name,
            'count': data_company.vacancies.count
        }
        return render(request, 'company.html', context=context)


class VacancyView(View):
    def get(self, request, id):
        return render(request, 'vacancy.html')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')


def custom_handler500(request):
    return HttpResponseServerError('Ой, что то пошло не так... Простите извините!')
