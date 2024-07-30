from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def get_all_books(request):
    books = Book.objects.all()
    serializer_obj = BookSerializer(books, many=True)
    return Response(serializer_obj.data)

@api_view(['GET'])
def get_book_by_id(request, pk):
    try:
        book = Book.objects.get(id=pk)
        serializer_obj = BookSerializer(book, many=False)
        return Response(serializer_obj.data)
    except Book.DoesNotExist:
        return Response( "Book not found")

   

@api_view(['DELETE'])
def delete_book(request, pk):
    try:
        book = Book.objects.get(id=pk)
        book.delete()
        return Response("Book deleted successfully")
    except Book.DoesNotExist:
        return Response("Book not found")
    

@api_view(['POST'])
def add_book(request):
    serializer_obj = BookSerializer(data=request.data)
    if serializer_obj.is_valid():
        serializer_obj.save()
        return Response("Book added successfully")
    else:
        return Response("book not added")
    

@api_view(['PUT'])
def update_book(request, pk):
    try:
        book = Book.objects.get(id=pk)
        serializer_obj = BookSerializer(instance=book, data=request.data, partial=True)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response("Book updated successfully")
    except Book.DoesNotExist:
        return Response("Book not updated")
    
# @api_view(['GET'])
# def Login(request,pk)
#     try:
#         book = Book.objects.filter(price = Book.objects.get('price'), author = Book.objects.get('author'))
#         return
        
    



