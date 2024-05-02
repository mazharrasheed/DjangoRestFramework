# views.py
from django.shortcuts import render, redirect
from .models import Book
from .serializers import BookSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
def index(request):
   
    return render(request, 'book_list.html')

def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
    

@csrf_exempt
def book_detail(request, pk):
    print("i m book_detail")
    book = Book.objects.get(pk=pk)
    return render(request, 'book_list.html', {'book': book})



@csrf_exempt
def book_create(request):
    if request.method == 'POST':
        print("i m book post book_create",request.POST)
        serializer = BookSerializer(data=request.POST)
        print("i m book post hfhfg")
        if serializer.is_valid():
            serializer.save()
            return redirect('book_list')    
    else:
        serializer = BookSerializer()
    
    return JsonResponse(serializer.data, safe=False)
    return render(request, 'book_list.html', {'serializer': serializer})

@csrf_exempt
def book_update(request, pk):
    print("i m book update" ,request.POST)
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        serializer = BookSerializer(instance=book, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('book_list')
    else:
        serializer = BookSerializer(instance=book)
    return render(request, 'book_list.html', {'serializer': serializer})
@csrf_exempt
def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_list.html', {'book': book})
