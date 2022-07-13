from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.query_response_metric import QueryResponseMetric
from ..models.query_response_streams import QueryResponseStreams
from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryResponseResult")


@attr.s(auto_attribs=True)
class QueryResponseResult:
    """
    Attributes:
        value (List[str]):
        metric (Union[Unset, QueryResponseMetric]):
        streams (Union[Unset, QueryResponseStreams]):
    """

    value: List[str]
    metric: Union[Unset, QueryResponseMetric] = UNSET
    streams: Union[Unset, QueryResponseStreams] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value

        metric: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metric, Unset):
            metric = self.metric.to_dict()

        streams: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.streams, Unset):
            streams = self.streams.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if metric is not UNSET:
            field_dict["metric"] = metric
        if streams is not UNSET:
            field_dict["streams"] = streams

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = cast(List[str], d.pop("value"))

        _metric = d.pop("metric", UNSET)
        metric: Union[Unset, QueryResponseMetric]
        if isinstance(_metric, Unset):
            metric = UNSET
        else:
            metric = QueryResponseMetric.from_dict(_metric)

        _streams = d.pop("streams", UNSET)
        streams: Union[Unset, QueryResponseStreams]
        if isinstance(_streams, Unset):
            streams = UNSET
        else:
            streams = QueryResponseStreams.from_dict(_streams)

        query_response_result = cls(
            value=value,
            metric=metric,
            streams=streams,
        )

        query_response_result.additional_properties = d
        return query_response_result

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
