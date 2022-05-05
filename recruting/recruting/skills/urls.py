from django.urls import path

from recruting.skills import views

urlpatterns = [
    path('departments/', views.CategoryList.as_view()),
    path('departments/<int:pk>/', views.CategoryDetails.as_view()),
    path('departments/<int:pk>/positions/', views.PositionList.as_view()),
    path('departments/<int:pk1>/positions/<int:pk2>/', views.PositionDetail.as_view()),
    path('questions/', views.QuestionList.as_view()),
    path('skillsets/', views.SkillSetList.as_view()),
    path('skillquestions/', views.SkillSetQuestionsList.as_view())
]