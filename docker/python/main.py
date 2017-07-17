# -*- coding: utf-8 -*-
# sample.py
import falcon
import json

class ItemsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        items = {
            'title': 'Python+FalconでWebAPI',
            'tags': [
                {
                    'name': 'Python','versions':[]
                },
                {
                    'name': 'Falcon','vresions':[]
                }
            ]
        }

        resp.body = json.dumps(items,ensure_ascii=False)

app = falcon.API()
app.add_route('/items', ItemsResource())
