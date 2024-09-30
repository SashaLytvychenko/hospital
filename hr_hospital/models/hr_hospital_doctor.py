from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _inherit = 'hr.hospital.person'
    _description = 'Doctor'

    email = fields.Char()
    specialization = fields.Selection([('pediatrics', 'Pediatrics'),
                                       ('pathology', 'Pathology'),
                                       ('psychiatry', 'Psychiatry')],
                                      default='pediatrics')
    is_intern = fields.Boolean(
    )
    doctor_mentor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        domain="[('id', '!=', id), ('is_intern', '=', False)]",
    )
