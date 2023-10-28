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
    """ 
        if fields is One2many, you must specify _ids in the end of column name 
        and the primary id of the model as inverse_name (ex: appointment_id)
        also, don't forget to define inverse_name (ex: appointment_id) as Many2one on the source model
    """
    pharmacy_detail_ids = fields.One2many(comodel_name='hospital.appointment.pharmacy.details', inverse_name='appointment_id',
                                          string="Pharmacy Details")
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Very High')], string='Priority', default='0', tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', default='draft', tracking=True)
    doctor_id = fields.Many2one(comodel_name='res.users', string='Doctor', tracking=True)

    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        self.ref = self.patient_id.ref

    @api.onchange('booking_date')
    def _delete_seconds(self):
        if self.booking_date:
            self.booking_date = self.booking_date.replace(second=0, microsecond=0)

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_redraft(self):
        for rec in self:
            rec.state = 'draft'


class AppointmentPharmacyDetails(models.Model):
    _name = 'hospital.appointment.pharmacy.details'
    _description = 'Hospital Appointment pharmacy details'

    product_id = fields.Many2one(comodel_name='product.product', string='Product', required=True)
    price_unit = fields.Float(related="product_id.list_price", string='Price Unit')
    qty = fields.Integer(string='Quantity', default=1)
    """
        define inverse_name Many2one on this column regarding One2many field of the defined One2many model
    """
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Hospital Appointment id')
