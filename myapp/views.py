from rest_framework import viewsets
from .models import User, Product, Category
from .serializers import UserSerializer, ProductSerializer, CategorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        user_id = self.request.data.get('user')
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({'user': 'User does not exist'})
        
        # Get category if provided
        category = None
        if 'category' in self.request.data and self.request.data['category']:  # Bu yerda o'zgartirildi
            try:
                category = Category.objects.get(pk=self.request.data['category'])
            except Category.DoesNotExist:
                raise serializers.ValidationError({'category': 'Category does not exist'})
        
        serializer.save(user=user, category=category)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def perform_create(self, serializer):
        # Get the user from the request (you'll need to ensure your request is authenticated)
        # Or alternatively, get the user ID from the request data
        serializer.save(user_id=self.request.data.get('user'))