from email.policy import default

from odoo import models, fields

class HospitalDoctor(models.Model):
    _name = 'hr.hospital.disease.type'
    _description = 'Types of diseases'

    name = fields.Char(string ='Name of disease', required = True)
    description = fields.Text(string = 'Disease description')
    disease_category = fields.Selection([
        ('infectious', 'Infectious'),
        ('allergic', 'Allergic'),
        ('mental', 'Mental'),
    ], default = 'allergic',  string="Disease category", required=True)
