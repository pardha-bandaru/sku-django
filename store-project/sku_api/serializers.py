from rest_framework import serializers

from .models import Location, Category, SubCategory, Department, SKUData


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class SKUDataSerializer(serializers.ModelSerializer):
    location = serializers.ReadOnlyField(source='location.name')
    department = serializers.ReadOnlyField(source='department.name')
    category = serializers.ReadOnlyField(source='category.name')
    subcategory = serializers.ReadOnlyField(source='subcategory.name')
    class Meta:
        model = SKUData
        fields = ('id', 'name', "location", "department", "category", "subcategory")
