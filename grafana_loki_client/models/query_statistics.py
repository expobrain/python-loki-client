from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.query_statistics_ingester import QueryStatisticsIngester
from ..models.query_statistics_querier import QueryStatisticsQuerier
from ..models.query_statistics_summary import QueryStatisticsSummary

T = TypeVar("T", bound="QueryStatistics")


@attr.s(auto_attribs=True)
class QueryStatistics:
    """
    Attributes:
        summary (QueryStatisticsSummary):
        querier (QueryStatisticsQuerier):
        ingester (QueryStatisticsIngester):
    """

    summary: QueryStatisticsSummary
    querier: QueryStatisticsQuerier
    ingester: QueryStatisticsIngester
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        summary = self.summary.to_dict()

        querier = self.querier.to_dict()

        ingester = self.ingester.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "summary": summary,
                "querier": querier,
                "ingester": ingester,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        summary = QueryStatisticsSummary.from_dict(d.pop("summary"))

        querier = QueryStatisticsQuerier.from_dict(d.pop("querier"))

        ingester = QueryStatisticsIngester.from_dict(d.pop("ingester"))

        query_statistics = cls(
            summary=summary,
            querier=querier,
            ingester=ingester,
        )

        query_statistics.additional_properties = d
        return query_statistics

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
