from odoo import models, fields, api

class ReceptionVehicle(models.Model):
    _name = 'reception.vehicle'
    _description = 'Reception of Vehicles'

    name = fields.Char(string='Vehicle Plate', required=True)
    client_id = fields.Many2one('res.partner', string='Client', required=True, domain="[('customer','=',True)]")
    service_id = fields.Many2one('product.product', string='Service', domain="[('type','=','service')]")
    reception_date = fields.Datetime(string='Reception Date', default=fields.Datetime.now)
    vehicle_details = fields.Text(string='Vehicle Details')
    phone = fields.Char(string='Contact Phone', related='client_id.phone', store=True)
    email = fields.Char(string='Contact Email', related='client_id.email', store=True)

    @api.onchange('client_id')
    def _onchange_client_id(self):
        if self.client_id:
            self.phone = self.client_id.phone
            self.email = self.client_id.email
