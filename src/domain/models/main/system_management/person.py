"""
    ToDo: DocString
"""
import sqlalchemy as sa
from domain.models.main.base import NamedEntity
from domain.persistence.main import sql_alchemy as db
from application.common.general import BasicSearchParameters


class Person(NamedEntity):
    """ ToDo: DocString """
    last_name = db.Column(db.String(100), default = None)

    @classmethod
    def filter(cls, basic_search_parameters: BasicSearchParameters):
        """ ToDo: DocString """
        query = cls.query.filter(
            sa.cast(cls.uid, sa.String).like(f"%{basic_search_parameters.filter_value}%") |
            cls.name.contains(
                basic_search_parameters.filter_value) | cls.last_name.contains(basic_search_parameters.filter_value)
            ).order_by(
                cls.last_name, cls.name, cls.created_at.desc(), cls.modified_at.desc()
            ).paginate(basic_search_parameters.current_page, basic_search_parameters.page_size)

        return query.items

    @classmethod
    def total_count(cls, basic_search_parameters: BasicSearchParameters):
        """ ToDo: DocString """
        return cls.query.filter(
            sa.cast(cls.uid, sa.String).like(f"%{basic_search_parameters.filter_value}%") |
            cls.name.contains(
                basic_search_parameters.filter_value) | cls.last_name.contains(basic_search_parameters.filter_value)
            ).count()
