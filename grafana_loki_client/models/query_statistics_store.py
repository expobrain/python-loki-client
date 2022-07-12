from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.query_statistics_store_chunk import QueryStatisticsStoreChunk
from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryStatisticsStore")


@attr.s(auto_attribs=True)
class QueryStatisticsStore:
    """
    Attributes:
        total_chunks_ref (int):
        total_chunks_downloaded (int):
        chunks_download_time (int):
        chunk (Union[Unset, QueryStatisticsStoreChunk]):
    """

    total_chunks_ref: int
    total_chunks_downloaded: int
    chunks_download_time: int
    chunk: Union[Unset, QueryStatisticsStoreChunk] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_chunks_ref = self.total_chunks_ref
        total_chunks_downloaded = self.total_chunks_downloaded
        chunks_download_time = self.chunks_download_time
        chunk: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.chunk, Unset):
            chunk = self.chunk.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalChunksRef": total_chunks_ref,
                "totalChunksDownloaded": total_chunks_downloaded,
                "chunksDownloadTime": chunks_download_time,
            }
        )
        if chunk is not UNSET:
            field_dict["chunk"] = chunk

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_chunks_ref = d.pop("totalChunksRef")

        total_chunks_downloaded = d.pop("totalChunksDownloaded")

        chunks_download_time = d.pop("chunksDownloadTime")

        _chunk = d.pop("chunk", UNSET)
        chunk: Union[Unset, QueryStatisticsStoreChunk]
        if isinstance(_chunk, Unset):
            chunk = UNSET
        else:
            chunk = QueryStatisticsStoreChunk.from_dict(_chunk)

        query_statistics_store = cls(
            total_chunks_ref=total_chunks_ref,
            total_chunks_downloaded=total_chunks_downloaded,
            chunks_download_time=chunks_download_time,
            chunk=chunk,
        )

        query_statistics_store.additional_properties = d
        return query_statistics_store

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
