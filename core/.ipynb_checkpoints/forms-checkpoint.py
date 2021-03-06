from django import forms
from django.core.mail.message import EmailMessage

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    phone = forms.CharField(label='Telefone', max_length=50)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        message = self.cleaned_data['message']

        content = f'name:{name}\nemail:{email}\nphone:{phone}\nmessage:{message}'

        mail = EmailMessage(
            subject = 'teste',
            body = content,
            from_email = 'santiagolenil@gmail.com',
            to = ['santiagolenil@gmail.com'],
            headers = {'Reply-to': email}
        )

        mail.send()