from django.shortcuts import render 
from django.shortcuts import redirect
from .models import Store
from django.http import Http404
from django.forms.models import modelform_factory # 20170622 implement user create function

# Create your views here.

# # Move to pages/views.py
# def home(request):
#     return render(request, 'home.html')

def store_list(request):
    stores = Store.objects.all()
    return render(request, 'stores/store_list.html', {'stores': stores})

def store_detail(request, pk):
  try:
    store = Store.objects.get(pk=pk) # get store by id (Django would assign a ID as primary key to each model)
  except Store.DoesNotExist:
    raise Http404
  return render(request, 'stores/store_detail.html', {'store': store})

# # 20170622 implement user create function
# def store_create(request):
#     StoreForm = modelform_factory(Store, fields=('name', 'notes',))
#     form = StoreForm()
#     return render(request, 'stores/store_create.html', {'form': form})

# 20170622-2 implement user create function - insert POST methods
def store_create(request):
    StoreForm = modelform_factory(Store, fields=('name', 'notes',))
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save()
            return redirect(store.get_absolute_url())
    else:
        form = StoreForm()
    return render(request, 'stores/store_create.html', {'form': form})


def store_update(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404
    
    StoreForm = modelform_factory(Store, fields=('name', 'notes'))
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            store = form.save()
            return redirect(store.get_absolute_url())
    else:
        form = StoreForm(instance=store)
    
    return render(request, 'stores/store_update.html', {
        'form': form, 'store': store,
    })