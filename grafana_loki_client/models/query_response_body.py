from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.query_response_data import QueryResponseData

T = TypeVar("T", bound="QueryResponseBody")


@attr.s(auto_attribs=True)
class QueryResponseBody:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'My test API key'}

    Attributes:
        status (str):  Example: success.
        data (QueryResponseData):
    """

    status: str
    data: QueryResponseData
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status")

        data = QueryResponseData.from_dict(d.pop("data"))

        query_response_body = cls(
            status=status,
            data=data,
        )

        query_response_body.additional_properties = d
        return query_response_body

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
