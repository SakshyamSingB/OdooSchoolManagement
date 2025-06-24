# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
import json
class SchoolManagement(http.Controller):

    @http.route('/school_management/get_grade', type='json', methods=['POST'], auth='public', csrf=False)
    def fetch_grades(self, **kwargs):
        grades = request.env['grade'].sudo().search([])
        result = []
        for grade in grades:
            result.append({
                "grade": grade.name,
                "teacher": grade.subject_id.name if grade.subject_id else None,
            })
        return {"grades": result}

    @http.route('/school_management/add_grade', type='json', methods=['POST'], auth='public', csrf=False)
    def add_grades(self, **kwargs):
        grade_name = kwargs.get("name")
        grade = request.env['grade'].sudo().create({'name':grade_name})
        students = kwargs.get('students',[])
        
        students_ids = []

        for student in students:
            student_id = student.get('id')
            student_name = student.get('name')
            if student_id:
                student_rec = request.env['res.partner'].sudo().search([('id', '=', student_id)])
                student_rec.update({"grade_id":grade.id})
                if student_rec.grade_id:
                    pass
                else:
                    students_ids.append(student_rec.id)
            else:
                student_add = request.env['res.partner'].sudo().create({'name':student_name,'is_student':True,'grade_id':grade.id})
                students_ids.append(student_add.id)
        for student_id in students_ids:
            students_det = request.env['grade.student.details'].sudo().create({'grade_id':grade.id,'student_id':student_id})

        return {
        'status' : 'success',
        'grade_id': grade.id,
        'grade_name': grade_name,
        'students_added': students_ids
        }
    
 

    @http.route('/school_management/test', type='http', methods=['GET'], auth='public', website=True)
    def test(self, **kwargs):
        return request.render("school_management.add_grade")

    
    @http.route('/school_management/showgrades', type='http', auth='public', website=True)
    def show_grades_page(self, **kwargs):
        # Render your page template
        return request.render('school_management.show_grade_page')

    @http.route('/school_management/api/grades', type='json', auth='public')
    def get_grades(self):
        grades = request.env['grade'].sudo().search([])
        return [{'id': g.id, 'name': g.name} for g in grades]

