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
     image = fields.Binary(string='imagen')
     done = fields.Boolean(string="Realizado")

     def toggle_state(self):
          self.done = not self.one

     def toggle_exportPdf(self):
          self.done = not self.done

     def f_create(self):
          visit = {
               'cif':'A12345678B',
               'empresa':'Pepote SL',
               'type':'B',
               'queVende':'Cocacola',
               'phone':'655876942',
               'fixedPhone': '918703203',
               'mail':'pepoteSL@pepote.es',
               'provincia':'Madrid',
               'done': False
          }
          print(visit)
          self.env['custom_crm.visit'].create(visit)

     def f_search_update(self):
          visit = self.env['custom_crm.visit'].search([('cif', '=', 'A12345678B')])
          print('search()', visit, visit.cif)

          visit_b = self.env['custom_crm.visit'].browse([15])
          print('browse',visit_b.cif)

          visit.write({
               'cif': 'A12345678B'
          })

     def f_delete(self):
          visit = self.env['custom_crm.visit'].browse([17])
          visit.unlink()

class VisitReport(models.AbstractModel):

     _name='report.custom_crm.report_visit_card'

     @api.model
     def _get_report_values(self,docids,data=None):
          report_obj = self.env['ir.action.report']
          report = report_obj._get_report_from_name('custom_crm.report_visit_card')
          return {
               'doc_ids':docids,
               'doc_model':self.env['custom_crm.visit'],
               'docs':self.env['custom_crm.visit'].browse(docids)
          }