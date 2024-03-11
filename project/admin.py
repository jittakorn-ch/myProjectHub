from django.contrib import admin

from .models import TodoList

class TodoListAdmin(admin.ModelAdmin):
    list_display = ['todo_id', 'subject', 'description', 'date_start', 'date_end', 'is_completed']


admin.site.register(TodoList, TodoListAdmin)
