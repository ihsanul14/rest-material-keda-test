from odoo import http
from odoo.http import request
from . import constant


class MaterialController():

    @http.route('/api/material', type='json', auth='public', methods=['GET'], csrf=False)
    def get_material(self):
        result = {}
        filter = []
        type_filter = request.httprequest.args.get('type')
        if type_filter:
            filter.append(('type', '=', type_filter))
        try:
            data = []
            raw_data = request.env['material'].sudo().search(filter)
            for i in raw_data:
                d = {}
                d['code'] = i['code']
                d['name'] = i['name']
                d['type'] = i['type']
                d['buy_price'] = i['buy_price']
                d['related_supplier'] = i['related_supplier']
                data.append(d)
            
            result[constant.code] = 200
            result[constant.message] = 'success retrive data'
            result[constant.data] = data
            if len(data) == 0:
                result[constant.code] = 404
                result[constant.message] = 'no data found'
            else:
                result[constant.code] = 200
        except Exception as e:
            result[constant.code] = 500
            result[constant.error] = e
        
        return result

    @http.route('/api/materials', type='json', auth='public', methods=['POST'], csrf=False)
    def create_material(self):
        req = request.jsonrequest
        result = {}
        try:
            if req['buy_price'] < 100:
                result[constant.code] = 400
                result[constant.message] = 'buy_price must be > 100'
            else:    
                request.env['material'].sudo().create(req)
                result[constant.code] = 200
                result[constant.message] = 'success create data'
        except Exception as e:
            result[constant.error] = e
            if 'Wrong value for material.type' in str(e):
                result[constant.code] = 400
            else:
                result[constant.code] = 500

        return result

    @http.route('/api/materiald/<string:id>', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_material(self, id):
        req = request.jsonrequest
        result = {}
        try:
            if req['buy_price'] < 100:
                result[constant.code] = 400
                result[constant.message] = 'buy_price must be > 100'
            else:
                data = request.env['material'].sudo().search([('code', '=', id)])
                data.write(req)    
                result[constant.code] = 200
                result[constant.message] = 'success update data'
        except Exception as e:
            result[constant.error] = e
            if 'Wrong value for material.type' in str(e):
                result[constant.code] = 400
            else:
                result[constant.code] = 500

        return result

    @http.route('/api/materialw/<string:id>', type='json', auth='public', methods=['DELETE'], csrf=False)
    def delete_material(self, id):
        result = {}
        try:
            data = request.env['material'].sudo().search([('code', '=', id)])
            data.unlink()    
            result[constant.code] = 200
            result[constant.message] = 'success delete data'
        except Exception as e:
            result[constant.error] = e
            result[constant.code] = 500
        return result