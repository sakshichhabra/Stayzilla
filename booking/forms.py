from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('listing_id', 'customer_id', 'check_in', 'check_out', 'price', 'number_of_guests')
        widgets = {
            'listing_id': forms.HiddenInput(attrs={'readonly': 'true'}),
            'customer_id': forms.HiddenInput(attrs={'readonly': 'true'}),
            'check_in': forms.DateInput(attrs={'class': 'form-control date'}, format='%d-%m-%y'),
            'check_out': forms.DateInput(attrs={'class': 'form-control date'}, format='%d-%m-%y'),
            'price': forms.HiddenInput(attrs={'readonly': 'true', 'class': 'form-control price'}),
            'number_of_guests': forms.NumberInput(attrs={'class': 'form-control form-control-sm '
                                                                  'guest-box text-center text-white p-2',
                                                         'placeholder': 'Number of Guests',
                                                         'readonly': 'true'})
        }
