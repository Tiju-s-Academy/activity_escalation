{
    'name': 'Activity Escalation',
    'version': '1.0',
    'summary': 'Escalate activities if they stay incomplete',
    'description': 'This module escalates activities if they stay incomplete and allows configuration of the timespan for escalation.',
    'author': 'Anas',
    'depends': ['base', 'mail'],  # Ensure 'mail' is listed as a dependency
    'data': [
        'security/ir.model.access.csv',
        'views/activity_escalation_views.xml',
        'views/activity_escalation_config_views.xml',
        'views/new_view_file.xml',
        'data/activity_escalation_data.xml',
    ],
    'installable': True,
    'application': True,
}
