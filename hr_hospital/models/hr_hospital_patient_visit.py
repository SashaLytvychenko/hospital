from odoo import models, fields

class HospitalPatientVisit(models.Model):
    _name = 'hr.hospital.patient.visit'
    _description = 'Patient visits'


    patient_id = fields.Many2one(comodel_name= 'hr.hospital.patient', string="Patient", required=True)
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor', string='Treating doctor', required=True)
    disease_id = fields.Many2one(comodel_name='hr.hospital.disease.type', string="Disease")
    visit_date = fields.Datetime(string="Visit Date", required=True)
    prescription = fields.Text(string="Prescription")