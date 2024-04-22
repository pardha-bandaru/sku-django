from django.shortcuts import render, get_object_or_404

from django.http import JsonResponse
# Create your views here.

from rest_framework.decorators import api_view

from rest_framework import generics

from .models import Location, Department, Category, SubCategory, SKUData
from .serializers import LocationSerializer, DepartmentSerializer, CategorySerializer, SubCategorySerializer, SKUDataSerializer


class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
        

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class DepartmentList(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        locationid = self.kwargs.get("pk")

        return Department.objects.filter(location_id=locationid)


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentSerializer

    def get_object(self):
        locationid = self.kwargs.get("pk")
        departmentid = self.kwargs.get("departmentid")

        return get_object_or_404(Department, location_id=locationid, id=departmentid)


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        locationid = self.kwargs.get("pk")
        departmentid = self.kwargs.get("departmentid")

        department = get_object_or_404(Department, location_id=locationid, id=departmentid)

        return Category.objects.filter(department=department)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

    def get_object(self):
        locationid = self.kwargs.get("pk")
        departmentid = self.kwargs.get("departmentid")
        categoryid = self.kwargs.get("categoryid")

        department = Department.objects.get(location_id=locationid, id=departmentid)

        return Category.objects.get(department=department, id=categoryid)


class SubCategoryList(generics.ListCreateAPIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        locationid = self.kwargs.get("pk")
        departmentid = self.kwargs.get("departmentid")
        categoryid = self.kwargs.get("categoryid")

        department = Department.objects.get(location_id=locationid, id=departmentid)
        category = Category.objects.get(department=department, id=categoryid)

        return SubCategory.objects.filter(category=category)


class SubCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubCategorySerializer

    def get_object(self):
        locationid = self.kwargs.get("pk")
        departmentid = self.kwargs.get("departmentid")
        categoryid = self.kwargs.get("categoryid")
        subcategoryid = self.kwargs.get("subcategoryid")

        department = Department.objects.get(location_id=locationid, id=departmentid)
        category = Category.objects.get(department=department, id=categoryid)

        return SubCategory.objects.get(category=category, id=subcategoryid)




class SKUDataView(generics.ListAPIView):
    serializer_class = SKUDataSerializer


    def get_queryset(self):
        location_name = self.request.GET.get('location')
        department_name = self.request.GET.get('department')
        category_name = self.request.GET.get('category')
        subcategory_name = self.request.GET.get('subcategory')

        matched_search_results = SKUData.objects.filter(
            location__name=location_name,
            department__name = department_name,
            category__name = category_name,
            subcategory__name = subcategory_name
            )
        return matched_search_results
