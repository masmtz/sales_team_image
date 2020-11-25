# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools import partition, collections, frozendict, lazy_property
from odoo.tools import image_process


class CrmTeam(models.Model):
    _inherit = 'crm.team'
    # _inherit = ['crm.team', 'image.mixin']

    @api.model
    def _get_default_image(self):
        """ Get a default image when the user is created without image

            Inspired to _get_default_image method in
            https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/res/res_partner.py
        """
        image_path = get_module_resource('base', 'static/img', 'avatar.png')
        image = base64.b64encode(open(image_path, 'rb').read())
        return image_process(image, colorize=True)

    image_1920 = fields.Image(
        readonly=False,
        default=_get_default_image,
        store=True)
