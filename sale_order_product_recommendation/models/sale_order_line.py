# Copyright 2024 Camptocamp
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    # Add database index to improve performance of _recommendable_sale_order_lines_domain
    qty_delivered = fields.Float(
        string="Delivery Quantity",
        compute="_compute_qty_delivered",
        digits="Product Unit of Measure",
        store=True,
        readonly=False,
        copy=False,
        index="btree_not_null",
    )
