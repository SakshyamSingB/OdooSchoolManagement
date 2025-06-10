from odoo import models, fields, api

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean()
    is_teacher = fields.Boolean()
    grade_id = fields.Many2many('grade')

    @api.onchange("grade_id")
    def _onchange_grade(self):
        self.grade_id = self.grade_id.name

class Subject(models.Model):
    _name = 'subject'

    name = fields.Char(string="Subject Name")
    teacher_id = fields.Many2many('res.partner', string="Teacher", domain=[('is_teacher', '=', True)])
    grade_id = fields.Many2one('grade', string="Grade")


class Grade(models.Model):
    _name = 'grade'

    name = fields.Char(string="Grade Name")
    student_id = fields.Many2many('res.partner', string="Student", domain=[('is_student', '=', True)])
