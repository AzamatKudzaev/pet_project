from django.urls import path
from monkey_app import views


urlpatterns = [
    path('', views.main, name='main'),
    path('about-us/', views.about_us, name='about-us'),
    path('articles/', views.articles_view, name='articles'),
    path('articles/add_new_article/', views.create_article, name='create_article'),
    path('articles/<str:article_kind>/<int:id_article>/', views.show_article, name='show-article'),
    path('profiles/<str:profile_name>/', views.show_profile, name='profile')
]

# адрес лучше закрывать слэшем в конце

