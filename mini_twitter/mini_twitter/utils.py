from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from django.core.mail import send_mail

from .settings import EMAIL_HOST_USER


class CustomPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response(
            {
                "links": {"next": self.get_next_link(), "previous": self.get_previous_link()},
                "count": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )
    

def send_custom_email(subject, message, receivers):
    try: 
        send_mail(
            subject=subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=receivers,
            fail_silently=False,
        )
    except Exception as error:
        print("erro ao enviar email: ", error)

