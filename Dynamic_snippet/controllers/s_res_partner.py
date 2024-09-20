import json
from odoo import http
from odoo.http import request


class PartnerHighlightController(http.Controller):
    @http.route('/partners/highlighted', methods=['POST'], type='json', auth="none", csrf=False)
    def highlighted_partners(self):
                partners = request.env['res.partner'].sudo().search([('highlight_partner', '=', True)])
                partner_data = [{'name': partner.name} for partner in partners]
                print(partner_data)
                return  partner_data

                # if partners:
                #     return request.make_json_response({
                #         partner_data
                #          # "name":partners.name,
                #          # "id":partners.partner_id
                #                })



