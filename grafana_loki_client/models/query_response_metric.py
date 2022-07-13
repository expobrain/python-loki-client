from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.query_response_metric_level import QueryResponseMetricLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryResponseMetric")


@attr.s(auto_attribs=True)
class QueryResponseMetric:
    """
    Attributes:
        level (Union[Unset, QueryResponseMetricLevel]):
    """

    level: Union[Unset, QueryResponseMetricLevel] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        level: Union[Unset, str] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if level is not UNSET:
            field_dict["level"] = level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _level = d.pop("level", UNSET)
        level: Union[Unset, QueryResponseMetricLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = QueryResponseMetricLevel(_level)

        query_response_metric = cls(
            level=level,
        )

        query_response_metric.additional_properties = d
        return query_response_metric

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
