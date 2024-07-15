from django import forms
from .models import Prato

class PratoForm(forms.ModelForm):
    class Meta:
        model = Prato
        fields = ('nome', 'descricao', 'preco', 'imagem')
    
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
                field.widget.attrs['class'] = 'form-control'