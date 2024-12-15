from odoo import http
from odoo.http import request

class WhatsappController(http.Controller):
    @http.route('/whatsapp/webhook', type='json', auth='public', methods=['POST'])
    def handle_incoming_message(self, **kwargs):
    #     message = kwargs.get('message')
    #     phone_number = kwargs.get('phone_number')
        
    #     # Process the incoming message here, e.g., create a log, send an automated reply, etc.
    #     request.env['whatsapp.integration'].create({
    #         'message': message,
    #         'phone_number': phone_number,
    #     })
        return {'status': 'ok'}
