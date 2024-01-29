from django.urls import path
from .views import ReadingList, ReadingDetail, ReadingCreate  # 追加

urlpatterns = [
    path("", ReadingList.as_view(), name="list"),
    path("detail/<int:pk>", ReadingDetail.as_view(), name="detail"),
    path("create/", ReadingCreate.as_view(), name="create"),  # 追加
]
