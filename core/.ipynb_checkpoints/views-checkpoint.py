
from django.views.generic import FormView
from .forms import ContactForm
from django.contrib import messages
from django.urls import reverse_lazy
from .Data import services, team


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = services
        context['team'] = team
        return context


    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)


    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Error')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)