from django.db import models
from login_app.models import User, Validator

class Exam(models.Model):
    destination = models.CharField(max_length=255)
    itineray = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user = models.ForeignKey(User, related_name='exams', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validator()

def add_exam_model(request):
    user = User.objects.get(id=request.session['userid'])
    exam_destination = request.POST['destination']
    exam_itineray = request.POST['itineray']
    exam_start_date = request.POST['start_date']
    exam_end_date = request.POST['end_date']
    Exam.objects.create(destination = exam_destination, itineray = exam_itineray, start_date = exam_start_date, end_date = exam_end_date, user = user)

def update_exam_model(request):
    ID = request.POST['exam_id']
    exam = Exam.objects.get(id = ID)
    exam_destination = request.POST['destination']
    exam_itineray = request.POST['itineray']
    exam_start_date = request.POST['start_date']
    exam_end_date = request.POST['end_date']

    exam.destination = exam_destination
    exam.itineray = exam_itineray
    exam.start_date = exam_start_date
    exam.end_date = exam_end_date
    exam.save()
    return ID
    
def get_all_exams():
    return Exam.objects.all()

def get_exam(ID):
    return Exam.objects.get(id = ID)

def get_user_session(request):
    return User.objects.get(id=request.session['userid'])

def delete_exam_model(request, uuid):
    exam = Exam.objects.get(id = uuid)
    exam.delete()
