from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
  path('',views.index,name='index'),
  path('add_transaction/',views.add_transaction,name='add_transaction'),
  path('edit_transaction/<int:id>/',views.edit_transaction,name='edit_transaction'),
  path('delete/<int:id>/',views.delete_transaction,name='delete_transaction'),
  path('add_category/',views.category,name='add_category'),
  path('transaction_list/',views.Transaction_list,name='transaction_list'),
  path('register/', views.register, name='register'),
  path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
  path('profile/',views.profile,name='profile'),
  path('profile/edit/', views.edit_profile, name='edit_profile'),
  path('about/',views.about,name='about')
]
