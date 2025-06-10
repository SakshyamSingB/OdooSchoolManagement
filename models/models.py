# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class ../school_mangement(models.Model):
#     _name = '../school_mangement.../school_mangement'
#     _description = '../school_mangement.../school_mangement'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Grade(models.Model):
    _name = "grade"

    name = fields.Char()
    student_details_id = fields.One2many('grade.student.details', 'grade_id')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            pass
        res = super().create(vals_list)
        for each in res.student_details_id:
            each.student_id.update({"grade_id":res.id})
        return res


class ResPartnerInherit(models.Model):
    _inherit = "res.partner"

    is_student = fields.Boolean(default=False)
    grade_id = fields.Many2one('grade')


class GradeStudentDetails(models.Model):
    _name = "grade.student.details"

    grade_id = fields.Many2one('grade')
    student_id = fields.Many2one('res.partner')
    notes = fields.Char()