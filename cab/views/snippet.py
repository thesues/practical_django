from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from cab.models import Snippet
class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        exclude = ['author']

@login_required
def add_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            new_snippet = form.save(commit=False)
            new_snippet = form.save()
            return HttpResponseRedirect(new_snippet.get_absolute_url())
    else:
        form = SnippetForm()
    return render_to_response('cab/add_snippet.html',{ 'form': form })

