# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'summary': 'Hospital Management System',
    'description': """This module contains all the common features of Hospital Management System.""",
    'author': "rereasdev",
    'sequence': -100,
    # any module necessary for this one to work correctly
    'depends': ['mail'],
    # always loaded
    'data': [
        # access rights for model
        'security/ir.model.access.csv',
        # views
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
