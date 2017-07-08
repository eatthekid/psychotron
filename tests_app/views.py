from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.models import User
from datetime import datetime

@csrf_exempt
def EPI_testing(request):
    if request.method == 'POST':
        ext = 0
        ner = 0
        lie = 0
        ext_yes = ['1', '3', '8', '10', '13', '17', '22', '25', '27', '39', '44', '46', '49', '53', '56']
        ext_no = ['5', '15', '20', '29', '32', '34', '37', '41', '51']
        ner_yes = ['2', '4', '7', '9', '11', '14', '16', '19', '21', '23', '26', '28', '31', '33', '35', '38', '40', '43', '45', '47', '50', '52', '55', '57']
        lie_yes = ['6', '24', '36']
        lie_no = ['12', '18', '30', '42', '48', '54']
        for q in ext_yes:
            if request.POST.get(q) == 'yes':
                ext += 1
        for q in ext_no:
            if request.POST.get(q) == 'no':
                ext += 1
        for q in ner_yes:
            if request.POST.get(q) == 'yes':
                ner += 1
        for q in lie_yes:
            if request.POST.get(q) == 'yes':
                lie += 1
        for q in lie_no:
            if request.POST.get(q) == 'no':
                lie += 1
        testing = EPI.objects.create(TestUser = request.user, EXT = ext, NER = ner, LIE = lie)
        testing.save()
        # passingDate = datetime.strptime(str(testing.passingDate), "%d/%m/%y %H:%M")
        result = {
            'username': testing.TestUser.username,
            'dateTesting': str(testing.passingDate),
            'EXT': testing.EXT,
            'NER': testing.NER,
            'LIE': testing.LIE,
        }
        context = {'result': result}
        return render(request,'tests/EPI.html', context)

    else:
        f = open('tests_app/StimulMaterial/EPI.txt', 'r', encoding='utf-8')
        questions = []
        for row in f:
            questions.append(row)
        f.close()
        return render(request, 'tests/EPI.html', {'questions': questions})

