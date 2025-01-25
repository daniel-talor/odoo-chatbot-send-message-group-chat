from odoo import models, fields

class GroupChat(models.Model):
    _name = "co.group.chat"

    name = fields.Char(string="Name")
    chat_id = fields.Char(string="Chat ID")