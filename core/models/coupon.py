# -*- coding:utf-8 -*-

import time

from core import db
from .base import BaseShardingModel


__all__ = ["Coupon"]


class Coupon(BaseShardingModel):
    """
    Coupon model with table sharding.
    """
    __tablename__ = 'tip_coupon'
    __bind_key__ = "coupon_db"
    __table_args__ = {"mysql_engine": "InnoDB", "mysql_charset": "utf8"}

    _mapper = {}

    id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    coupon_id = db.Column(db.BigInteger, nullable=False, default=0)
    member_id = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.Integer, nullable=False, default=0)
    start_time = db.Column(db.BigInteger, nullable=False, default=0)
    end_time = db.Column(db.BigInteger, nullable=False, default=0)
    create_time = db.Column(db.BigInteger, nullable=False, default=0)

    @staticmethod
    def get_property_list():
        return ['coupon_id', 'member_id', 'status', 'start_time', 'end_time',
                'create_time']

    def to_dict(self):
        return {
            'id': self.id,
            'couponId': self.coupon_id,
            'memberId': self.member_id,
            'status': self.status,
            'startTime': self.start_time,
            'endTime': self.end_time,
            'createTime': self.create_time
        }

    @classmethod
    def create_coupon(cls, **kwargs):
        member_id = kwargs.get("member_id")
        model = cls.rehash(member_id)
        now = time.time()
        kwargs['create_time'] = now
        kwargs['status'] = 0
        coupon = model()
        for key in cls.get_property_list():
            setattr(coupon, key, kwargs.get(key))
        db.session.add(coupon)
        db.session.commit()

    @classmethod
    def get_member_coupon(cls, member_id):
        model = cls.rehash(member_id)
        coupons = model.query.filter_by(member_id=member_id).all()

        return coupons
