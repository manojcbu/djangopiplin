from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView

app_name = "candidates"
urlpatterns = [
    # /candidates/
    path('', HomeView.as_view(), name='home'),
    path('', views.home, name='candidates-home'),
    path('', views.candidates, name='candidates'),
    path('create/', views.create_candidate, name='create candidates')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




#urlpatterns = path['basic.events.views',
 #   url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/(?P<event_id>\d)/$',
  #      view='event_detail',
   #     name='event_detail'
    #    )],
        
        
        
        
#urlpatterns = [
    # Define your URL patterns using 'path' or 're_path'
 #   path('events/', views.some_view_function, name='name'),
    # Use 're_path' for regex-based URL patterns
  #  re_path(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/(?P<event_id>\d+)/$', views.event_detail, name='event-detail'),
    # Add more URL patterns if needed
#]