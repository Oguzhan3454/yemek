from django.urls import path
from .views import index, post, post_details
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", index, name="index"),
    path("food", post, name="food_post"),
    path("food/<int:pk>", post_details, name="post_details")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
