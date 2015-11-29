from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'encuestas/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Devuelve los ultimos cinco preguntas publicadas."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'encuestas/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'encuestas/results.html'

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



def encuestas(request):

    if request.method == 'GET':
        encuestas = Question.objects.all()
        serializador = QuestionSerializer(encuestas, many=True)
        return JSONResponse(serializador.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializador = QuestionSerializer(data=data) 
        if serializador.is_valid():
            serializador.save()
            return JSONResponse(serializador.data, status=201)
    return JSONResponse(serializador.errors, status=400)


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        """ vuelve a mostrar la votacion """
        return render(request, 'encuestas/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
	""" Devuelve HttpResponseRedirect cuando la accion ocurre con exito """
        return HttpResponseRedirect(reverse('results', args=(p.id,)))
