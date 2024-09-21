from odoo import models, fields

class Ticket(models.Model):
    _name = 'ir.todo.ticket'
    _description = 'Todo Ticket'

    name = fields.Char(string='Name')
    number = fields.Integer(string='Number')
    tag = fields.Char(string='Tag')
    state = fields.Selection([
        ('new', 'New'),
        ('doing', 'Doing'),
        ('done', 'Done')
    ], string='State', default='new')
    description = fields.Text(string='Description')
    file = fields.Binary(string='File')

    def action_new(self):
        print("inside action_new")
        self.state = 'new'

    def action_doing(self):
        print("inside action_confirm")
        self.state = 'doing'

    def action_done(self):
        print("inside action_done")
        self.state = 'done'