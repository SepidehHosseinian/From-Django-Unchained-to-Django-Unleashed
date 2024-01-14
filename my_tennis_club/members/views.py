from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  #  mydata = Member.objects.all()
  #  mydata = Member.objects.all().values()
  #  mydata = Member.objects.values_list('firstname')
   mydata = Member.objects.filter(firstname='Emil').values()
   template = loader.get_template('template.html')
   context = {
    'mymembers': mydata,
  }
   return HttpResponse(template.render(context, request))
 
  # mymembers = Member.objects.all().values()
  # template = loader.get_template('template.html')
  # context = {
  #   'greeting':2,
  #   'mymembers': mymembers,
  # }
   #context = {
  # 'var1': 'John',
  #}
  # return HttpResponse(template.render(context, request))
  