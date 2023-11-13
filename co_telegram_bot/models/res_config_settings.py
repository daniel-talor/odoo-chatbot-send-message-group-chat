from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    bot_api_token = fields.Char("Bot API Token", config_parameter="co_telegram_bot.bot_api")
