import time
from django.db import connection
from django.utils.deprecation import MiddlewareMixin


class PerformanceMiddleware(MiddlewareMixin):
    """Простой мидлвар для вывода в консоль количество запросов к БД и времени выполнения"""

    @staticmethod
    def process_request(request):
        request.start_time = time.time()

    @staticmethod
    def process_response(request, response):
        total_queries = len(connection.queries)
        total_time = time.time() - request.start_time
        print(f'Database queries: {total_queries}')
        print(f'Request processing time: {total_time:.3f} seconds')
        return response
