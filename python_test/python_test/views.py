from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from .forms import ClientForm
from .models import Client

# Insert views here
def client_list(request):
    q = Q()
    q_client = request.GET.get('q_client','')
    q_email = request.GET.get('q_email','')
    q_phone = request.GET.get('q_phone','')
    q_suburb = request.GET.get('q_suburb','')
    sort = request.GET.get('sort','')
    order = request.GET.get('order','asc')
    
    if q_client:
        q &= Q(name__contains=q_client)
        
    if q_email:
        q &= Q(email__contains=q_email)
        
    if q_phone:
        q &= Q(phone__contains=q_phone)
        
    if q_suburb:
        q &= Q(address_suburb__contains=q_suburb)

    client_list = Client.objects.filter(q)

    if sort:
        if order == "desc":
            client_list = client_list.order_by('-'+sort)
        else:
            client_list = client_list.order_by(sort)
        
        
    context = {"client_list":client_list,
    "q_client":q_client ,
    "q_email":q_email ,
    "q_phone":q_phone,
    "q_suburb":q_suburb, "sort":sort, "order": 'asc' if order=="desc" else 'desc' }

    return render(request,"clients/list.html", context)

def client_form(request, id=0):
    if request.method == "GET":
        if (id==0):
            form = ClientForm()
        else:
            client = Client.objects.get(pk=id)
            form = ClientForm(instance=client)
        return render(request,"clients/client_form.html", {'form':form})
    else: 
        if (id==0):
            form = ClientForm(request.POST)
        else:
            client = Client.objects.get(pk=id)
            form = ClientForm(request.POST, instance=client)

        if form.is_valid():
            form.save()
            return redirect('/clients')
        else:
            return render(request,"clients/client_form.html", {'form':form})