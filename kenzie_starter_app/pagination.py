from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class CustomPage(PageNumberPagination):
    @classmethod
    def setParams(cls, page_size, max_page_size):
        cls.page_size_query_param = "size"
        cls.page_size = page_size
        cls.max_page_size = max_page_size
        return cls


class CustomOffset(LimitOffsetPagination):
    max_limit = 100
