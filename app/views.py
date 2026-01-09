from rest_framework.generics import ListAPIView
from .models import Category
from .serializers import ParentCategoryModelSerializer


class ParentCategoryListApiView(ListAPIView):
    serializer_class = ParentCategoryModelSerializer

    def get_queryset(self):
        return Category.objects.filter(parent__isnull=True)


class ChildrenCategoryByCategorySlug(ListAPIView):
    serializer_class = ParentCategoryModelSerializer

    def get_queryset(self):
        category_slug = self.kwargs['slug']
        parent_category = Category.objects.filter(slug=category_slug).first()

        if not parent_category:
            return Category.objects.none()

        return parent_category.children.all()
