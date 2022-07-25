from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="home"),
    path('property/<int:id>', views.single,name="single"),
    path('properties', views.propertiesView.as_view(),name="properties"),
    path('about', views.about,name="about"),
    path('agent/<int:id>', views.agent,name="agent"),
    path('agents', views.agentsView.as_view(),name="agents"),
    path('blog/<int:id>', views.blog,name="blog"),
    path('blogs', views.blogsView.as_view(),name="blogs"),
    path('search_me', views.search_meView.as_view(),name="search_me"),

    path('add_house', views.add_house,name="add_house"),
    path('add_blog', views.add_blog,name="add_blog"),
    path('add_agent', views.add_agent,name="add_agent"),

    path('update_agent/<int:pk>', views.update_agent.as_view(),name="update_agent"),
    path('update_blog/<int:pk>', views.update_blog.as_view(),name="update_blog"),
    path('update_property/<int:pk>', views.update_property.as_view(),name="update_property"),

    path('delete_agent/<int:pk>', views.delete_agent.as_view(),name="delete_agent"),
    path('delete_blog/<int:pk>', views.delete_blog.as_view(),name="delete_blog"),
    path('delete_property/<int:pk>', views.delete_property.as_view(),name="delete_property"),

    path('userlogin', views.userlogin,name="userlogin"),
    path('userregister', views.userregister,name="userregister"),
    path('userlogout', views.userlogout,name="userlogout"),
    path('Profile', views.Profile,name="Profile"),
    path('messages', views.messages,name="messages"),
]