from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryStatisticsSummary")


@attr.s(auto_attribs=True)
class QueryStatisticsSummary:
    """
    Attributes:
        bytes_processed_per_second (Union[Unset, int]):
        lines_processed_per_second (Union[Unset, int]):
        total_bytes_processed (Union[Unset, int]):
        total_lines_processed (Union[Unset, int]):
        exec_time (Union[Unset, int]):
        queue_time (Union[Unset, int]):
        subqueries (Union[Unset, int]):
        total_entries_returned (Union[Unset, int]):
    """

    bytes_processed_per_second: Union[Unset, int] = UNSET
    lines_processed_per_second: Union[Unset, int] = UNSET
    total_bytes_processed: Union[Unset, int] = UNSET
    total_lines_processed: Union[Unset, int] = UNSET
    exec_time: Union[Unset, int] = UNSET
    queue_time: Union[Unset, int] = UNSET
    subqueries: Union[Unset, int] = UNSET
    total_entries_returned: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bytes_processed_per_second = self.bytes_processed_per_second
        lines_processed_per_second = self.lines_processed_per_second
        total_bytes_processed = self.total_bytes_processed
        total_lines_processed = self.total_lines_processed
        exec_time = self.exec_time
        queue_time = self.queue_time
        subqueries = self.subqueries
        total_entries_returned = self.total_entries_returned

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bytes_processed_per_second is not UNSET:
            field_dict["bytesProcessedPerSecond"] = bytes_processed_per_second
        if lines_processed_per_second is not UNSET:
            field_dict["linesProcessedPerSecond"] = lines_processed_per_second
        if total_bytes_processed is not UNSET:
            field_dict["totalBytesProcessed"] = total_bytes_processed
        if total_lines_processed is not UNSET:
            field_dict["totalLinesProcessed"] = total_lines_processed
        if exec_time is not UNSET:
            field_dict["execTime"] = exec_time
        if queue_time is not UNSET:
            field_dict["queueTime"] = queue_time
        if subqueries is not UNSET:
            field_dict["subqueries"] = subqueries
        if total_entries_returned is not UNSET:
            field_dict["totalEntriesReturned"] = total_entries_returned

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bytes_processed_per_second = d.pop("bytesProcessedPerSecond", UNSET)

        lines_processed_per_second = d.pop("linesProcessedPerSecond", UNSET)

        total_bytes_processed = d.pop("totalBytesProcessed", UNSET)

        total_lines_processed = d.pop("totalLinesProcessed", UNSET)

        exec_time = d.pop("execTime", UNSET)

        queue_time = d.pop("queueTime", UNSET)

        subqueries = d.pop("subqueries", UNSET)

        total_entries_returned = d.pop("totalEntriesReturned", UNSET)

        query_statistics_summary = cls(
            bytes_processed_per_second=bytes_processed_per_second,
            lines_processed_per_second=lines_processed_per_second,
            total_bytes_processed=total_bytes_processed,
            total_lines_processed=total_lines_processed,
            exec_time=exec_time,
            queue_time=queue_time,
            subqueries=subqueries,
            total_entries_returned=total_entries_returned,
        )

        query_statistics_summary.additional_properties = d
        return query_statistics_summary

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
