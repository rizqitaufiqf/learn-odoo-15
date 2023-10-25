from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'
    """
        This field must be specified on this form because it doesn't have 'name' field.
        This field determines how the records of a model are displayed in various parts of the Odoo user interface, 
        such as in list views, form views, and search results.
    """
    _rec_name = 'patient_id'

    patient_id = fields.Many2one(comodel_name='hospital.patient', string='Patient')
    ref = fields.Char(string='Reference')
    gender = fields.Selection(string='Gender', related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Datetime(string='Booking Date', tracking=True)
    prescription = fields.Html(string='Prescription')

    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        self.ref = self.patient_id.ref

    @api.onchange('booking_date')
    def _delete_seconds(self):
        if self.booking_date:
            self.booking_date = self.booking_date.replace(second=0, microsecond=0)
