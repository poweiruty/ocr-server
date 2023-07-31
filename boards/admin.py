from django.contrib import admin
from .models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = [
        'no',
        'title',
        'contents',
        'author',
        'created_at',        
    ]
    list_filter = [
        'no',
        'created_at',
    ]

    sortable_by = [   
        'no',
        'created_at',
    ]