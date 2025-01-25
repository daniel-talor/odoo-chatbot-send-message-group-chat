
import requests, logging

from odoo import models
from pip._internal.exceptions import NetworkConnectionError

_logger = logging.getLogger(__name__)


class Task(models.Model):
    _inherit = "project.task"

    def _get_message_to_send(self, init_values, message):
        for field_name, old_value in init_values.items():
            new_value = self[field_name]

            if old_value != new_value:
                field_label = self._fields[field_name].string
                if isinstance(old_value, models.Model):
                    message += f"{field_label}: {old_value.name} -> {new_value.name}\n"
                else:
                    message += f"{field_label}: {old_value} -> {new_value}\n"

        return message

    def send_message(self, init_values):
        api_token = self.env["ir.config_parameter"].sudo().get_param("co_telegram_bot.bot_api")

        if not api_token:
            return

        session = requests.Session()
        user_name = self.env.user.name
        user_modify = f"{user_name} has made the following changes:\n"
        message = self._get_message_to_send(init_values, user_modify)

        if message:
            for group_chat in self.project_id.group_chat_ids:
                try:
                    title = f"Message sent to chat {group_chat.name}: {group_chat.chat_id}\n"
                    response = session.post(
                        f"https://api.telegram.org/bot{api_token}/sendMessage", 
                        json={
                            "chat_id": group_chat.chat_id.strip(),
                            "text": title + message
                        }
                    )
                    response.raise_for_status()

                    _logger.info(f"Message sent to chat {group_chat.chat_id}:\n{message}")
                except NetworkConnectionError as exc:
                    assert exc.response
                    logger.critical(
                        "HTTP error %s while getting %s",
                        exc.response.status_code,
                        url,
                    )
                    raise
                except Exception as e:
                    _logger.error(f"Error sending message: {e}")
                    raise

    def _track_subtype(self, init_values):
        if self.project_id.group_chat_ids:
            self.send_message(init_values)
        return super(Task, self)._track_subtype(init_values)
