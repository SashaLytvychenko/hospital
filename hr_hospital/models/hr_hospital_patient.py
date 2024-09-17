from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Doctor'

    name = fields.Char(required=True)
    date_birth = fields.Date(string='Date of birth')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], default='male')
    phone = fields.Char()
    email = fields.Char()
    doctor_id = (
        fields.Many2one(comodel_name='hr.hospital.doctor',
                        string='Treating doctor'))
