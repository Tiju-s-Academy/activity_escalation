from odoo import models, fields

class ActivityEscalationConfig(models.Model):
    _name = 'activity.escalation.config'
    _description = 'Activity Escalation Configuration'

    first_level_hours = fields.Integer(string='First Level Escalation (hours)', required=True, default=24)
    second_level_days = fields.Integer(string='Second Level Escalation (days)', required=True, default=3)
    third_level_days = fields.Integer(string='Third Level Escalation (days)', required=True, default=7)
