# -*- coding: utf-8 -*-
from odoo import http


class ChangeFont(http.Controller):
    @http.route('/font/selected', type="json", auth='public')
    def get_selected(self, **kw):
        user_id = http.request.uid
        users = http.request.env['res.users']

        font_family = users.search([('id', '=', user_id)], limit=1).font_family

        return font_family
