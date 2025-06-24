from odoo import models, fields, api

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean()
    is_teacher = fields.Boolean()
    grade_id = fields.Many2one('grade')

class Subject(models.Model):
    _name = 'subject'

    name = fields.Char(string="Subject Name")
    teacher_id = fields.Many2many('res.partner', string="Teacher", domain=[('is_teacher', '=', True)])
    grade_id = fields.Many2one('grade', string="Grade")


class Grade(models.Model):
    _name = 'grade'
    
    name = fields.Char(string="Grade Name")
    student_details_id = fields.One2many('grade.student.details', 'grade_id')
    subject_id = fields.One2many('subject','grade_id',string="Subject")
    context = fields.Boolean(default=0)

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        for each in res.student_details_id:
            each.student_id.update({"grade_id":res.id})
        return res
    
    def write(self, vals_list):
        res = super().write(vals_list)
        for each in self.student_details_id:
            each.student_id.update({"grade_id":self.id})
        return res

class GradeStudentDetails(models.Model):
    _name = "grade.student.details"

    grade_id = fields.Many2one('grade')
    student_id = fields.Many2one('res.partner')
    notes = fields.Char()


# class SubjectTeacherDetails(models.Model):
#     _name = "subject.teacher.details"

#     subject_id = fields.Many2one('subject')
#     teacher_id = fields.Many2one('res.partner')
#     notes = fields.Char()