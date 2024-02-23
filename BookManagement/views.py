from django.shortcuts import render

# Create your views here.
def bookCatalog(request):
    return render(request,'./BookManagement/book_catalog.html',{"book":[
        {
          'image':'1.jpg',
          'title':'equivalent javascript',
          'author':'sefat',
          'ISBN': '123',
          'publication date':'12-12-2022',
          'genre':'sdjjfhf',
          'availability status' :'available',
          'no of books available':10  
        },
        {
           'image':'1.jpg',
          'title':'my javascript',
          'author':'sefat',
          'ISBN': '123',
          'publication date':'12-12-2022',
          'genre':'sdjjfhf',
          'availability status' :'available',
          'no of books available':10  
        },
        {
          'image':'2.jpg',
          'title':'my javascript',
          'author':'sefat',
          'ISBN': '123',
          'publication date':'12-12-2022',
          'genre':'sdjjfhf',
          'availability status' :'available',
          'no of books available':10  
        },
    ]})