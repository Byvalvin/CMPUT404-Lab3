from django.urls import path
from . import views

# urlpatterns = [ path('', views.index, name='index'), ]


app_name = 'polls' #to add app name


urlpatterns = [ 
#ex: /polls/
path('', views.index, name='index'), 

#ex: /polls/5/
path('<int:question_id>/', views.detail, name='detail'),

#ex: /polls/5/results/
path('<int:question_id>/results/', views.results, name='results'),

#ex: /pools/5/vote/
path('<int:question_id>/vote/', views.vote, name='vote'),

#serialiser
path('api/questions/', views.get_questions, name='get_questions'),

path('api/question/<int:pk>', views.update_question, name='update_question'),

]


# urlpatterns = [ 
# #ex: /polls/
# path('', views.IndexView.as_view(), name='index'), 

# #ex: /polls/5/
# path('<int:pk>/', views.DetailView.as_view(), name='detail'),

# #ex: /polls/5/results/
# path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

# #ex: /pools/5/vote/
# path('<int:question_id>/vote/', views.vote, name='vote'),

# ]