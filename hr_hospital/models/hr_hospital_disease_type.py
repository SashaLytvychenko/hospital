from odoo import models, fields


class HospitalDisease(models.Model):
    _name = 'hr.hospital.disease.type'
    _description = 'Types of diseases'

    name = fields.Char(string='Name of disease', required=True)
    description = fields.Text(string='Disease description')
    disease_category_ids = fields.Many2many(
        comodel_name='hr.hospital.disease.category',
        relation="hospital_disease_type_hospital_category_reader_rel",
        column1="disease_id",
        column2="category_id",
    )
