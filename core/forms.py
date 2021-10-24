from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100, min_length=10)
    email = forms.EmailField(label='Email', max_length=100, min_length=10)
    phone = forms.CharField(label='Telefone', max_length=50, min_length=10)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(), min_length=100)

    def show(self):
        name = self.clean['name']
        print(name)
