from odoo import fields, models


class saleRank(models.Model):
    _name = 'sale.rank'
    _description = 'Sale Rank'
    _auto = False
    _order = 'wkn_categ_id asc,rank asc'

    wkn_categ_id = fields.Many2one(
        'product.category',
        string='Category',
    )
    category_name = fields.Char(
        string='Category name',
        related='wkn_categ_id.name'
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product',
    )
    name = fields.Char(
        string='Product name',
        related="product_id.name"
    )
    product_uom_qty = fields.Float(
        string='qty',
    )
    rank = fields.Integer(
        string='Rank',
    )

    def update_sale_rank(self):
        self._cr.execute('REFRESH MATERIALIZED VIEW %s' % self._table)

    def init(self):
        self._cr.execute('DROP MATERIALIZED VIEW IF EXISTS %s' % self._table)

        query = """
            CREATE MATERIALIZED VIEW %s AS (
               select pc.wkn_categ_id as wkn_categ_id, pp.id,
                      pp.id as product_id, sum(l.product_uom_qty) as product_uom_qty,
                      rank() OVER (PARTITION BY pc.wkn_categ_id ORDER BY sum(l.product_uom_qty) ASC)
                FROM product_product pp
                join product_template pt on pp.product_tmpl_id = pt.id
                Join sale_order_line l on l.product_id = pp.id
                Join sale_order so on l.order_id = so.id
                join product_category pc on pc.id = pt.categ_id
                WHERE date_order >= date_trunc('month', current_date - interval '1' month)
                    and date_order < date_trunc('month', current_date)
                    and so.state not in ('draft','cancel')
                    and pt.type = 'product'
                group by pp.id,pc.wkn_categ_id

            )
        """ % self._table
        self._cr.execute(query)
