from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('dash', views.dash, name='dash'),
    path('mprfform', views.mprfform, name='mprfform'),
    path('success', views.success, name='success'),
    path('jobs', views.jobs, name='jobs'),
    path('mprfauthform/<int:pk>', views.mprfauthform, name='mprfauthform'),
    path('mprfapplyform/<int:pk>', views.mprfapplyform, name='mprfapplyform'),
    path('loginapply', views.loginapply, name='loginapply'),
    path('signupapply', views.signupapply, name='signupapply'),
    path('AppliedCandidates',views.AppliedCandidates,name='AppliedCandidates'),
    path('updatecandidatestatus<int:pk>',views.update_candidate_status,name='update_candidate_status'),
    path('formviewapplied<int:pk>',views.formviewapplied,name='formviewapplied'),

]