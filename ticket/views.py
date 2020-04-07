from django.http import Http404,HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import *
def show_dates(request):
    selected_dates = Date.objects.all()
    context = {'date': selected_dates}
    return render(request, 'base.html', context)
def show_ticket(request,pk):
    print(Date.objects.get(pk=pk).date)
    project = Ticket.objects.filter(
    ticdate = Date.objects.get(pk=pk).date,
    ticbooked = False,

    )
    # print(list(project))
    
    context = {
        'selected_tickets': project,
        'current' : request.user

    }
    return render(request, 'ticket.html', context)
    
def book_ticket(request,tk):
    get_ticket = Ticket.objects.get(pk=tk)
    print(request.user,get_ticket.ticbooked)
    get_ticket.ticuser = request.user
    get_ticket.ticbooked = True
    get_ticket.save()
    # return HttpResponse("You're ticket booked.")
    return HttpResponseRedirect(reverse('ticket:index', args=())) 
     
