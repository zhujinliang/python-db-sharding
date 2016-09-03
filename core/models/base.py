# -*- coding:utf-8 -*-

from core import app
from core import db


class CouponBaseModel(object):
    _mapper = {}

    @classmethod
    def rehash(cls, hash_id):
        sharding_num = app.config['SHARDING_NUM']
        cls_name = cls.__tablename__ + "_" + str(hash_id % sharding_num)
        model_class = cls._mapper.get(cls_name)
        if not model_class:
            model_class = type(
                cls_name,
                (cls, db.Model),
                {'__tablename__': cls_name,
                 '__bind_key__': cls.__bind_key__,
                 '__table_args__': cls.__table_args__})
        cls._mapper[cls_name] = model_class

        return model_class
