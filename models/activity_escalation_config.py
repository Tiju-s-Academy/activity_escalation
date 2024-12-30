from odoo import models, fields

class ActivityEscalationConfig(models.Model):
    _name = 'activity.escalation.config'
    _description = 'Activity Escalation Configuration'

    timespan = fields.Integer(string='Escalation Timespan (days)', required=True, default=7)
