from django.urls import path,include
from .views import atbashCipher

urlpatterns = [
    path("",atbashCipher ,name="atbash"),    
]
