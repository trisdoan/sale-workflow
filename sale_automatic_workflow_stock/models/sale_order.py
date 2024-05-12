# Copyright 2011 Akretion Sébastien BEAU <sebastien.beau@akretion.com>
# Copyright 2013 Camptocamp SA (author: Guewen Baconnier)
# Copyright 2016 Sodexis
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class SaleOrder(models.Model):
    """Extend to add stock related workflow."""

    _inherit = "sale.order"

    @api.depends("partner_id", "user_id", "workflow_process_id")
    def _compute_team_id(self):  # pylint: disable=W8110
        super()._compute_team_id()
        if self.workflow_process_id.picking_policy:
            self.picking_policy = self.workflow_process_id.picking_policy
