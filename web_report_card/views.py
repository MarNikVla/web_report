from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'web_report_card/main.html', context)
