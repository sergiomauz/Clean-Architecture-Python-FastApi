"""
    ToDo: DocString
"""
import uuid
import datetime
from typing import List
import sqlalchemy as sa
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID as db_uuid
from common.utils import convert_to_uuid
from domain.persistence.main import Base
from application.common.general import BasicSearchParameters


class BasicEntityIdInt(Base):
    """ ToDo: DocString """
    __abstract__ = True
    uid = Column(db_uuid(as_uuid = True), primary_key = True, index = True, default = uuid.uuid1())
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    disabled_at = Column(DateTime)

    @classmethod
    def get_by_uid(cls, str_uid: str):
        """ ToDo: DocString """
        uid = convert_to_uuid(str_uid)

        if uid is not None:
            try:
                return cls.query.get(uid)
            except Exception:
                return None

        return None

    @classmethod
    def get_list_by_uids(cls, uids_list: List[str]):
        """ ToDo: DocString """
        return cls.query.filter(cls.uid.in_(uids_list)).all()

    @classmethod
    def filter(cls, basic_search_parameters: BasicSearchParameters):
        """ ToDo: DocString """
        query = cls.query.filter(
            sa.cast(cls.uid, sa.String).like(f"%{basic_search_parameters.filter_value}%")
            ).order_by(
                cls.created_at.desc(), cls.modified_at.desc()
            ).paginate(basic_search_parameters.current_page, basic_search_parameters.page_size)

        return query.items

    @classmethod
    def delete_list_by_uids(cls, uids_list: List[str]):
        """ ToDo: DocString """
        cls.query.filter(cls.uid.in_(uids_list)).delete()
        db.session.commit()

    @classmethod
    def total_count(cls, basic_search_parameters: BasicSearchParameters):
        """ ToDo: DocString """
        return cls.query.filter(
            sa.cast(cls.uid, sa.String).like(f"%{basic_search_parameters.filter_value}%")
            ).count()

    def save(self):
        """ ToDo: DocString """
        if self.uid is None:
            self.uid = uuid.uuid1()
            self.created_at = datetime.datetime.now()
            db.session.add(self)
        else:
            self.modified_at = datetime.datetime.now()
            db.session.merge(self)
        db.session.commit()
