from django.shortcuts import render
from django.http.response import HttpResponse
from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import Widget



# Create your views here.
class FormNums(forms.Form):
    num4 = forms.IntegerField(widget= forms.NumberInput,
                              help_text="a NumberRR")
    
    def clean (self):
        data = super(FormNums,self).clean()
        try:
            num = int(data['num4'])
        except:
            raise ValidationError("Int is require")
        return data
    
def conver_int(number):
    result =0
    try:
        result = int(number)
    except:
        pass
    return result 

def home(request,num1, num2):
    num4 = 0
    num3 = conver_int(request.GET.get('num3','0'))
    
    if request.method == 'POST':
        form = FormNums(request.POST)
        if form.is_valid():
       # num4 = conver_int(request.POST.get('num4','0'))
         num4 = conver_int(form.cleaned_data['num4'])
    else:
        form = FormNums()
                      
   # print (request.GET)
    
   # print(type(num1))
    result = int(num1)+ int(num2)+ num3 +num4
    return render(request, 'home.html',{
        'result':result,
        'values':[num1,num2,num3],
        'form':form#FormNums()
    }) 
    #return HttpResponse("Hola a Todos %d" %(result,))