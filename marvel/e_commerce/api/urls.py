from django.urls import path
from e_commerce.api.views import *
from e_commerce.api.marvel_api_views import *

urlpatterns = [
    path('hello-world/',hello_world),
    path('parametro-post/',parametro_post),
    path('get-commits/',get_comics),
    path('purchased-item/',purchased_item),
    
]