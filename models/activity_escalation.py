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
                    # Notify the user's manager
                    if activity.user_id and activity.user_id.parent_id:
                        manager = activity.user_id.parent_id
                        # Create an additional activity for the manager
                        self.create({
                            'res_id': activity.res_id,
                            'res_model_id': activity.res_model_id.id,
                            'activity_type_id': activity.activity_type_id.id,
                            'summary': 'Recheck Task: ' + activity.summary,
                            'user_id': manager.id,
                            'date_deadline': fields.Date.today() + timedelta(days=3),
                        })
                        # Send a chatter message to the manager
                        activity.message_post(
                            body=f'This activity has been pending for {timespan} days. It has been escalated to your manager {manager.name}.',
                            partner_ids=[manager.partner_id.id]
                        )
