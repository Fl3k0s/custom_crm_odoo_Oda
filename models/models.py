from odoo import models, fields, api


class Visit(models.Model):
     _name = 'custom_crm.visit'
     _description = 'Visit'

     cif = fields.Char(string='Cif Empresa')
     empresa = fields.Char(string='Nombre Empresa')
     type = fields.Selection([('B', 'Bebida'), ('C', 'Comida'), ('PL', 'Producto de limpieza'), ('PVC','Producto de venta al cliente'),
                              ('UC','Utensilios de cocina')], string = 'Tipo de producto', required=True)
     queVende = fields.Char(string='Que vende')
     phone = fields.Char(string='Telefono')
     fixedPhone = fields.Char(string='Telefono fijo')
     mail = fields.Char(string='Correo electronico')
     provincia = fields.Char(string='provincia')

     def toggle_state(self):
          self.done = not self.done

     def toggle_exportPdf(self):
          self.done = not self.done