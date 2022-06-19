from django import forms
from .models import Jobs, References, Skills, Roles, Works, Education, Objectives, Address, Details, Duties

class DetForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = {'pic','fname','lname','email','phone', 'author'}

        widgets = {
            'author': forms.TextInput(attrs= {'id':'elder', 'placeholder':'username', 'type':'hidden'})
        }
    
class ObjForm(forms.ModelForm):
    class Meta:
        model = Objectives
        fields = {'car', 'author'}

        widgets = {
            'car': forms.Textarea(attrs= {'style':'width: 100%', 'placeholder': 'STATE YOUR CAREER OBJECTIVES. NOTE THIS IS OPTIONAL'}),
            'author': forms.TextInput(attrs= {'id':'elder', 'placeholder':'username', 'type':'hidden'})
        }

class RefForm(forms.ModelForm):
    class Meta:
        model = References
        fields = {'name','firm','tel','email', 'author'}

        widgets = {
            'author': forms.TextInput(attrs= {'id':'elder', 'placeholder':'username', 'type':'hidden'})
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = {'names', 'author'}

        widgets = {
            'author': forms.TextInput(attrs= {'id':'elder', 'placeholder':'username', 'type':'hidden'})
        }

class WorkForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = {'name','location','start','end', 'author'}

        widgets = {
            'author': forms.TextInput(attrs= {'id':'elder', 'placeholder':'username', 'type':'hidden'})
        }

class EduForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = {'inst','location','start','end','cert', 'author'}

        widgets = {
            'author': forms.TextInput(attrs= {'id':'elder', 'placeholder':'username', 'type':'hidden'})
        }

class AddForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = {'snum','stname','lgname','state', 'author'}

        widgets = {
            'author': forms.TextInput(attrs= {'id':'elder', 'placeholder':'username', 'type':'hidden'})
        }

