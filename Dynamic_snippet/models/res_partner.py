from odoo import models, fields

class ResPartner(models.Model):
    # _name = 'partner.hightlight'
    _inherit = 'res.partner'

    highlight_partner = fields.Boolean(string="Highlight Partner", default=False)
    partner_id = fields.Many2one("res.partner")