from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'

    patient_id = fields.Many2one(comodel_name='hospital.patient', string='Patient')
    gender = fields.Selection(string='Gender', related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Datetime(string='Booking Date', tracking=True)

