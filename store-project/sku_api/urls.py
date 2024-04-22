from django.urls import path

from .views import (
    LocationList, LocationDetail, DepartmentList,
    DepartmentDetail, CategoryList, CategoryDetail,
    SubCategoryList, SubCategoryDetail, SKUDataView
)


urlpatterns = [
    path('location/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
    path('location/<int:pk>/department/', DepartmentList.as_view()),
    path('location/<int:pk>/department/<int:departmentid>/', DepartmentDetail.as_view()),
    path('location/<int:pk>/department/<int:departmentid>/category/', CategoryList.as_view()),
    path('location/<int:pk>/department/<int:departmentid>/category/<int:categoryid>/', CategoryDetail.as_view()),
    path('location/<int:pk>/department/<int:departmentid>/category/<int:categoryid>/subcategory/', SubCategoryList.as_view()),
    path('location/<int:pk>/department/<int:departmentid>/category/<int:categoryid>/subcategory/<int:subcategoryid>/', SubCategoryDetail.as_view()),

    path('skus/', SKUDataView.as_view())
]
