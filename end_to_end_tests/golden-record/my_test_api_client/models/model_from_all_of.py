from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.another_all_of_sub_model_type import AnotherAllOfSubModelType
from ..models.another_all_of_sub_model_type_enum import AnotherAllOfSubModelTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelFromAllOf")


@attr.s(auto_attribs=True)
class ModelFromAllOf:
    """
    Attributes:
        a_sub_property (Union[Unset, str]):
        type (Union[Unset, AnotherAllOfSubModelType]):
        type_enum (Union[Unset, AnotherAllOfSubModelTypeEnum]):
        another_sub_property (Union[Unset, str]):
    """

    a_sub_property: Union[Unset, str] = UNSET
    type: Union[Unset, AnotherAllOfSubModelType] = UNSET
    type_enum: Union[Unset, AnotherAllOfSubModelTypeEnum] = UNSET
    another_sub_property: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        a_sub_property = self.a_sub_property
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        type_enum: Union[Unset, int] = UNSET
        if not isinstance(self.type_enum, Unset):
            type_enum = self.type_enum.value

        another_sub_property = self.another_sub_property

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if a_sub_property is not UNSET:
            field_dict["a_sub_property"] = a_sub_property
        if type is not UNSET:
            field_dict["type"] = type
        if type_enum is not UNSET:
            field_dict["type_enum"] = type_enum
        if another_sub_property is not UNSET:
            field_dict["another_sub_property"] = another_sub_property

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        a_sub_property = d.pop("a_sub_property", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AnotherAllOfSubModelType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AnotherAllOfSubModelType(_type)

        _type_enum = d.pop("type_enum", UNSET)
        type_enum: Union[Unset, AnotherAllOfSubModelTypeEnum]
        if isinstance(_type_enum, Unset):
            type_enum = UNSET
        else:
            type_enum = AnotherAllOfSubModelTypeEnum(_type_enum)

        another_sub_property = d.pop("another_sub_property", UNSET)

        model_from_all_of = cls(
            a_sub_property=a_sub_property,
            type=type,
            type_enum=type_enum,
            another_sub_property=another_sub_property,
        )

        model_from_all_of.additional_properties = d
        return model_from_all_of

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
