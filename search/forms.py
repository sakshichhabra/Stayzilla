from django import forms
from .models import Search
from bootstrap_datepicker_plus import DatePickerInput
from datetime import datetime


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('destination', 'from_date', 'to_date', 'num_guests')
        widgets = {
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Destination'}),
            'from_date': DatePickerInput(attrs={'class': 'form-control', 'placeholder': 'Check-In'},
                                         options={
                                             "format": "DD-MMM-YY",  # moment date-time format
                                             "showClose": False,
                                             "showClear": False,
                                             "showTodayButton": False,
                                         }
                                         ),
            'to_date': DatePickerInput(attrs={'class': 'form-control', 'placeholder': 'Check-Out'},
                                       options={
                                           "format": "DD-MMM-YY",  # moment date-time format
                                           "showClose": False,
                                           "showClear": False,
                                           "showTodayButton": False,
                                       }
                                       ),
            'num_guests': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Guests'})
        }

    def clean(self):
        form_data = self.cleaned_data

        today = datetime.now()
        today = today.replace(hour=0, minute=0, second=0, microsecond=0).date()

        from_date_string = form_data.get('from_date')
        to_date_string = form_data.get('to_date')

        from_date = datetime.strptime(from_date_string, '%d-%b-%y').date()
        to_date = datetime.strptime(to_date_string, '%d-%b-%y').date()

        number_of_guests = form_data.get('num_guests')

        if from_date < today or to_date < today:
            self._errors["Invalid Date"] = "Dates cannot be in past."
            return form_data

        if from_date >= to_date:
            self._errors["Invalid Date"] = "Check-In cannot be greater than or equal to Check-Out."
            return form_data

        if number_of_guests <= 0:
            self._errors["Invalid Guests"] = "Number of guests cannot be negative or zero."
            return form_data

        return form_data

