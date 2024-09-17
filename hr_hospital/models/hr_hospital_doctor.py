from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctor'

    name = fields.Char(string='Name', required=True)
    date_birth = fields.Date(string='Date of birth')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    specialization = fields.Selection([('pediatrics', 'Pediatrics'),
                                       ('pathology', 'Pathology'),
                                       ('psychiatry', 'Psychiatry')],
                                      default='pediatrics',
                                      string='Specialization')

