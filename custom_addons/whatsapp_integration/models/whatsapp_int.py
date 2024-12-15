from odoo import models, fields, api
import requests

class WhatsappIntegration(models.Model):
    _name = 'whatsapp_int.model'
    _description = 'WhatsApp Integration'

    message = fields.Text('Message')
    phone_number = fields.Char('Phone Number')

    # def send_whatsapp_message(self):
    #     url = "https://api.your-whatsapp-api-provider.com/sendMessage"  # Replace with the API URL
    #     payload = {
    #         'phone': self.phone_number,
    #         'message': self.message,
    #     }
    #     headers = {
    #         'Authorization': 'Bearer YOUR_API_TOKEN',  # Add API token or any other authentication header
    #     }

    #     response = requests.post(url, data=payload, headers=headers)
    #     if response.status_code == 200:
    #         return True
    #     else:
    #         return False

    