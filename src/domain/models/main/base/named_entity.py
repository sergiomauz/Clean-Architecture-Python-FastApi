"""
    ToDo: DocString
"""
import sqlalchemy as sa
from sqlalchemy import Column, String
from application.common.general import BasicSearchParameters
from .basic_entity_id_uuid import BasicEntity


class NamedEntity(BasicEntity):
    """ ToDo: DocString """
    __abstract__ = True
    name = Column(String(100))

    @classmethod
    def filter(cls, basic_search_parameters: BasicSearchParameters):
        """ ToDo: DocString """
        query = cls.query.filter(
            sa.cast(cls.uid, sa.String).like(f"%{basic_search_parameters.filter_value}%") |
            cls.name.contains(
                basic_search_parameters.filter_value)
            ).order_by(
                cls.name, cls.created_at.desc(), cls.modified_at.desc()
            ).paginate(basic_search_parameters.current_page, basic_search_parameters.page_size)

        return query.items

    @classmethod
    def total_count(cls, basic_search_parameters: BasicSearchParameters):
        """ ToDo: DocString """
        return cls.query.filter(
            sa.cast(cls.uid, sa.String).like(f"%{basic_search_parameters.filter_value}%") |
            cls.name.contains(
                basic_search_parameters.filter_value)
            ).count()
