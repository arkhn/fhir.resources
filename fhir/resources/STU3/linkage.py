# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Linkage
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Linkage(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Links records for 'same' item.
    Identifies two or more records (resource instances) that are referring to
    the same real-world "occurrence".
    """

    resource_type = Field("Linkage", const=True)

    active: bool = Field(
        None,
        alias="active",
        title="Whether this linkage assertion is active or not",
        description=(
            "Indicates whether the asserted set of linkages are considered to be "
            '"in effect".'
        ),
        # if property is element of this resource.
        element_property=True,
    )
    active__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_active", title="Extension field for ``active``."
    )

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Who is responsible for linkages",
        description=(
            "Identifies the user or organization responsible for asserting the "
            "linkages and who establishes the context for evaluating the nature of "
            "each linkage."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Organization"],
    )

    item: ListType[fhirtypes.LinkageItemType] = Field(
        ...,
        alias="item",
        title="Item to be linked",
        description=(
            "Identifies one of the records that is considered to refer to the same "
            "real-world occurrence as well as how the items hould be evaluated "
            "within the collection of linked items."
        ),
        # if property is element of this resource.
        element_property=True,
    )


class LinkageItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Item to be linked.
    Identifies one of the records that is considered to refer to the same real-
    world occurrence as well as how the items hould be evaluated within the
    collection of linked items.
    """

    resource_type = Field("LinkageItem", const=True)

    resource: fhirtypes.ReferenceType = Field(
        ...,
        alias="resource",
        title="Resource being linked",
        description="The resource instance being linked as part of the group.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.Code = Field(
        ...,
        alias="type",
        title="source | alternate | historical",
        description=(
            'Distinguishes which item is "source of truth" (if any) and which items'
            " are no longer considered to be current representations."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["source", "alternate", "historical"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )
