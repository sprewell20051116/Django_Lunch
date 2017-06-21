from django.shortcuts import render
from .models import Store
from django.http import Http404


# Create your views here.
'''
# Move to pages/views.py
def home(request):
    return render(request, 'home.html')
'''
def store_list(request):
    stores = Store.objects.all()
    return render(request, 'store_list.html', {'stores': stores})

def store_detail(request, pk):
  try:
    store = Store.objects.get(pk=pk) # get store by id (Django would assign a ID as primary key to each model)
  except Store.DoesNotExist:
    raise Http404
  return render(request, 'store_detail.html', {'store': store})