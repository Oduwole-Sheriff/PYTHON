from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Customer
from .forms import Payment
import decimal
from django.db import transaction

# Create your views here.

def process_payment(request):

    if request.method == 'POST':

        form = Payment(request.POST)

        if form.is_valid():
            x = form.cleaned_data['payar']
            y = form.cleaned_data['payee']
            z = decimal.Decimal(form.cleaned_data['amount'])

            payar = Customer.objects.select_for_update().get(name=x)
            payee = Customer.objects.select_for_update().get(name=y)

        with transaction.atomic():
            payar.balance -= z
            payar.save()

            payee.balance += z
            payee.save()

            # customer.objects.filter(name=x).update(balance=F('balance') - z)
            # customer.objects.filter(name=y).update(balance=F('balance') + z)

            return HttpResponseRedirect('/')

    else:
        form = Payment()

    return render(request, 'index.html', {'form': form})
