# -*- coding:utf-8 -*-

import json

from flask import request
from core import app
from core.models.coupon import Coupon

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/coupon')
def get_member_coupon():
    member_id = request.args.get('member_id', 0)
    member_id = int(member_id)
    coupons = Coupon.get_member_coupon(member_id)

    coupons_data = [c.to_dict() for c in coupons]

    return json.dumps(coupons_data)
