import os
from django.http import HttpResponseRedirect
from django.shortcuts import render

myContext=[
        {
            'id':1,
            'name':'workout',
            'description':'Lifting Weights'
        },
        {
            'id':2,
            'name':'go shopping',
            'description':'Buy stuff'
        }
    ]

def home_view(request):
    print(os.path.abspath(os.getcwd()))
    return render(request,'home_view.html',{'myContext':myContext})
def add_view(request):
    return render(request,'add_view.html',{'myContext':myContext})

def item_view(request, **kwargs):
    id=kwargs.get('id');
    print("itemVIEW"+str(myContext))
    for item in myContext:
        if(item.get('id')==id):
            index=myContext.index(item)
    targetTodo={'targetTodo':myContext[index]}
    return render(request,'item_view.html',targetTodo)

def delete_view(request, **kwargs):
    id=kwargs.get('id');
    for item in myContext:
        if(item.get('id')==id):
            index=myContext.index(item)
    targetTodo=myContext[index]
    index=myContext.index(targetTodo)
    myContext.pop(index)
    # return render(request,'home_view.html',targetTodo)
    return HttpResponseRedirect("/home")

def edit_view(request, **kwargs):
    id=kwargs.get('id');
    for item in myContext:
        if(item.get('id')==id):
            index=myContext.index(item)
            targetTodo=myContext[index]
            # index=myContext.index(targetTodo)
            # myContext[index]
    return render(request,'edit_view.html',{'targetTodo':targetTodo})
    # return HttpResponseRedirect("/home")

def editFunction(request, **kwargs):
    id=kwargs.get('id');
    for item in myContext:
        if(item.get('id')==id):
            index=myContext.index(item)
    targetTodo=myContext[index]
    # index=myContext.index(targetTodo)
    # myContext[index]
    editedTargetTodo={
        'id':request.POST['id'],
        'name':request.POST['name'],
        'description':request.POST['description'],
    }
    targetTodo.update(editedTargetTodo)
    # return render(request,'edit_view.html',{'targetTodo':targetTodo})
    return HttpResponseRedirect("/home")

def addToArray_view(request, **kwargs):
    dict={
        'id':request.POST['id'],
        'name':request.POST['name'],
        'description':request.POST['description'],
    }
    myContext.append(dict)
    # return HttpResponseRedirect("/home")
    return render(request,'home_view.html',{'myContextNew':myContext})

