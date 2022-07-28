from django.urls import path
from . import views # all views in file structure will be imported
from .views import FoodDetail, FoodList, FoodCreate, FoodUpdate,FoodDelete

urlpatterns = [
    path('', FoodList.as_view(), name='foods'), # base url, name of view, url pattern on host
    path('food/<int:pk>', FoodDetail.as_view(), name='food'), # primary key, name of view, url pattern on host
    path('food-create', FoodCreate.as_view(), name='food-create'), # base url, name of view, url pattern on host
    path('food-update/<int:pk>', FoodUpdate.as_view(), name='food-update'), # primary key, name of view, url pattern on host
    path('food-delete<int:pk>', FoodDelete.as_view(), name='food-delete'), # primary key, name of view, url pattern on host

]