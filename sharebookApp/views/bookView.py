from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from sharebookApp.models.book import Book
from sharebookApp.serializers.bookSerializer import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)

class BooksView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)
