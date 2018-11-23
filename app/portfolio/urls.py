from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.BaseView.as_view(),name="base"),
    url(r'^home/$',views.HomeView.as_view(),name='home'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^experience/$',views.ExpView.as_view(),name='exp'),
    url(r'^projects/$',views.ProjView.as_view(),name='proj'),
    url(r'^skills/$',views.SkillsView.as_view(),name='skills'),
]