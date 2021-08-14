from django.urls import path
from api import views

urlpatterns = [
    path("",views.ListCoursAPIView.as_view(),name="cours_list"),
    path("create/", views.CreateCoursAPIView.as_view(),name="cours_create"),
    path("update/<int:pk>/",views.UpdateCoursAPIView.as_view(),name="update_cours"),
    path("delete/<int:pk>/",views.DeleteCoursAPIView.as_view(),name="delete_cours")
]