from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from leftright.models import Game


# Create your views here.
class GameListView(ListView):
    model = Game
    paginate_by = 10
    ordering = ['-created_date']

class GameDoView(LoginRequiredMixin, TemplateView):
    template_name = "leftright/game_do.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['ltScore'] = Game.objects.filter(leftright='lf', usr=user).count()
        context['rtScore'] = Game.objects.filter(leftright='rt', usr=user).count()
        return context


def getpoint(request):
    direction = request.GET.get('dir', None)
    req_user = request.user
    Game.objects.create(usr=req_user, leftright=direction)
    count = Game.objects.filter(usr=request.user, leftright=direction).count()
    data = {
        'dir': direction,
        'point': count
    }
    return JsonResponse(data)
