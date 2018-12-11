from django import forms

class ContactForm(forms.Form):
    nome_completo = forms.CharField(
        error_messages={'required': 'Obrigatório o preenchimento deste campo!'},
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Seu nome completo"
                }
            )
        )
    email     = forms.EmailField(
        error_messages={'invalid': 'Digite um email válido!'},
        widget=forms.EmailInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite seu email"
                }
            )
        )
    texto   = forms.CharField(
        error_messages = {'required': 'Obrigatório o preenchimento deste campo!'},
        widget=forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite sua mensagem"
                }
            )
)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("apenas email do GMAIL são aceitos")
        return email

