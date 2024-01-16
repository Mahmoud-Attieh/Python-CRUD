from django.shortcuts import render, redirect
from . import models
from django.contrib import messages

def exam(request):
    if  'userid' not in request.session:
        return redirect('/')
    context = {
        "user": models.get_user_session(request),
        "exams": models.get_all_exams(),
    }
    return render(request, 'dashboard.html', context)

def add_trip(request):
    if  'userid' not in request.session:
        return redirect('/')
    context = {
        "user": models.get_user_session(request)
    }
    
    return render(request, 'add_trip.html', context)

def add_exam(request):
    errors = models.Exam.objects.exam_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/trips/new')
    else:
        models.add_exam_model(request)
        return redirect('/dashboard')

def render_edit_exam(request, ID):
    if  'userid' not in request.session:
        return redirect('/')
    context = {
        "user": models.get_user_session(request),
        "exams": models.get_all_exams(),
        "exam": models.get_exam(ID)
    }
    return render(request, 'edit_trip.html', context)

def update_exam(request):
    errors = models.Exam.objects.exam_validator(request.POST)
    ID = models.update_exam_model(request)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f'/trips/edit/{ID}'  )
    else:
        ID = models.update_exam_model(request)
        return redirect( f'/trips/{ID}')

def delete_exam(request, uuid):
    models.delete_exam_model(request, uuid)
    return redirect('/dashboard')


def exam_info(request, ID):
    if  'userid' not in request.session:
        return redirect('/')
    context = {
        "user": models.get_user_session(request),
        "exams": models.get_all_exams(),
        "exam": models.get_exam(ID),
    }
    return render(request, 'trip_info.html', context)
