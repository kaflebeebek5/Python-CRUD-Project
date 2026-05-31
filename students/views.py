from django.db import connection
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
import json


@method_decorator(csrf_exempt, name='dispatch')
class StudentView(APIView):

    # LIST  →  GET /api/students/
    def get(self, request):
        with connection.cursor() as cur:
            cur.execute("SELECT * FROM students")
            cols = [col[0] for col in cur.description]
            rows = [dict(zip(cols, row)) for row in cur.fetchall()]
        return JsonResponse(rows, safe=False)

    # CREATE  →  POST /api/students/
    def post(self, request):
        body = json.loads(request.body)

        with connection.cursor() as cur:
            cur.execute(
                "SELECT insert_student(%s, %s, %s, %s)",
                [body['name'], body['address'], body['age'], body['created_by']]
            )
            

        return JsonResponse({'message': 'Student created'}, status=201)

class StudentDetailView(APIView):

    # RETRIEVE  →  GET /api/students/<id>/
    def get(self, request, studentid):
        with connection.cursor() as cur:
            cur.execute("SELECT * FROM students WHERE studentid = %s", [studentid])
            row = cur.fetchone()
            if not row:
                return JsonResponse({'error': 'Student not found'}, status=404)
            cols = [col[0] for col in cur.description]
            student = dict(zip(cols, row))
        return JsonResponse(student)

    # UPDATE  →  PUT /api/students/<id>/
    def post(self, request):
        body = json.loads(request.body)

        with connection.cursor() as cur:
            cur.execute(
                "SELECT update_student(%s, %s, %s, %s, %s)",
                [body['studentid'], body['name'], body['address'], body['age'], body['modified_by']]
            )
            

        return JsonResponse({'message': 'Student updated'})

    # DELETE  →  DELETE /api/students/<id>/
    def delete(self, request, studentid):
        with connection.cursor() as cur:
            cur.execute("DELETE FROM students WHERE studentid = %s", [studentid])
        return JsonResponse({'message': 'Student deleted'}) 

class CourseView(APIView):

    # LIST  →  GET /api/courses/
    def get(self, request):
        with connection.cursor() as cur:
            cur.execute("SELECT * FROM courses")
            cols = [col[0] for col in cur.description]
            rows = [dict(zip(cols, row)) for row in cur.fetchall()]
        return JsonResponse(rows, safe=False)
    
    # CREATE  →  POST /api/courses/
    def post(self, request):    
        body = json.loads(request.body)

        with connection.cursor() as cur:
            cur.execute(
                "INSERT INTO courses (coursename) VALUES (%s)",
                [body['coursename']]
            )
            

        return JsonResponse({'message': 'Course created'}, status=201)

class EnrollmentView(APIView):

    # CREATE  →  POST /api/enrollments/
    def post(self, request):    
        body = json.loads(request.body)

        with connection.cursor() as cur:
            cur.execute(
                "INSERT INTO enrollments (studentid, courseid) VALUES (%s, %s)",
                [body['studentid'], body['courseid']]
            )
            

        return JsonResponse({'message': 'Enrollment created'}, status=201)
    
    def get(self, request):
        with connection.cursor() as cur:
            cur.execute("SELECT * FROM enrollments")
            cols = [col[0] for col in cur.description]
            rows = [dict(zip(cols, row)) for row in cur.fetchall()]
        return JsonResponse(rows, safe=False)
    



    
