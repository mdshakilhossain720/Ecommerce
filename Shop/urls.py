from django.urls import path
from Shop import views
from . forms import LoginForm,MyPasswordChange
from django.contrib .auth import views as auth_view
urlpatterns = [
    path('', views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>/', views.ProductDetailsView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/',auth_view.PasswordChangeForm.as_View(template_name='shop/passwordchange.html',form_class=MyPasswordChange),name='changepassword'),
    path('lehenga/', views.lehenga, name='lehenga'),
    path('lehenga/<slug:data>/', views.lehenga, name='lehengaitem'),
    # path('login/', views.login, name='login'),
    path('registration/', views.CustomerRegestionView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path("accounts/login/",auth_view.LoginView.as_view(template_name='shop/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),

]