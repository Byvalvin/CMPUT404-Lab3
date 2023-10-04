# from django.shortcuts import render

# # Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, get_object_or_404 #for new index.html, detail.html,results.html and all views that return render templates
from .models import Question, Choice
from django.urls import reverse #for writng a simple form
from django.views import generic

#serialiser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuestionSerializer


# def index(request):
# 	string = "Hello, World. You're at the polls index."
# 	return HttpResponse(string)

#updated so qyestions are returned
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	out = ', '.join([q.question_text for q in latest_question_list])
# 	return HttpResponse(string)

#updated to use new template in index.html
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)


# #additional views to poll
# def detail(request, question_id):
# 	return HttpResponse("You're looking at question %s. " % question_id)

#updated to use detail.html template
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question':question})

# def results(request, question_id):
# 	response = "You're looking at results of question %s."
# 	return HttpResponse(response % question_id)

# Update results view->After voting, the application should redirect to a view displaying the results.
def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question':question})

# def vote(request, question_id):
# 	return HttpResponse("You're voting on question %s." % question_id)

#vote view updated to handle new template for writng a simple form
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#Redisplay question voting form.
		return render(request, 'polls/detail.html', {'question':question, 'error_message':"You didn't select a choice.",})
	else:
		selected_choice.votes+=1
		selected_choice.save()

		#Always return on HttpResponseRedirect after successfully dealing with POST data.
		#This prevents data from being posted twice if a user hits the back button
		return HttpResponseRedirect( reverse('polls:results', args=(question.id,)) )




# class IndexView(generic.ListView):
# 	template_name = 'polls/index.html'
# 	context_object_name = 'latest_question_list'

# 	def get_queryset(self):
# 		"""Return the last five published questions."""
# 		return Question.objects.order_by('-pub_date')[:5]

# class DetailView(generic.DetailView):
# 	model = Question
# 	template_name = 'polls/detail.html'

# class ResultsView(generic.DetailView):
# 	model = Question
# 	template_name = 'polls/results.html'



# # same as above
# def vote(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	try:
# 		selected_choice = question.choice_set.get(pk=request.POST['choice'])
# 	except (KeyError, Choice.DoesNotExist):
# 		#Redisplay question voting form.
# 		return render(request, 'polls/detail.html', {'question':question, 'error_message':"You didn't select a choice.",})
# 	else:
# 		selected_choice.votes+=1
# 		selected_choice.save()

# 		#Always return on HttpResponseRedirect after successfully dealing with POST data.
# 		#This prevents data from being posted twice if a user hits the back button
# 		return HttpResponseRedirect( reverse('polls:results', args=(question.id,)) )










#Serialiser
@api_view(['GET']) #decorator that wraps view so only HTTP methods in list will be executed
def get_questions(request):
    '''
    Get the list of questions on our website
    '''


    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def update_question(request, pk):
    """
    Get list of questions on our website
    """
    questions = Question.objects.get(id=pk)
    serializer = QuestionSerializer(questions, data=request.data, partial=True)
    if serializer.is_valid():
        return Response(serializer.data)
    return Response(status=400,data=serializer.errors)
















