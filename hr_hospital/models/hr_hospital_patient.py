from odoo import models, fields

class HospitalPatient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Doctor'

    name = fields.Char(string='Name', required=True)
    date_birth = fields.Date(string='Date of birth')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string="Gender", default='male')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    doctor_id = fields.Many2one(comodel_name = 'hr.hospital.doctor', string = 'Treating doctor')



