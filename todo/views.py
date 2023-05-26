from django.shortcuts import render, HttpResponse, redirect
from .models import Item

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {  # dictionary all the item in it, so we net the keys of Items
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)
        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')
