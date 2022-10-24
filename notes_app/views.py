
from django.shortcuts import render, redirect 
from django.http import HttpResponse, FileResponse
from .models import Notes
from django.db.models.aggregates import Count
from django.contrib import messages
from . forms import AddNewNoteForm, UpdateNoteForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date




import io
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import A4




# Function Based Views
def notes_list(request):
    notes_list= Notes.objects.all().order_by('-created_at')
    total_notes = Notes.objects.aggregate(notes = Count('id'))
    context = {'notes': notes_list, 'total_notes': total_notes}
    return render(request,'notes_app/notes_list.html', context)

# Today Notes filter
def notes_list_today(request):
    today = date.today()
    notes_list= Notes.objects.filter(created_at__icontains=today).order_by('-created_at')
    total_notes = Notes.objects.filter(created_at__icontains=today).aggregate(notes = Count('id'))
    context = {'notes': notes_list, 'total_notes': total_notes}
    return render(request,'notes_app/notes_list.html', context)


# This Week Notes filter
def notes_this_week(request):
    from datetime import datetime, timedelta
    one_week_ago = datetime.today() - timedelta(days=7)
    notes_list= Notes.objects.filter(created_at__gte=one_week_ago).order_by('-created_at')
    total_notes = Notes.objects.filter(created_at__gte=one_week_ago).aggregate(notes = Count('id'))
    context = {'notes': notes_list, 'total_notes': total_notes}
    return render(request,'notes_app/notes_list.html', context)

# This Month Notes filter
def notes_this_month(request):
    from datetime import datetime, timedelta
    one_month_ago = datetime.today() - timedelta(days=30)
    notes_list= Notes.objects.filter(created_at__gte=one_month_ago).order_by('-created_at')
    total_notes = Notes.objects.filter(created_at__gte=one_month_ago).aggregate(notes = Count('id'))
    context = {'notes': notes_list, 'total_notes': total_notes}
    return render(request,'notes_app/notes_list.html', context)


# This Month Notes filter
def notes_this_year(request):
    from datetime import datetime, timedelta
    one_month_ago = datetime.today() - timedelta(days=365)
    notes_list= Notes.objects.filter(created_at__gte=one_month_ago).order_by('-created_at')
    total_notes = Notes.objects.filter(created_at__gte=one_month_ago).aggregate(notes = Count('id'))
    context = {'notes': notes_list, 'total_notes': total_notes}
    return render(request,'notes_app/notes_list.html', context)

def note_details(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request, "notes_app/note_details.html", context={"note":note})




def NoteViewPdf(request, pk):
    note = Notes.objects.get(pk=pk)
    
    pdf_buffer = io.BytesIO()
    my_doc = SimpleDocTemplate(pdf_buffer, pagesizes=A4)
    
    flowables = []
    sample_style_sheet = getSampleStyleSheet()
    
    note_title = Paragraph(note.title, sample_style_sheet['Heading1'])
    # note_created_at = Paragraph(note.created_at, sample_style_sheet['Heading2'])
    note_body = Paragraph(note.body, sample_style_sheet['BodyText'])
    
    
    flowables.append(note_title)
    # flowables.append(note_created_at)
    flowables.append(note_body)
    
    my_doc.build(flowables)
    pdf_buffer.seek(0)
    
    return FileResponse(pdf_buffer, as_attachment=False, filename=f'{note.title}.pdf')



@login_required(login_url='member_login')
def NoteGetPdf(request, pk):
    note = Notes.objects.get(pk=pk)
    
    pdf_buffer = io.BytesIO()
    my_doc = SimpleDocTemplate(pdf_buffer, pagesizes=A4)
    
    simple_style_sheet = getSampleStyleSheet()
    
    flowables = []
    
    note_title = Paragraph(note.title, simple_style_sheet['Heading1'])
    # note_created_at = Paragraph(note.created_at, simple_style_sheet['Heading2'])
    note_body = Paragraph(note.body, simple_style_sheet['BodyText'])
    
    
    
    flowables.append(note_title)
    # flowables.append(note_created_at)
    flowables.append(note_body)
    
    my_doc.build(flowables)
    
    pdf_buffer.seek(0)
    return FileResponse(pdf_buffer, as_attachment=True, filename=f'{note.title}.pdf')





@login_required(login_url='member_login')
def add_note(request):
    if request.method == 'POST':
        form = AddNewNoteForm(request.POST)
        if form.is_valid():
            new_note = form.save()
            messages.add_message(request, messages.SUCCESS, 'New note added successfully!')
            return redirect('notes_list')
        else:
            messages.add_message(request, messages.WARNING, 'Something went wrong, try again!')
            return redirect('add_note')
    else:
        form = AddNewNoteForm()
        context = {'form': form}
        return render(request, 'notes_app/add_note.html', context)
    
    

@login_required(login_url='member_login')  
def update_note(request, pk):
    note = Notes.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateNoteForm(request.POST or None, instance=note)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Note updated successfully!')
            return redirect('notes_list')
            
        else:
            messages.add_message(request, messages.WARNING, 'Something went wrong, try again!')
            return redirect('upadte_note', pk=pk)
        
    else: 
        form = UpdateNoteForm(instance=note)
        
    return render(request, 'notes_app/update_note.html', context={'form': form, 'note': note})




@login_required(login_url='member_login')
def delete_note(request, pk):
    note = Notes.objects.get(pk=pk)
    
    if request.method == "POST":
        note.delete()
        return redirect('notes_list')
    else:
        context = {'note': note}
        return render(request, 'notes_app/delete_note.html', context)
    
    

@login_required(login_url='member_login')   
def delete_all_notes(request):
    if request.method == "POST":
        notes = Notes.objects.all().delete()
        messages.add_message(request, messages.SUCCESS, "All notes are deleted!" )
        return redirect('notes_list')
    else:
        return render(request, 'notes_app/delete_all_notes.html')
    