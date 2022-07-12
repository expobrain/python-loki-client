from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryStatisticsStoreChunk")


@attr.s(auto_attribs=True)
class QueryStatisticsStoreChunk:
    """
    Attributes:
        head_chunk_bytes (int):
        head_chunk_lines (int):
        decompressed_bytes (int):
        decompressed_lines (int):
        compressed_bytes (int):
        total_duplicates (Union[Unset, int]):
    """

    head_chunk_bytes: int
    head_chunk_lines: int
    decompressed_bytes: int
    decompressed_lines: int
    compressed_bytes: int
    total_duplicates: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        head_chunk_bytes = self.head_chunk_bytes
        head_chunk_lines = self.head_chunk_lines
        decompressed_bytes = self.decompressed_bytes
        decompressed_lines = self.decompressed_lines
        compressed_bytes = self.compressed_bytes
        total_duplicates = self.total_duplicates

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "headChunkBytes": head_chunk_bytes,
                "headChunkLines": head_chunk_lines,
                "decompressedBytes": decompressed_bytes,
                "decompressedLines": decompressed_lines,
                "compressedBytes": compressed_bytes,
            }
        )
        if total_duplicates is not UNSET:
            field_dict["totalDuplicates"] = total_duplicates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        head_chunk_bytes = d.pop("headChunkBytes")

        head_chunk_lines = d.pop("headChunkLines")

        decompressed_bytes = d.pop("decompressedBytes")

        decompressed_lines = d.pop("decompressedLines")

        compressed_bytes = d.pop("compressedBytes")

        total_duplicates = d.pop("totalDuplicates", UNSET)

        query_statistics_store_chunk = cls(
            head_chunk_bytes=head_chunk_bytes,
            head_chunk_lines=head_chunk_lines,
            decompressed_bytes=decompressed_bytes,
            decompressed_lines=decompressed_lines,
            compressed_bytes=compressed_bytes,
            total_duplicates=total_duplicates,
        )

        query_statistics_store_chunk.additional_properties = d
        return query_statistics_store_chunk

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
