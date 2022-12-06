from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem


def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    context = {
        'all_items': all_todo_items,
    }
    return render(request, 'todolist.html', context)


def addTodoView(request):
    content = request.POST['content']
    new_item = TodoListItem(content=content)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')


def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')
