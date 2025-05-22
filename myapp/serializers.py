from rest_framework import serializers
from .models import User, Product, Category

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False, allow_null=True)

    # Read-only fieldlar: Foydalanuvchi nomi va kategoriya nomi
    userName = serializers.CharField(source='user.userName', read_only=True)
    category_name = serializers.IntegerField(source='category.id', read_only=True)

    # Write va read uchun kerakli ID fieldlar
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    class Meta:
        model = Product
        fields = [
            'id', 'user', 'userName',
            'category', 'category_name',
            'image', 'name', 'description', 'price'
        ]


class CategorySerializer(serializers.ModelSerializer):
    userName = serializers.CharField(source='user.userName', read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'user', 'userName', 'name']


class UserSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True, source='product_set')
    categories = CategorySerializer(many=True, read_only=True,)

    class Meta:
        model = User
        fields = ['id', 'userName', 'password', 'products', 'categories']
