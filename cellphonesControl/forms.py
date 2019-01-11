from django import forms

from apps.cellphonesControl import RecepcionMercancia, OrdenCompra

class RecepcionForm(forms.Model):

    class Meta:
        model = Recepcion
        fields = [
            'subinventario',
            'nombre',
            'modelo',
            'imei',
            'folio'
        ]
        labels = {
            'subinventario' : 'Subinventario',
            'nombre' : 'Nombre',
            'modelo' : 'Modelo',
            'imei' : 'IMEI'
            'folio' : 'Folio'
        }
        widgets = {
            'suninventario':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'modelo':forms.TextInput(attrs={'class':'form-control'}),
            'imei':forms.TextInput(attrs={'class':'form-control'}),
            'folio':forms.TextInput(attrs={'class':'form-control'}),
        }

class OrdenCompraForm(forms.Form):
    class Meta:
        model = Orden
        fields = [
            'pvd',
            'cantidadPedidos',
            'comentario'
        ]    
        labels = {
            'pvd' : 'PVD',
            'cantidadPedidos' : 'Cantidad de elementos pedidos',
            'comentario' : 'Comentarios'
        }
        widgets = {
            'pvd':forms.TextInput(attrs={'class':'form-control'}),
            'cantidadPedidos':forms.TextInput(attrs={'class':'form-control'}),
            'comentario':forms.Textarea(attrs={'class':'form-control'}),
        }