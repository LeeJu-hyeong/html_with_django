from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage

def Range(a, b):
    ret = []
    for i in range(a, b):
        ret.append(i)
    return ret

def index(request):
    return render(request, 'index.html')

def nxt(request):
    file = request.FILES["fu"]
    file_name = default_storage.save('media/' + file.name, file)

    return render(request, 'next.html', {"file_name": file.name})

def func(request, question_id):
    return render(request, 'num.html', { "num": question_id, "range": Range(1, 11)})