from odoo import models, fields
from odoo.osv import expression


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    picking_state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting', 'Waiting Another Operation'),
        ('confirmed', 'Waiting'),
        ('assigned', 'Ready'),
        ('partial', 'Partial'),
        ('not_picking', 'Not picking'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'), ],
        string='Picking state',
        compute='_compute_picking_states',
        search='_search_picking_states'
    )

    def _compute_picking_states(self):
        for order in self:
            if not len(order.picking_ids):
                order.picking_state = 'not_picking'
            else:
                states = list(set([x.state for x in order.picking_ids]))
                if len(states) == 1:
                    order.picking_state = states[0]
                else:
                    order.picking_state = 'partial'

    def _search_picking_states(self, operator, value):
        negative = operator in expression.NEGATIVE_TERM_OPERATORS

        # In case we have no value
        if not value:
            return expression.TRUE_DOMAIN if negative else expression.FALSE_DOMAIN
        #partial
        if value == 'not_pickings':
            return [('picking_ids', operator, False)]

        return [('picking_ids.state', operator, value)]
