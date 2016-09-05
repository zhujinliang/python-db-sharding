# -*- coding:utf-8 -*-

import json
import time

from sqlalchemy import or_, and_, func

from core import db
from core.commons import enum
from coupon_base import CouponBaseModel
from coupon_service.const import COUPON_STATUS_EXPIRED
from coupon_service.const import COUPON_STATUS_USED
from coupon_service.const import COUPON_STATUS_USING
from coupon_service.const import COUPON_STATUS_NOT_USED
from coupon_service.const import MEMBER_TYPE_BANK_DEPOSIT
from coupon_service.const import MEMBER_TYPE_PLATFORM
from coupon_service.const import MEMBER_TYPE_SUPPLIER
from coupon_service.const import MEMBER_TYPE_TRANSPORTER
from coupon_service.const import MEMBER_TYPE_OUT_DEPOSIT
from coupon_service.const import MEMBER_TYPE_JD_USER
from coupon_service.const import MEMBER_TYPE_DAOJIA_SUPPLIER


__all__ = ["TipCoupon"]


class Coupon(CouponBaseModel):
    __tablename__ = 'tip_coupon'
    __bind_key__ = "coupon_service_db"
    __table_args__ = {"mysql_engine": "InnoDB", "mysql_charset": "utf8"}

    _mapper = {}

    MEMBER_TYPE = enum(TRANSPORTER=MEMBER_TYPE_TRANSPORTER,
                       SUPPLIER=MEMBER_TYPE_SUPPLIER,
                       PLATFORM=MEMBER_TYPE_PLATFORM,
                       BANK_DEPOSIT=MEMBER_TYPE_BANK_DEPOSIT,
                       OUT_DEPOSIT=MEMBER_TYPE_OUT_DEPOSIT,
                       DAOJIA_SUPPLIER=MEMBER_TYPE_DAOJIA_SUPPLIER,
                       JD_USER=MEMBER_TYPE_JD_USER)
    STATUS = enum(NOT_USED=COUPON_STATUS_NOT_USED,
                  USING=COUPON_STATUS_USING,
                  USED=COUPON_STATUS_USED,
                  EXPIRED=COUPON_STATUS_EXPIRED)
    EXPIRED_TYPE = enum(NOT_EXPIRED=1, START_END_TIME=2)
    id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    # 优惠券id
    coupon_id = db.Column(db.BigInteger, nullable=False, default=0)
    rule_id = db.Column(db.BigInteger, nullable=False, default=0)
    # 优惠描述
    desc = db.Column(db.String(128), nullable=False, default="")
    # 优惠标题
    content = db.Column(db.String(32), nullable=False, default="")
    # 用户类型
    member_type = db.Column(db.Integer, nullable=False, default=0)
    # 用户id
    member_id = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.Integer, nullable=False, default=0)
    amount = db.Column(db.Float, nullable=False, default=0)
    expired_type = db.Column(db.Integer, nullable=False, default=0)
    # 开始时间
    start_time = db.Column(db.BigInteger, nullable=False, default=0)
    # 结束时间
    end_time = db.Column(db.BigInteger, nullable=False, default=0)
    # 发放时间
    give_time = db.Column(db.BigInteger, nullable=False, default=0)
    create_time = db.Column(db.BigInteger, nullable=False, default=0)
    modify_time = db.Column(db.BigInteger, nullable=False, default=0)
    # 优惠券使用规则
    rule = db.Column(db.String(2048), nullable=False, default="")
