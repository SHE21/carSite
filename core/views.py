from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import ContactForm
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic.edit import FormView


class IndexView(FormView):
    template_name = 'index.html'
    form = ContactForm

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        print('sdocnifvnsdfivsdf')

        if form.is_valid():
            return HttpResponseRedirect('contact')

        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
