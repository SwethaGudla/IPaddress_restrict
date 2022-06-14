# from django.conf import settings
# from django import http
# class IPAddress(object):
#     def __init__(self,get_response):
#         self.get_response = get_response
#     def __call__(self,request):
#         if request.META['REMOTE_ADDR'] in settings.IP_ADDRESS:
#             return http.HttpResponseForbidden('<h1>This IP Address cannot access</h1>')
#         return self.get_response(request)

from django.conf import settings
from django import http
class IPAddress(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if request.META['REMOTE_ADDR'] in settings.IP_ADDRESS:
            return http.HttpResponseForbidden('<h1>This IP Address cannot access</h1>')
        return self.get_response(request)