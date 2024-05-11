from playground import models
from django.db.models import Q

class book_controller:
    def get_all_books_controller(request):
        try:
            books = models.Game.objects.all()
            data = [{'Name': book.name, 
                     'about_game': book.about_game,
                     'gameplay': book.gameplay,
                     'price': book.price,
                     'Video': book.video,
                    } for book in books]


            return 201, data
        
        except Exception as e:
            return 500, e
        
    
    def get_books_by_name_controller(request, str_variable):
        try:
            books = models.Game.objects.get(name=str_variable)
            print(books.name)
        
            if not books: return 404, "Books not found!!"

            data = [{'Name': books.name, 
                     'about_game': books.about_game,
                     'gameplay': books.gameplay,
                     'price': books.price,
                     'Video': books.video,
                    }]

            return 201, data
        
        except Exception as e:
            return 500, e
        
    
    def get_books_by_category_controller(request, category):
        try:
            books = models.Book.objects.filter(categories=category).values('book_id', 'title', 'authors', 'thumbnail', 'price', 'categories', 'average_rating')
        
            if not books:
                return 404, "Books not found!!"

            data = [{'book_id': book['book_id'], 
                     'title': book['title'],
                     'thumbnail': book['thumbnail'],
                     'authors': book['authors'],
                     'price': book['price'],
                     'category': book['categories'],
                     'average_rating': book['average_rating']
                    } for book in books]

            return 201, data
        
        except Exception as e:
            return 500, e
        
    
    def get_category_list_controller(request):
        try:
            categories_field = models.Book.objects.values_list('categories', flat=True)

            if not categories_field.exists():
                return 404, "Books not found!!"

            categories = set()
            for cate in categories_field:
                if cate:
                    categories.update([cate])

            category_list = sorted(categories)

            return 201, category_list

        except Exception as e:
            return 500, str(e)

    def get_book_detail_controller(request, book_id):
        try:
            book_query = models.Book.objects.filter(book_id=book_id).values('book_id', 'title', 'authors', 'categories', 'thumbnail', 
                                                         'description', 'published_year', 'average_rating', 'num_pages', 'price')
    
            if book_query.exists():
                book_data = book_query.first() 
            else:
                return 404, "Books not found!!"


            data = {'book_id': book_data['book_id'], 
                    'title': book_data['title'],
                    'authors': book_data['authors'],
                    'categories': book_data['categories'],
                    'thumbnail': book_data['thumbnail'],
                    'description': book_data['description'],
                    'published_year': book_data['published_year'],
                    'average_rating': book_data['average_rating'],
                    'num_pages': book_data['num_pages'],
                    'price': book_data['price']}

            return 201, data
    
        except Exception as e: 
            return 500, e
    
        
    def get_books_by_id_controller(book_id):
        try:
            book_query = models.Book.objects.filter(book_id=book_id).values('book_id', 'title', 'authors', 'thumbnail', 'price', 'average_rating')
        
            if book_query.exists():
                book = book_query.first() 
            else:
                return 404, "Books not found!!"

            data = {'book_id': book['book_id'], 
                     'title': book['title'],
                     'thumbnail': book['thumbnail'],
                     'authors': book['authors'],
                     'price': book['price'],
                     'average_rating': book['average_rating']
                    }

            return 201, data
        
        except Exception as e:
            return 500, e