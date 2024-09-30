from datetime import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hr.hospital.patient'
    _inherit = 'hr.hospital.person'
    _description = 'Patient'

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Treating doctor',
    )
    date_birth = fields.Date(
        string='Date of birth')
    age = fields.Integer(
        compute='_compute_age',
        store=True
    )
    email = fields.Char(
    )
    passport_code = fields.Char(
    )
    contact_person_ids = fields.Many2many(
        comodel_name='res.partner')

    @api.constrains('date_birth')
    def _check_date_birth(self):
        for rec in self:
            if rec.date_birth and rec.date_birth > fields.Date.today():
                raise ValidationError(
                    f'You cannot enter birth date more than today date:'
                    f' {fields.Date.today()}')

    @api.depends('date_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_birth:
                today = datetime.today()
                birth_date = rec.date_birth
                age = today.year - birth_date.year
                if ((today.month, today.day) <
                        (birth_date.month, birth_date.day)):
                    age -= 1
                rec.age = age
            else:
                rec.age = 0
