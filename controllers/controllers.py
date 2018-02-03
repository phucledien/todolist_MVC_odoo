# -*- coding: utf-8 -*-
from odoo import http
from werkzeug.utils import redirect

class Todo(http.Controller):
    @http.route('/todo/', auth='public')
    def index(self, **kw):
        # Lấy tất cả record của model todo.todo và gán vào list todos
        todos = http.request.env['todo.todo'].search([])
        # Truyền vào view list todos, render và trả về người dùng
        return http.request.render('todo.index', {
            'todos': todos
        })

    @http.route('/todo/add', auth='public')
    def store(self, **kw):
        # Lấy tất cả param người dùng truyền vào
        form_params = http.request.params
        # Lấy ra giá trị param todo và lưu vào biến todo
        todo = form_params['todo']
        # Lấy ra model todo
        todo_model = http.request.env['todo.todo']
        # Dùng ORM api để tạo record todo mới
        todo_model.create({
            'todo': todo
        })
        # Chuyển hướng người dùng về trang todo
        return redirect('/todo')

    # có thể dùng <model("todo.todo"):todo> thay vào id để khỏi search
    @http.route('/todo/complete/<id>', auth='public')
    def toggle(self, id, **kw):
        # Lấy ra record todo với id được truyền vào
        todo = http.request.env['todo.todo'].search([('id', '=', id)])
        # Chuyển đổi trạng thái trường completed
        todo.completed = not todo.completed
        # Chuyển hướng người dùng về trang todo
        return redirect('/todo')

    @http.route('/todo/delete/<id>', auth='public')
    def delete(self, id, **kw):
        # Lấy ra record todo với id được truyền vào        
        todo = http.request.env['todo.todo'].search([('id', '=', id)])
        # Xóa record todo
        todo.unlink()
        # Chuyển hướng người dùng về trang todo
        return redirect('/todo')

    @http.route('/todo/edit/<id>', auth='public')
    def edit(self, id, **kw):
        # Lấy ra record todo với id được truyền vào                
        todo = http.request.env['todo.todo'].search([('id', '=', id)])
        # Truyền record todo vào view edit, render và trả về người dùng    
        return  http.request.render('todo.edit', {
            'todo': todo
        })

    @http.route('/todo/update/<id>', auth='public')
    def update(self, id, **kw):
        # Lấy ra record todo với id được truyền vào                        
        todo = http.request.env['todo.todo'].search([('id', '=', id)])
        # Lấy tất cả param người dùng truyền vào
        form_params = http.request.params
        # Lấy giá trị param todo và gán vào task
        task = form_params['todo']
        # Edit trường todo trong record todo bằng giá trị task vừa lấy
        todo.todo = task
        # Chuyển hướng người dùng về trang todo
        return redirect('/todo')
    
    


#     @http.route('/todo/todo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo.listing', {
#             'root': '/todo/todo',
#             'objects': http.request.env['todo.todo'].search([]),
#         })

#     @http.route('/todo/todo/objects/<model("todo.todo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo.object', {
#             'object': obj
#         })