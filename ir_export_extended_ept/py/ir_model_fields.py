# -*- coding: utf-8 -*-

from openerp import models, fields, api

class irModelFieldEpt(models.Model):
    _name = 'ir.model.field.ept'
    
    model_id = fields.Many2one('ir.model', 'Model')
    field_id = fields.Many2one('ir.model.fields', 'Field')
    field_description = fields.Char(related='field_id.field_description')
    exportable = fields.Boolean('Exportable', default=True)
    export_help = fields.Char('Export Note', size=500)