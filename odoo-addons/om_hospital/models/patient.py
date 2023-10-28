# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date of Birth', tracking=True)
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True, group_operator='avg')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', tracking=True, default='male')
    active = fields.Boolean(string='Active', default=True)
    appointment_ids = fields.One2many(comodel_name='hospital.appointment', inverse_name="patient_id",
                                      string='Hospital Appointment id')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = date.today()
                record.age = today.year - record.date_of_birth.year - (
                        (today.month, today.day) < (record.date_of_birth.month, record.date_of_birth.day))
            else:
                record.age = 0
