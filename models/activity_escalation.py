from odoo import models, fields, api
from datetime import timedelta

class Activity(models.Model):
    _inherit = 'mail.activity'

    escalation_level = fields.Integer(default=0)

    @api.model
    def escalate_activities(self):
        config = self.env['activity.escalation.config'].search([], limit=1)
        if config:
            timespan = config.timespan
            activities = self.search([('state', '=', 'open')])
            for activity in activities:
                if activity.create_date + timedelta(days=timespan) < fields.Datetime.now():
                    activity.escalation_level += 1
                    # Add your escalation logic here (e.g., notify manager)
