from .views import ParentCategoryListApiView , ChildrenCategoryByCategorySlug
from django.urls import path, include


urlpatterns = [
    path('',ParentCategoryListApiView.as_view()),
    path('category/<slug:slug>/', ChildrenCategoryByCategorySlug.as_view()),

]
