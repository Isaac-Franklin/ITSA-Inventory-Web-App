from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.UserSignupPage, name="UserSignupPage"),
    path('continuesignup/', views.ContinueUserSignup, name="ContinueUserSignup"),
    path('', views.Login_User, name="userlogin"),
    # path('profilepic/<str:id>/', views.ProfilePic, name="profilepic"),
]
