# views.py
from django.shortcuts import render
from django.http import  HttpResponseRedirect, HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

def index(response, id):
	ls = ToDoList.objects.get(id=id)
    
	if response.method == "POST":
			print(response.POST)
			if response.POST.get("save"):
				for item in ls.item.all():
					if response.POST.get("c" + str(item.id)) =="clicked":
						item.complete = True
					else:
						item.complete = False
					item.save()
			elif response.POST.get("newItem"):
				txt = response.POST.get("new")
 
				if len(txt) > 2:
					ls.item.create(text=txt, complete=False)
				else:
					print("invalid")
					
	return render(response, "main/list.html", {"ls":ls})

def home(request):
	js = ["Item 1", "Item 3", "Item 4"]
	return render(request, "main/home.html", {"js":js})

def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    return render(request, "main/create.html", {"form":form})