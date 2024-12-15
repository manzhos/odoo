from odoo import fields, models, api, _


class InstagramIntegrate(models.Model):
    _name = 'inst_int.model'
    _description = 'Instagram Integration'

    name = fields.Char(string='Name', required=True)
    description = fields.Char(string='Description')

    