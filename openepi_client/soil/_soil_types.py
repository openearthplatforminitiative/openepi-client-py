# generated by datamodel-codegen:
#   filename:  https://api.openepi.io/soil/openapi.json
#   timestamp: 2024-10-08T08:01:15+00:00

from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Literal


class FeatureType(RootModel[Literal["Feature"]]):
    root: Literal["Feature"] = Field(..., title="FeatureType")


class GeometryType(RootModel[Literal["Point", "Polygon"]]):
    root: Literal["Point", "Polygon"] = Field(..., title="GeometryType")


class PointGeometry(BaseModel):
    coordinates: List[float] = Field(
        ...,
        description="[longitude, latitude] decimal coordinates",
        examples=[[60.5, 11.59]],
        max_length=2,
        min_length=2,
        title="Coordinates",
    )
    type: GeometryType


class SoilConversionFactors(RootModel[Literal[10, 100]]):
    root: Literal[10, 100] = Field(..., title="SoilConversionFactors")


class SoilDepthLabels(
    RootModel[
        Literal[
            "0-5cm", "0-30cm", "5-15cm", "15-30cm", "30-60cm", "60-100cm", "100-200cm"
        ]
    ]
):
    root: Literal[
        "0-5cm", "0-30cm", "5-15cm", "15-30cm", "30-60cm", "60-100cm", "100-200cm"
    ] = Field(..., title="SoilDepthLabels")


class SoilDepthUnits(RootModel[Literal["cm"]]):
    root: Literal["cm"] = Field(..., title="SoilDepthUnits")


class SoilDepths(RootModel[Literal[0, 5, 15, 30, 60, 100, 200]]):
    root: Literal[0, 5, 15, 30, 60, 100, 200] = Field(..., title="SoilDepths")


class SoilMappedUnits(
    RootModel[
        Literal[
            "cg/cm³",
            "mmol(c)/kg",
            "cm³/dm³",
            "g/kg",
            "cg/kg",
            "hg/m³",
            "t/ha",
            "pH*10",
            "dg/kg",
        ]
    ]
):
    root: Literal[
        "cg/cm³",
        "mmol(c)/kg",
        "cm³/dm³",
        "g/kg",
        "cg/kg",
        "hg/m³",
        "t/ha",
        "pH*10",
        "dg/kg",
    ] = Field(..., title="SoilMappedUnits")


class SoilPropertiesCodes(
    RootModel[
        Literal[
            "bdod",
            "cec",
            "cfvo",
            "clay",
            "nitrogen",
            "ocd",
            "ocs",
            "phh2o",
            "sand",
            "silt",
            "soc",
        ]
    ]
):
    root: Literal[
        "bdod",
        "cec",
        "cfvo",
        "clay",
        "nitrogen",
        "ocd",
        "ocs",
        "phh2o",
        "sand",
        "silt",
        "soc",
    ] = Field(..., title="SoilPropertiesCodes")


class SoilPropertyValueTypes(
    RootModel[Literal["mean", "Q0.05", "Q0.5", "Q0.95", "uncertainty"]]
):
    root: Literal["mean", "Q0.05", "Q0.5", "Q0.95", "uncertainty"] = Field(
        ..., title="SoilPropertyValueTypes"
    )


class SoilPropertyValues(BaseModel):
    mean: Optional[float] = Field(
        None,
        description="The mean value of the soil property",
        examples=[50],
        title="Mean",
    )
    Q0_05: Optional[float] = Field(
        None,
        alias="Q0.05",
        description="The 5th percentile of the soil property",
        examples=[40],
        title="Q0.05",
    )
    Q0_5: Optional[float] = Field(
        None,
        alias="Q0.5",
        description="The 50th percentile of the soil property",
        examples=[50],
        title="Q0.5",
    )
    Q0_95: Optional[float] = Field(
        None,
        alias="Q0.95",
        description="The 95th percentile of the soil property",
        examples=[60],
        title="Q0.95",
    )
    uncertainty: Optional[float] = Field(
        None,
        description="The uncertainty of the soil property",
        examples=[5],
        title="Uncertainty",
    )


class SoilTargetUnits(
    RootModel[
        Literal[
            "kg/dm³", "cmol(c)/kg", "cm³/100cm³", "%", "g/kg", "hg/m³", "kg/m²", "pH"
        ]
    ]
):
    root: Literal[
        "kg/dm³", "cmol(c)/kg", "cm³/100cm³", "%", "g/kg", "hg/m³", "kg/m²", "pH"
    ] = Field(..., title="SoilTargetUnits")


class SoilTypes(
    RootModel[
        Literal[
            "Acrisols",
            "Albeluvisols",
            "Alisols",
            "Andosols",
            "Arenosols",
            "Calcisols",
            "Cambisols",
            "Chernozems",
            "Cryosols",
            "Durisols",
            "Ferralsols",
            "Fluvisols",
            "Gleysols",
            "Gypsisols",
            "Histosols",
            "Kastanozems",
            "Leptosols",
            "Lixisols",
            "Luvisols",
            "Nitisols",
            "Phaeozems",
            "Planosols",
            "Plinthosols",
            "Podzols",
            "Regosols",
            "Solonchaks",
            "Solonetz",
            "Stagnosols",
            "Umbrisols",
            "Vertisols",
            "No information",
        ]
    ]
):
    root: Literal[
        "Acrisols",
        "Albeluvisols",
        "Alisols",
        "Andosols",
        "Arenosols",
        "Calcisols",
        "Cambisols",
        "Chernozems",
        "Cryosols",
        "Durisols",
        "Ferralsols",
        "Fluvisols",
        "Gleysols",
        "Gypsisols",
        "Histosols",
        "Kastanozems",
        "Leptosols",
        "Lixisols",
        "Luvisols",
        "Nitisols",
        "Phaeozems",
        "Planosols",
        "Plinthosols",
        "Podzols",
        "Regosols",
        "Solonchaks",
        "Solonetz",
        "Stagnosols",
        "Umbrisols",
        "Vertisols",
        "No information",
    ] = Field(..., title="SoilTypes")


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title="Location")
    msg: str = Field(..., title="Message")
    type: str = Field(..., title="Error Type")


class BoundingBoxGeometry(BaseModel):
    coordinates: List[List[List[float]]] = Field(
        ...,
        description="[[[min_lon, min_lat], [max_lon, min_lat], [max_lon, max_lat], [min_lon, max_lat], [min_lon, min_lat]]]",
        examples=[
            [[[60.5, 11.59], [60.6, 11.59], [60.6, 11.6], [60.5, 11.6], [60.5, 11.59]]]
        ],
        title="Coordinates",
    )
    type: GeometryType


class DepthRange(BaseModel):
    top_depth: SoilDepths = Field(..., description="The top depth", examples=[0])
    bottom_depth: SoilDepths = Field(..., description="The bottom depth", examples=[5])
    unit_depth: SoilDepthUnits = Field(
        ..., description="The unit of the depth range", examples=["cm"]
    )


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title="Detail")


class SoilDepth(BaseModel):
    range: DepthRange = Field(..., description="The soil depth range")
    label: SoilDepthLabels = Field(..., description="The soil depth label")
    values: SoilPropertyValues = Field(
        ..., description="The queried soil property values"
    )


class SoilPropertyUnit(BaseModel):
    conversion_factor: SoilConversionFactors = Field(
        ..., description="The conversion factor", examples=[10]
    )
    mapped_units: SoilMappedUnits = Field(
        ..., description="The mapped unit of the soil property", examples=["cm³/dm³"]
    )
    target_units: SoilTargetUnits = Field(
        ..., description="The target unit of the soil property", examples=["m³/ha"]
    )
    uncertainty_unit: str = Field(
        ...,
        description="The unit of the uncertainty",
        examples=[""],
        title="Uncertainty Unit",
    )


class SoilTypeProbability(BaseModel):
    soil_type: SoilTypes = Field(
        ..., description="The soil type", examples=["Acrisols"]
    )
    probability: int = Field(
        ...,
        description="The probability of the soil type as an integer between 0 and 100",
        examples=[70],
        title="Probability",
    )


class SoilTypeSummary(BaseModel):
    soil_type: SoilTypes = Field(
        ..., description="The soil type", examples=["Acrisols"]
    )
    count: int = Field(
        ...,
        description="The number of occurrences of the soil type within the queried bounding box",
        examples=[70],
        title="Count",
    )


class SoilTypeSummaryInfo(BaseModel):
    summaries: List[SoilTypeSummary] = Field(
        ...,
        description="The soil type summaries within the queried bounding box",
        title="Summaries",
    )


class SoilTypeSummaryJSON(BaseModel):
    type: FeatureType = Field(
        ..., description="The feature type of this geojson-object"
    )
    geometry: BoundingBoxGeometry = Field(
        ..., description="The geometry of the queried location"
    )
    properties: SoilTypeSummaryInfo = Field(
        ..., description="The soil type summary information"
    )


class SoilLayer(BaseModel):
    code: SoilPropertiesCodes = Field(
        ..., description="The soil property code", examples=["bdod"]
    )
    name: str = Field(
        ...,
        description="The name of the soil property",
        examples=["Bulk density"],
        title="Name",
    )
    unit_measure: SoilPropertyUnit = Field(
        ..., description="The unit of the soil property"
    )
    depths: List[SoilDepth] = Field(
        ..., description="The queried soil depths with values", title="Depths"
    )


class SoilLayerList(BaseModel):
    layers: List[SoilLayer] = Field(
        ..., description="The queried soil property layers", title="Layers"
    )


class SoilPropertyJSON(BaseModel):
    type: FeatureType = Field(..., description="The feature type of the geojson-object")
    geometry: PointGeometry = Field(
        ..., description="The geometry of the queried location"
    )
    properties: SoilLayerList = Field(
        ..., description="The queried soil property information"
    )


class SoilTypeInfo(BaseModel):
    most_probable_soil_type: SoilTypes = Field(
        ...,
        description="The most probable soil type at the queried location",
        examples=["Acrisols"],
    )
    probabilities: Optional[List[SoilTypeProbability]] = Field(
        None, description="The soil type probabilities", title="Probabilities"
    )


class SoilTypeJSON(BaseModel):
    type: FeatureType = Field(..., description="The feature type of the geojson-object")
    geometry: PointGeometry = Field(
        ..., description="The geometry of the queried location"
    )
    properties: SoilTypeInfo = Field(
        ..., description="The soil type information at the queried location"
    )
