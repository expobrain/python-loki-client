from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.query_response_data_result_type import QueryResponseDataResultType
from ..models.query_response_result import QueryResponseResult
from ..models.query_statistics import QueryStatistics

T = TypeVar("T", bound="QueryResponseData")


@attr.s(auto_attribs=True)
class QueryResponseData:
    """
    Attributes:
        result_type (QueryResponseDataResultType):
        result (List[QueryResponseResult]):
        stats (QueryStatistics):
    """

    result_type: QueryResponseDataResultType
    result: List[QueryResponseResult]
    stats: QueryStatistics
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result_type = self.result_type.value

        result = []
        for result_item_data in self.result:
            result_item = result_item_data.to_dict()

            result.append(result_item)

        stats = self.stats.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resultType": result_type,
                "result": result,
                "stats": stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        result_type = QueryResponseDataResultType(d.pop("resultType"))

        result = []
        _result = d.pop("result")
        for result_item_data in _result:
            result_item = QueryResponseResult.from_dict(result_item_data)

            result.append(result_item)

        stats = QueryStatistics.from_dict(d.pop("stats"))

        query_response_data = cls(
            result_type=result_type,
            result=result,
            stats=stats,
        )

        query_response_data.additional_properties = d
        return query_response_data

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
