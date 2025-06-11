from rest_framework.pagination import PageNumberPagination

class JurnalPagination(PageNumberPagination):
    page_size = 3  # har bir sahifada 3 ta maqola ko‘rsatiladi
    page_size_query_param = 'page_size'
    max_page_size = 100
