{

    'name': 'Hospital',
    'version': '17.0.1.0.0',
    'author': 'Sasha Lytvychenko',
    'website': 'https://odoo.school/',
    'category': 'Customizations',
    'license': 'OPL-1',
    'depends': [
        'base',
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menu.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_patient_views.xml',
        'views/hr_hospital_patient_visit_views.xml',
        'views/hr_hospital_disease_type_views.xml',
        'data/hr_hospital_disease_type.xml',

    ],
    'demo': [
        'demo/hr_hospital_doctor_demo.xml',
        'demo/hr.hospital.patient.csv',

    ],

    'installable': True,
    'auto_install': False,
    'images': [
        'static/description/icon.png'
    ]

}
