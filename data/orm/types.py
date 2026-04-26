import sqlalchemy.types as types
from sqlalchemy import String

from models.color_set import ColorSet
from models.condition import Condition

class ColorSetType(types.TypeDecorator):
    """
    Template taken from https://docs.sqlalchemy.org/en/21/core/custom_types.html
    """
    impl = String
    cache_ok = True

    def process_bind_param(self,
                           value: ColorSet | None,
                           dialect) -> str | None:
        """
        When writing to the database, convert ColorSet to string.
        """
        if value is None:
            return None
        return ",".join(value.to_string_list())
    
    def process_result_value(self,
                             value: str | None,
                             dialect) -> ColorSet | None:
        """
        When reading from the database, convert string to ColorSet.
        """
        if not value:
            return ColorSet()
        return ColorSet.from_string_list(value.split(","))

class ConditionType(types.TypeDecorator):
    """"""
    impl = String
    cache_ok = True

    def process_bind_param(self,
                           value: Condition | None, 
                           dialect) -> str | None:
        """When writing to database, convert Condition to string."""
        if value is None:
            return None
        return value.value
    
    def process_result_value(self,
                             value: str | None,
                             dialect) -> Condition | None:
        """When reading from a database, convert string to Condition."""
        if not value:
            return None
        return Condition(value)