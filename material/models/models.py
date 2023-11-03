from odoo import fields, models

class Material(models.Model):
    _name = 'material'
    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Code must be unique per Items!'),
    ]
    code = fields.Char(string='Code',required=True, index=True)
    name = fields.Char(string='Name')
    type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton'),
    ], string='Type')
    buy_price = fields.Float(string='Buy Price',default=100)
    related_supplier = fields.Selection([('supplier 1', 'Supplier 1')], string='Related Supplier')
