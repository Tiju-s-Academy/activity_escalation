{
    'name': 'Escalations',
    'version': '1.0',
    'summary': 'Escalate activities if they stay incomplete',
    'description': 'This module escalates activities if they stay incomplete and allows configuration of the timespan for escalation.',
    'author': 'Anas',
    'depends': ['base', 'mail'],
    'data': [
        'security/activity_escalation_security.xml',
        'security/ir.model.access.csv',
        'views/activity_escalation_views.xml',
        'views/activity_escalation_config_views.xml',
        'data/activity_escalation_data.xml',
    ],
    'images': ['static/description/icon-hi.png'],
    'installable': True,
    'application': True,
}
