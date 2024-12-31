from odoo import models, fields, api
from datetime import timedelta

class Activity(models.Model):
    _inherit = 'mail.activity'

    escalation_level = fields.Integer(default=0)

    @api.model
    def escalate_activities(self):
        config = self.env['activity.escalation.config'].search([], limit=1)
        if config:
            first_level_hours = config.first_level_hours
            second_level_days = config.second_level_days
            third_level_days = config.third_level_days
            activities = self.search([('state', '=', 'open')])
            for activity in activities:
                time_since_creation = fields.Datetime.now() - activity.create_date
                if activity.escalation_level == 0 and time_since_creation > timedelta(hours=first_level_hours):
                    activity.escalation_level = 1
                    self._escalate_to_manager(activity, first_level_hours, 'hours')
                elif activity.escalation_level == 1 and time_since_creation > timedelta(days=second_level_days):
                    activity.escalation_level = 2
                    self._escalate_to_manager(activity, second_level_days, 'days')
                elif activity.escalation_level == 2 and time_since_creation > timedelta(days=third_level_days):
                    activity.escalation_level = 3
                    self._escalate_to_manager(activity, third_level_days, 'days')

    def _escalate_to_manager(self, activity, timespan, unit):
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
                body=f'This activity has been pending for {timespan} {unit}. It has been escalated to your manager {manager.name}.',
                partner_ids=[manager.partner_id.id]
            )
