from django import forms
from .models import NewListing
from bootstrap_datepicker_plus import DatePickerInput
from datetime import datetime

ROOM_CHOICES = (
    ('Private Room', 'Private Room'),
    ('Shared Room', 'Shared Room'),
    ('Entire Place', 'Entire Place'),
)

PROPERTY_CHOICES = (
    ('apartment', 'Apartment'),
    ('condominium', 'Condominium'),
    ('guest_suite', 'Guest Suite'),
    ('house', 'House'),
)


class HostForm(forms.ModelForm):
    room_type = forms.ChoiceField(choices=ROOM_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    property_type = forms.ChoiceField(choices=PROPERTY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = NewListing
        fields = ('name', 'description' , 'house_rules' , 'accommodates' ,
                  'cancellation_policy', 'room_type','property_type','amenities',
                  'picture_url','city', 'state', 'street', 'zip_code', 'start_date', 'end_date', 'price')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of your listing'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': 'Brief description of your listing'}),
            'house_rules': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'House Rules'}),
            'accommodates': forms.NumberInput(attrs={'class': 'form-control',
                                                     'placeholder': 'Enter number of maximum guests'}),
            'cancellation_policy': forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Cancellation Policy of the listing'}),
            'amenities': forms.Textarea(attrs={'class': 'form-control',
                                                'placeholder': 'Amenities offered'
                                                }),
            'picture_url': forms.URLInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Attract guests with a picture'
                                                 }),
            'city': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'City'
                                                }),
            'state': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'State'
                                                }),
            'street': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Street Address'
                                                }),
            'zip_code': forms.NumberInput(attrs={'class': 'form-control',
                                                'placeholder': 'Zip/Postal Code'
                                                }),
            'start_date': DatePickerInput(attrs={'class': 'form-control', 'placeholder': 'Available from date'},
                                          options={
                                                "format": "DD-MMM-YY",  # moment date-time format
                                                "showClose": False,
                                                "showClear": False,
                                                "showTodayButton": False,
                                          }
                                          ),
            'end_date': DatePickerInput(attrs={'class': 'form-control', 'placeholder': 'Available till date'},
                                        options={
                                           "format": "DD-MMM-YY",  # moment date-time format
                                           "showClose": False,
                                           "showClear": False,
                                           "showTodayButton": False,
                                       }
                                       ),
            'price': forms.NumberInput(attrs={'class': 'form-control',
                                                'placeholder': 'Price per night'
                                                }),
        }

    def clean(self):
        form_data = self.cleaned_data

        today = datetime.now()
        today = today.replace(hour=0, minute=0, second=0, microsecond=0).date()
        print(form_data)
        from_date_string = form_data.get('start_date')
        to_date_string = form_data.get('end_date')

        print(from_date_string)

        from_date = datetime.strptime(from_date_string, '%d-%b-%y').date()
        to_date = datetime.strptime(to_date_string, '%d-%b-%y').date()

        if from_date < today or to_date < today:
            self._errors["Invalid Date "] = "Dates cannot be in past."
            return form_data

        if from_date >= to_date:
            self._errors["Invalid Date "] = "Start Date cannot be greater than or equal to To Date."
            return form_data

        return form_data

