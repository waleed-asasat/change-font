# -*- coding: utf-8 -*-

from odoo import models, fields


class ChangeFont(models.Model):
    _inherit = "res.users"

    SELF_WRITEABLE_FIELDS = ['signature', 'action_id', 'company_id', 'email', 'name', 'image_1920', 'lang', 'tz',
                             'font_family']

    # Add new fonts here (add fonts names)
    font_family = fields.Selection([('Cairo', 'Cairo')], default="Cairo", string="Font", required=True)
