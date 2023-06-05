# in unit_converter/views.py

from django.shortcuts import render
from pint import UnitRegistry
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)


def convert(request):
    
    if request.method == 'POST':
        from_unit = request.POST['from_unit']
        to_unit = request.POST['to_unit']
        value = float(request.POST['value'])
        
        if from_unit == 'celsius' and to_unit == 'fahrenheit':
            result = value * 9/5 + 32
        elif from_unit == 'fahrenheit' and to_unit == 'celsius':
            result = (value - 32) * 5/9
        elif from_unit == 'kilometers' and to_unit == 'miles':
            result = value / 1.609
        elif from_unit == 'miles' and to_unit == 'kilometers':
            result = value * 1.609
        elif from_unit == 'second' and to_unit =='hour':
            result=value/3600
        else:
            result = None
        return render(request, 'unit_converter/convert.html', {'result': result, 'from_unit':from_unit,'to_unit':to_unit,'value':value})
    return render(request, 'unit_converter/convert.html')
