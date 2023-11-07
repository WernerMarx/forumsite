from main.models import ToDoList
from main.models import Item
ToDoList.objects.create(name='Study hard')
Item.objects.create(todolist_id=1,text='Master Django', complete=False)