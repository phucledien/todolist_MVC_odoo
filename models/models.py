# -*- coding: utf-8 -*-

from odoo import models, fields, api

class todo(models.Model):
    # id để truy xuất đến model
    _name = 'todo.todo' 
    # Trường todo type là Text
    todo = fields.Text('Todo')
    # Trường completed type là Boolean 
    completed = fields.Boolean('Completed?', default=False)