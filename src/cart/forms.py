from django import forms
from .models import OrderItem, Producto, Medida, Address
from django.contrib.auth import get_user_model

User = get_user_model()

class AddToCartForm(forms.ModelForm):
    
    size = forms.ModelChoiceField(queryset=Medida.objects.none())
    quantity = forms.IntegerField(min_value=1)

    class Meta:
        model = OrderItem
        fields = ['quantity',  'size']

    def __init__(self, *args, **kwargs):
        self.product_id = kwargs.pop('product_id')
        producto = Product.objects.get(id=self.product_id)
        super().__init__(*args, **kwargs)

        
        self.fields['size'].queryset = producto.available_sizes.all()

    def clean(self):
        product_id = self.product_id
        producto = Product.objects.get(id=self.product_id)
        quantity = self.cleaned_data['quantity']

        if producto.stock < quantity:
            raise forms.ValidationError(f"The maximum stock is {producto.stock}")



class AddressForm(forms.Form):
    
    shipping_address_line_1 = forms.CharField(required=False)
    shipping_address_line_2 = forms.CharField(required=False)
    
    shipping_city = forms.CharField(required=False)

    billing_address_line_1 = forms.CharField(required=False)
    billing_address_line_2 = forms.CharField(required=False)
   
    billing_city = forms.CharField(required=False)

    selected_shipping_address = forms.ModelChoiceField(
        Address.objects.none(), required=False
    )

    selected_billing_address = forms.ModelChoiceField(
        Address.objects.none(), required=False
    )

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)

        user = User.objects.get(id=user_id)

        shipping_address_qs = Address.objects.filter(
            user=user,
            address_type='S'
        )

        billing_address_qs = Address.objects.filter(
            user=user,
            address_type='B'
        )

        self.fields['selected_shipping_address'].queryset = shipping_address_qs
        self.fields['selected_billing_address'].queryset = billing_address_qs


    def clean(self):
        data = self.cleaned_data

        selected_shipping_address = data.get('selected_shipping_address', None)
        if selected_shipping_address is None:
            if not data.get('shipping_address_line_1', None):
                self.add_error("shipping_address_line_1", "Please fill in this field")
            if not data.get('shipping_address_line_2', None):
                self.add_error("shipping_address_line_2", "Please fill in this field")
            
            if not data.get('shipping_city', None):
                self.add_error("shipping_city", "Please fill in this field")

        selected_billing_address = data.get('selected_billing_address', None)
        if selected_billing_address is None:
            if not data.get('billing_address_line_1', None):
                self.add_error("billing_address_line_1", "Please fill in this field")
            if not data.get('billing_address_line_2', None):
                self.add_error("billing_address_line_2", "Please fill in this field")
            
            if not data.get('billing_city', None):
                self.add_error("billing_city", "Please fill in this field")
