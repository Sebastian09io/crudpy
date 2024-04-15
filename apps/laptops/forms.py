"""
formularios
"""

from django import forms
from .models import Laptop

class LaptopForm(forms.ModelForm):
    """
    clase de formulario
    """
    class Meta:
        """
        maneja metadatos
        """
        model = Laptop
        fields = ['procesador', 'generacion', 'sistema', 'ram', 'rom',]

    def clean_generacion(self):
        generacion = self.cleaned_data['generacion']
        if generacion <= 0:
            raise forms.ValidationError("La generación debe ser un número entero positivo.")
        return generacion 
