from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('addrecipe/', views.add_recipe),
    path('addauthor/', views.add_author),
    path('recipe/<int:recipe_id>/', views.recipe),
    path('author/<int:author_id>/', views.author)
    # path('admin/', admin.site.urls),
]