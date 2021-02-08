from django.shortcuts import render
from.forms import EnqueryD
from.models import ContactDetails
from django.http import HttpResponse
def Enquery_data(request):
    if request.method =="POST":
        eform=EnqueryD(request.POST)
        if eform.is_valid():
            first_name1 = request.POST.get('first_name','')
            last_name1 = request.POST.get('last_name','')
            mobile1 = request.POST.get('mobile','')
            email_id1 = request.POST.get('email_id', '')
            courses1 = request.POST.get('courses','')
            fee1 = request.POST.get('fee','')
            location1 = request.POST.get('location','')
            data = ContactDetails(
                first_name=first_name1,
                last_name=last_name1,
                mobile=mobile1,
                courses=courses1,
                fee=fee1,
                location=location1,
                email_id=email_id1,

            )
            data.save()
            eform = EnqueryD()
            return render(request,'enquery.html',{'eform':eform})
        else:
            return HttpResponse('Invalid Response')
    else:
        eform = EnqueryD()
        return render(request,'enquery.html',{'eform':eform})


