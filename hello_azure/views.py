from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SearchLog

def index(request):
    print('Request for index page received')
    return render(request, 'hello_azure/index.html')

@csrf_exempt
def hello(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        id = request.POST.get('id')
        if name is None or name == '':
            print("Request for hello page received with no name or blank name -- redirecting Jai Sri Ram")
            return redirect('index')
        else:
            print("Request for hello page received with name=%s Jai Sri Ram" % name)
            jsr = 'Jai Sri Ram'
            jsr = name + jsr
            db = SearchLog(id=id,name=name)
            db.save()
            context = {'name': jsr}
            return render(request, 'hello_azure/hello.html', context)
    else:
        return redirect('index')