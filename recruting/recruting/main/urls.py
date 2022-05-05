from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter


from recruting.main import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('reg/', views.RegistrationView.as_view()),
    path('admins/', views.AdminView.as_view()),
    path('managers/', views.ManagerView.as_view()),
    path('managers/<int:pk>/', views.ManagerDetail.as_view()),
    path('employees/', views.EmployeeView.as_view())
]

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')

urlpatterns += router.urls