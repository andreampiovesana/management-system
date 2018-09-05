# -*- coding: utf-8 -*-
# Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class MgmtsystemHazardRiskType(models.Model):

    _name = "mgmtsystem.hazard.risk.type"
    _description = "Risk type of the hazard"

    name = fields.Char('Risk Type', size=50, required=True, translate=True)
    description = fields.Text('Description')
