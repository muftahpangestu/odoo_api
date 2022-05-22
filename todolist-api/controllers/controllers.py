# -*- coding: utf-8 -*-
import xmlrpclib
from json import dumps as json
from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import serialize_exception

class Todolist_api(http.Controller):
    @http.route('/todolist-api/todolist-api/', auth='public')
    def index(self, **kw):
        return "Hello, world"
    
    @http.route('/todolist-api/restful', type='http', auth='none', csrf=False)
    @serialize_exception
    def restful(self, **post):
        filecontent = {}
        if post.get('login') and post.get('password'):
           if not post.get('database'): #If no database is passed on the ajax post, get one random database
              from odoo.service.db import list_dbs
              post['database'] = list_dbs()[0]
           login = request.session.authenticate(post['database'], post['login'], post['password'])
           if not login: #If login doesn't return uid, return json with status denied
              filecontent['status'] = 'denied'
              return request.make_response(json(filecontent), [('Access-Control-Allow-Origin', '*')])
           filecontent = request.env['res.users'].search([]).read() #If login successful, you can execute functions and access datas
        if not filecontent: #If no data filled in the dict, return error
           filecontent = {'status': 'error'}
        return request.make_response(json(filecontent), [('Access-Control-Allow-Origin', '*')])

    @http.route('/todolist-api/return-smth', type='http', auth='none', csrf=False)
    @serialize_exception
    def return_something(self,**post):
        if post.get('text'):
            output ={
                "message":"success",
                "text":post.get('text')
            }
        else:
            output ={
                "message":"failed"
            }
        return request.make_response(json(output))
    
    @http.route('/todolist-api/get-all', type='http', auth='none', csrf=False)
    @serialize_exception
    def get_all(self, **post):
        filecontent = {}
        if post.get('login') and post.get('password'):
           if not post.get('database'): #If no database is passed on the ajax post, get one random database
              from odoo.service.db import list_dbs
              post['database'] = list_dbs()[0]
           login = request.session.authenticate(post['database'], post['login'], post['password'])
           if not login: #If login doesn't return uid, return json with status denied
              filecontent['status'] = 'denied'
              return request.make_response(json(filecontent), [('Access-Control-Allow-Origin', '*')])
           filecontent = request.env['todo.list'].search([]).read() #If login successful, you can execute functions and access datas
        if not filecontent: #If no data filled in the dict, return error
           filecontent = {'status': 'error'}
        return request.make_response(json(filecontent), [('Access-Control-Allow-Origin', '*')])
    
    @http.route('/todolist-api/add', type='http', auth='none', csrf=False)
    @serialize_exception
    def add_todo(self, **post):
        filecontent = {}
        if post.get('login') and post.get('password'):
           if not post.get('database'): #If no database is passed on the ajax post, get one random database
              from odoo.service.db import list_dbs
              post['database'] = list_dbs()[0]
           login = request.session.authenticate(post['database'], post['login'], post['password'])
           if not login: #If login doesn't return uid, return json with status denied
              filecontent['status'] = 'denied'
              return request.make_response(json(filecontent), [('Access-Control-Allow-Origin', '*')])
           data = {
               "description": post.get('description'),
               "customer_id": post.get('customer_id'),
               "time": post.get('time')
           } 
           try:
               request.env['todo.list'].sudo().create(data) #If login successful, you can execute functions and access datas
               filecontent ={"status":"success"}
           except:
              filecontent ={"status":"failed"}
        return request.make_response(json(filecontent), [('Access-Control-Allow-Origin', '*')])
      
    @http.route('/todolist-api/delete', type='http', auth='none', csrf=False)
    @serialize_exception
    def delete_todo(self, **post):
        filecontent = {}
        if post.get('login') and post.get('password'):
           if not post.get('database'): #If no database is passed on the ajax post, get one random database
              from odoo.service.db import list_dbs
              post['database'] = list_dbs()[0]
           login = request.session.authenticate(post['database'], post['login'], post['password'])
           if not login: #If login doesn't return uid, return json with status denied
              filecontent['status'] = 'denied'
              return request.make_response(json(filecontent), [('Access-Control-Allow-Origin', '*')])
           try:
               todo_id = post.get('id')
               request.env['todo.list'].search([('id','=',todo_id)]).unlink() #If login successful, you can execute functions and access datas
               filecontent ={"status":"success"}
           except:
              filecontent ={"status":"failed"}
        return request.make_response(json(filecontent), [('Access-Control-Allow-Origin', '*')])
      
    @http.route('/todolist-api/editDesc', type='http', auth='none', csrf=False)
    @serialize_exception
    def editdesc_todo(self, **post):
        filecontent = {}
        if post.get('login') and post.get('password'):
           if not post.get('database'): #If no database is passed on the ajax post, get one random database
              from odoo.service.db import list_dbs
              post['database'] = list_dbs()[0]
           login = request.session.authenticate(post['database'], post['login'], post['password'])
           if not login: #If login doesn't return uid, return json with status denied
              filecontent['status'] = 'denied'
              return request.make_response(json(filecontent), [('Access-Control-Allow-Origin', '*')])

           data = {
               "description": post.get('description')
           } 
           todo_id = int(post.get('id'))
           request.env['todo.list'].browse(todo_id).write(data) #If login successful, you can execute functions and access datas
           filecontent ={"status":"success"}
         
        return request.make_response(json(filecontent), [('Access-Control-Allow-Origin', '*')])

#    @http.route('/todolist-api/get-all/', type='http', auth='none', csrf=False)
#    @serialize_exception
#    def get_all(self, **post):
#        res ={}
#        if post.get('some'):
#            res = request.env['todo.list'].search([]).read()
#            if not res:
#                res = {'status':'error'}
#        else:
#            res = {'status':'error'}

#        return request.make_response(json(res), [('Access-Control-Allow-Origin', '*')])
    



#     @http.route('/todolist-api/todolist-api/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todolist-api.listing', {
#             'root': '/todolist-api/todolist-api',
#             'objects': http.request.env['todolist-api.todolist-api'].search([]),
#         })

#     @http.route('/todolist-api/todolist-api/objects/<model("todolist-api.todolist-api"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todolist-api.object', {
#             'object': obj
#         })

