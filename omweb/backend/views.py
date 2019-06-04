from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.core import serializers
from backend.models import Book
import json

# Create your views here.
@require_http_methods(['GET'])
def add(request):
    response = {}
    try:
        book = Book(name=request.GET.get('name'))
        book.save()
        response['msg'] = 'success'
        response['error_code'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_code'] = 1
    
    return JsonResponse(response)


@require_http_methods(['GET'])
def books(request):
    response = {}
    try:
        all_books = Book.objects.filter()
        response['books'] = json.loads(serializers.serialize("json", all_books))
        response['msg'] = 'success'
        response['error_code'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_code'] = 1
        
    return JsonResponse(response)

    
