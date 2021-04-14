from django.shortcuts import render
from django.shortcuts import get_object_or_404
import datetime
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy, reverse


from .forms import LanguageModelForm
from .models import Language


def index(request):
    now = datetime.datetime.now()
    return render(request, "index.html", {"now": now})


def profile(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Uncnown"
    print(request.user)
    return render(request, "profile.html", {"username": username})


def languages(request):
    form = LanguageModelForm()
    return render(request, 'languages.html', {'form': form})


def renew_language(request, pk):
    language_inst = get_object_or_404(Language)

    # Если данный запрос типа POST, тогда
    if request.method == 'POST':

        # Создаём экземпляр формы и заполняем данными из запроса (связывание, binding):
        form = LanguageModelForm(request.POST)

        # # Проверка валидности данных формы:
        # if form.is_valid():
        #     # Обработка данных из form.cleaned_data
        #     #(здесь мы просто присваиваем их полю due_back)
        #     language_inst.complexity = form.cleaned_data['complexity']
        #     language_inst.save()
        #
        #     # Переход по адресу 'all-borrowed':
        #     return HttpResponseRedirect(reverse('all-borrowed'))

    # Если это GET (или какой-либо ещё), создать форму по умолчанию.
    else:
        form = LanguageModelForm()

    return render(request, 'languages.html', {'form': form})


class LanguageListView(ListView):
    model = Language
    paginate_by = 100
    template_name = "languages.html"


class LanguageCreate(CreateView):
    model = Language
    # fields = '__all__'
    success_url = reverse_lazy('languages')
    form_class = LanguageModelForm


class LanguageUpdate(UpdateView):
    model = Language
    form_class = LanguageModelForm
    success_url = reverse_lazy('languages')


class LanguageDelete(DeleteView):
    model = Language
    success_url = reverse_lazy('languages')
