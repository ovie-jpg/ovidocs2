from cgitb import html
from PyPDF2 import pdf
from django import template
from django.shortcuts import render, get_object_or_404
from django.template import context
from requests import request
from .models import Jobs, References, Skills, Roles, Works, Education, Objectives, Address, Details, Duties
from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from .forms import AddForm, DetForm, EduForm, ObjForm, RefForm, SkillForm, WorkForm
from django.contrib import messages
from django.http import HttpResponse, response, FileResponse
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.contrib.auth.models import User
import os
from django.conf import settings
from django.contrib.staticfiles import finders
from io import BytesIO

# Create your views here.
# def cv1_pdf(request):
#     #create a bytestream buffer
#     buf = io.BytesIO()
#     #create a canvas
#     c = canvas.Canvas(buf, pagesize= letter, bottomup= 0)
#     #create text object
#     textob = c.beginText()
#     textob.setTextOrigin(inch, inch)
#     # textob.setFont("none", 13)

#     add some lines of text
#     dets = Details.objects.all()
#     adds = Address.objects.all()
#     objs = Objectives.objects.all()
#     edus = Education.objects.all()
#     works = Works.objects.all()
#     skills = Skills.objects.all()
#     refs = References.objects.all()
    
#     Lines = []

#     for det in dets:
#         Lines.append(det.pic)
#         Lines.append(det.fname)
#         Lines.append(det.lname)
#         Lines.append(det.email)
#         Lines.append(det.phone)
#         Lines.append(det.author)
    
#     lines2 = []

#     for add in adds:
#         lines2.append(add.snum)
#         lines2.append(add.stname)
#         lines2.append(add.lgname)
#         lines2.append(add.state)
#         lines2.append(add.author)
    
#     lines3 = []

#     for obj in objs:
#         lines3.append(obj.car)
#         lines3.append(obj.author)
    
#     lines4 = []

#     for edu in edus:
#         lines4.append(edu.inst)
#         lines4.append(edu.location)
#         lines4.append(edu.start)
#         lines4.append(edu.end)
#         lines4.append(edu.cert)
#         lines4.append(edu.author)
    
#     lines5 = []

#     for work in works:
#         lines5.append(work.name)
#         lines5.append(work.location)
#         lines5.append(work.start)
#         lines5.append(work.end)
#         lines5.append(work.author)
    
#     lines6 = []

#     for skill in skills:
#         lines6.append(skill.names)
#         lines6.append(skill.author)
    
#     lines7 = []

#     for ref in refs:
#         lines7.append(ref.name)
#         lines7.append(ref.firm)
#         lines7.append(ref.tel)
#         lines7.append(ref.email)
#         lines7.append(ref.author)
    
    
    
    
#     #finish up
#     c.drawText(textob)
#     c.showPage()
#     c.save()
#     buf.seek(0)

    

#     #return something
#     return FileResponse(buf, as_attachment= True, filename= "cv1.pdf")
    
# def link_callback(uri, rel):
#             """
#             Convert HTML URIs to absolute system paths so xhtml2pdf can access those
#             resources
#             """
#             result = finders.find(uri)
#             if result:
#                     if not isinstance(result, (list, tuple)):
#                             result = [result]
#                     result = list(os.path.realpath(path) for path in result)
#                     path=result[0]
#             else:
#                     sUrl = settings.STATIC_URL        # Typically /static/
#                     sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
#                     mUrl = settings.MEDIA_URL         # Typically /media/
#                     mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

#                     if uri.startswith(mUrl):
#                             path = os.path.join(mRoot, uri.replace(mUrl, ""))
#                     elif uri.startswith(sUrl):
#                             path = os.path.join(sRoot, uri.replace(sUrl, ""))
#                     else:
#                             return uri

#             # make sure that file exists
#             if not os.path.isfile(path):
#                     raise Exception(
#                             'media URI must start with %s or %s' % (sUrl, mUrl)
#                     )
#             return path


# def cv_render_pdf_view(request):
#     # template_path = 'cv1.html'
    
#     dets = Details.objects.all()
#     adds = Address.objects.all()
#     objs = Objectives.objects.all()
#     edus = Education.objects.all()
#     works = Works.objects.all()
#     skills = Skills.objects.all()
#     refs = References.objects.all()
    
#     context = {
#         'dets': dets,
#         'adds': adds,
#         'objs': objs,
#         'edus': edus,
#         'works': works,
#         'skills': skills,
#         'refs': refs
#         }
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#     # find the template and render it.
#     # template = get_template(template_path)
#     html = render_to_string('cv1.html', context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#        html, dest=response, link_callback=link_callback)
#     # if error then show some funny view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response

# def render_pdf(template_src, context_dict):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type= 'application/pdf')
#     return HttpResponse('We had some errors <pre>' + html + '</pre>')

# def cv1_pdf(request):
#     dets = Details.objects.all()
#     return render_pdf('cv1.html', {'dets':dets})

def cv3_render_pdf_view(request):
    dets = Details.objects.all()
    adds = Address.objects.all()
    objs = Objectives.objects.all()
    edus = Education.objects.all()
    works = Works.objects.all()
    skills = Skills.objects.all()
    refs = References.objects.all()
    template_path = 'cv3.html'
    context = {
        'dets': dets,
        'adds': adds,
        'objs': objs,
        'edus': edus,
        'works': works,
        'skills': skills,
        'refs': refs
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    


def home(request):
    jobs = Jobs.objects.all()
    return render(request,'home.html', {'jobs': jobs})

def information(request, id):
    context = {'jobs': get_object_or_404(Jobs, pk=id)}
    return render(request, 'information.html', context)

def listy(request):
    dets = Details.objects.all()
    adds = Address.objects.all()
    objs = Objectives.objects.all()
    edus = Education.objects.all()
    works = Works.objects.all()
    skills = Skills.objects.all()
    refs = References.objects.all()
    return render(request, 'listy.html', {'dets':dets, 'adds':adds, 'objs':objs, 'edus': edus, 'works':works, 'skills':skills, 'refs':refs})

def updet(request):
    dets = Details.objects.all()
    return render(request, 'updet.html', {'dets': dets})



def cvgen(request):
    dets = Details.objects.all()
    adds = Address.objects.all()
    objs = Objectives.objects.all()
    edus = Education.objects.all()
    works = Works.objects.all()
    skills = Skills.objects.all()
    refs = References.objects.all()
    return render(request, 'cvgen.html', {'dets': dets, 'adds':adds, 'objs':objs, 'edus': edus, 'works':works, 'skills':skills, 'refs':refs})

def cv1(request):
    dets = Details.objects.all()
    adds = Address.objects.all()
    objs = Objectives.objects.all()
    edus = Education.objects.all()
    works = Works.objects.all()
    skills = Skills.objects.all()
    refs = References.objects.all()
    return render(request, 'cv1.html', {'dets': dets, 'adds':adds, 'objs':objs, 'edus': edus, 'works':works, 'skills':skills, 'refs':refs})

def cv2(request):
    return render(request, 'cv2.html')

def cv3(request):
    return render(request, 'cv3.html')

def cv4(request):
    return render(request, 'cv4.html')

def cv5(request):
    return render(request, 'cv5.html')

class HomeView(ListView):
    template_name = 'home.html'
    model = Jobs
    context_object_name = 'jobs'


class InfoDetailView(DetailView):
    template_name = 'information.html'
    model = Jobs
    context_object_name = 'jobs'

class DetView(CreateView):
    template_name= 'updet.html'
    model = Details
    form_class= DetForm
    def warn(self, request):
        dets= Details.objects.all()
        if dets.count == 1:
            messages.info(request, 'details submitted, click next')
        return render(request, {'dets':dets})

class AddView(CreateView):
    template_name= 'updet2.html'
    model = Address
    form_class = AddForm

class ObjView(CreateView):
    template_name= 'updet3.html'
    model= Objectives
    form_class= ObjForm

class EduView(CreateView):
    template_name= 'updet4.html'
    model = Education
    form_class = EduForm

class WorkView(CreateView):
    template_name= 'updet5.html'
    model = Works
    form_class = WorkForm

class SkillView(CreateView):
    template_name= 'updet6.html'
    model = Skills
    form_class = SkillForm

class RefView(CreateView):
    template_name= 'updet7.html'
    model = References
    form_class = RefForm


    