from odoo import models, fields

class Project(models.Model):
    _inherit = "project.project"

    group_chat_ids = fields.Many2many("co.group.chat", string="Group chat")
