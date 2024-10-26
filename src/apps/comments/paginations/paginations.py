from apps.base.pagination import CustomPageNumberPagination

class CommentReplyPagination(CustomPageNumberPagination):
    page_size = 5
    page_query_param = 'child_page'
    page_size_query_param = 'child_page_size'
    max_page_size = 50

