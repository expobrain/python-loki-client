from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.query_statistics_store import QueryStatisticsStore
from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryStatisticsIngester")


@attr.s(auto_attribs=True)
class QueryStatisticsIngester:
    """
    Attributes:
        total_reached (int):
        total_chunks_matched (int):
        total_batches (int):
        total_lines_sent (int):
        store (Union[Unset, QueryStatisticsStore]):
    """

    total_reached: int
    total_chunks_matched: int
    total_batches: int
    total_lines_sent: int
    store: Union[Unset, QueryStatisticsStore] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_reached = self.total_reached
        total_chunks_matched = self.total_chunks_matched
        total_batches = self.total_batches
        total_lines_sent = self.total_lines_sent
        store: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.store, Unset):
            store = self.store.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalReached": total_reached,
                "totalChunksMatched": total_chunks_matched,
                "totalBatches": total_batches,
                "totalLinesSent": total_lines_sent,
            }
        )
        if store is not UNSET:
            field_dict["store"] = store

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_reached = d.pop("totalReached")

        total_chunks_matched = d.pop("totalChunksMatched")

        total_batches = d.pop("totalBatches")

        total_lines_sent = d.pop("totalLinesSent")

        _store = d.pop("store", UNSET)
        store: Union[Unset, QueryStatisticsStore]
        if isinstance(_store, Unset):
            store = UNSET
        else:
            store = QueryStatisticsStore.from_dict(_store)

        query_statistics_ingester = cls(
            total_reached=total_reached,
            total_chunks_matched=total_chunks_matched,
            total_batches=total_batches,
            total_lines_sent=total_lines_sent,
            store=store,
        )

        query_statistics_ingester.additional_properties = d
        return query_statistics_ingester

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
