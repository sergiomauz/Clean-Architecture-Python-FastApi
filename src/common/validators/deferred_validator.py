"""
    ToDo: DocString
"""


from typing import TypeVar, Dict, Any, Generic, Type
from pydantic import BaseModel


T = TypeVar("T", bound=BaseModel)


class DeferrableValidator(Generic[T]):
    """ ToDo: DocString """

    def __init__(self, type_: Type[T], kwargs: Dict[str, Any]):
        """ ToDo: DocString """
        self.type_ = type_
        self.kwargs = kwargs

    def validate(self) -> T:
        """ ToDo: DocString """
        return self.type_(**self.kwargs)

    def __repr__(self):
        """ ToDo: DocString """
        return f"{type(self).__name__}(type_={self.type_.__name__}, kwargs={self.kwargs})"


class DeferredValidator(BaseModel):
    """ ToDo: DocString """

    class Config:
        """ ToDo: DocString """
        arbitrary_types_allowed = True

    @classmethod
    def create_instance(cls: Type[T], **kwargs: Any) -> DeferrableValidator[T]:
        """ ToDo: DocString """
        return DeferrableValidator(cls, kwargs)
