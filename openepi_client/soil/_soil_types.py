# run the following:
#  datamodel-codegen --url https://api-test.openepi.io/soil/openapi.json --output openepi_client/soil/_soil_types.py

from __future__ import annotations
from enum import Enum
from typing import List, Optional, Union
from pydantic import BaseModel, Field


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title="Location")
    msg: str = Field(..., title="Message")
    type: str = Field(..., title="Error Type")


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title="Detail")


class FeatureType(Enum):
    Feature = "Feature"


class GeometryType(Enum):
    Point = "Point"
    Polygon = "Polygon"


class PointGeometry(BaseModel):
    coordinates: List[float] = Field(
        description="[longitude, latitude] decimal coordinates",
        example=[60.5, 11.59],
        min_items=2,
        max_items=2,
    )
    type: GeometryType


class BoundingBoxGeometry(BaseModel):
    coordinates: List[List[List[float]]] = Field(
        description="[[[min_lon, min_lat], [max_lon, min_lat], [max_lon, max_lat], [min_lon, max_lat], [min_lon, min_lat]]]",
        example=[
            [[60.5, 11.59], [60.6, 11.59], [60.6, 11.6], [60.5, 11.6], [60.5, 11.59]]
        ],
    )
    type: GeometryType


class SoilPropertiesNames(Enum):
    bdod = "Bulk density"
    cec = "Cation exchange capacity (CEC pH 7)"
    cfvo = "Coarse fragments"
    clay = "Clay"
    nitrogen = "Nitrogen"
    ocd = "Organic carbon density"
    ocs = "Organic carbon stocks"
    phh2o = "pH water"
    sand = "Sand"
    silt = "Silt"
    soc = "Soil organic carbon"


class SoilPropertiesCodes(Enum):
    bdod = "bdod"
    cec = "cec"
    cfvo = "cfvo"
    clay = "clay"
    nitrogen = "nitrogen"
    ocd = "ocd"
    ocs = "ocs"
    phh2o = "phh2o"
    sand = "sand"
    silt = "silt"
    soc = "soc"


class SoilPropertiesMappedUnits(Enum):
    bdod = "cg/cm³"
    cec = "mmol(c)/kg"
    cfvo = "cm³/dm³"
    clay = "g/kg"
    nitrogen = "cg/kg"
    ocd = "hg/m³"
    ocs = "t/ha"
    phh2o = "pH*10"
    sand = "g/kg"
    silt = "g/kg"
    soc = "dg/kg"


class SoilPropertiesTargetUnits(Enum):
    bdod = "kg/dm³"
    cec = "cmol(c)/kg"
    cfvo = "cm³/100cm³"
    clay = "%"
    nitrogen = "g/kg"
    ocd = "hg/m³"
    ocs = "kg/m²"
    phh2o = "pH"
    sand = "%"
    silt = "%"
    soc = "g/kg"


class SoilPropertiesConversionFactors(Enum):
    bdod = 100
    cec = 10
    cfvo = 10
    clay = 10
    nitrogen = 100
    ocd = 10
    ocs = 10
    phh2o = 10
    sand = 10
    silt = 10
    soc = 10


class SoilLayerList(BaseModel):
    layers: List[SoilLayer] = Field(..., description="The queried soil property layers")


class SoilPropertyUnit(BaseModel):
    d_factor: SoilPropertiesConversionFactors = Field(
        ..., description="The conversion factor", example=10
    )
    mapped_units: SoilPropertiesMappedUnits = Field(
        ..., description="The mapped unit of the soil property", example="cm³/dm³"
    )
    target_units: SoilPropertiesTargetUnits = Field(
        ..., description="The target unit of the soil property", example="m³/ha"
    )
    uncertainty_unit: str = Field(
        ..., description="The unit of the uncertainty", example=""
    )


class SoilLayer(BaseModel):
    code: SoilPropertiesCodes = Field(
        ..., description="The soil property code", example="bdod"
    )
    name: SoilPropertiesNames = Field(
        ..., description="The name of the soil property", example="Bulk density"
    )
    unit_measure: SoilPropertyUnit = Field(
        ..., description="The unit of the soil property"
    )
    depths: List[SoilDepth] = Field(
        ..., description="The queried soil depths with values"
    )


class SoilPropertyValues(BaseModel):
    mean: float | None = Field(
        None, description="The mean value of the soil property", example=50
    )
    Q0_05: float | None = Field(
        None,
        description="The 5th percentile of the soil property",
        example=40,
        alias="Q0.05",
    )
    Q0_5: float | None = Field(
        None,
        description="The 50th percentile of the soil property",
        example=50,
        alias="Q0.5",
    )
    Q0_95: float | None = Field(
        None,
        description="The 95th percentile of the soil property",
        example=60,
        alias="Q0.95",
    )
    uncertainty: float | None = Field(
        None, description="The uncertainty of the soil property", example=5
    )


class SoilDepthLabels(Enum):
    depth_0_5 = "0-5cm"
    depth_0_30 = "0-30cm"
    depth_5_15 = "5-15cm"
    depth_15_30 = "15-30cm"
    depth_30_60 = "30-60cm"
    depth_60_100 = "60-100cm"
    depth_100_200 = "100-200cm"


# Create a reverse lookup dictionary
REVERSE_DEPTH_LOOKUP = {
    v.value: k for k, v in list(SoilDepthLabels.__members__.items())
}


# Function to get the enum member using the reverse lookup
def get_soil_depth_from_label(depth_string: str) -> SoilDepthLabels:
    try:
        return REVERSE_DEPTH_LOOKUP[depth_string]
    except KeyError:
        raise ValueError(f"No soil depth label found for '{depth_string}'")


class SoilDepthTop(Enum):
    depth_0_5 = 0
    depth_0_30 = 0
    depth_5_15 = 5
    depth_15_30 = 15
    depth_30_60 = 30
    depth_60_100 = 60
    depth_100_200 = 100


class SoilDepthBottom(Enum):
    depth_0_5 = 5
    depth_0_30 = 30
    depth_5_15 = 15
    depth_15_30 = 30
    depth_30_60 = 60
    depth_60_100 = 100
    depth_100_200 = 200


class SoilDepthUnits(Enum):
    depth_0_5 = "cm"
    depth_0_30 = "cm"
    depth_5_15 = "cm"
    depth_15_30 = "cm"
    depth_30_60 = "cm"
    depth_60_100 = "cm"
    depth_100_200 = "cm"


class SoilDepth(BaseModel):
    range: DepthRange = Field(..., description="The soil depth range")
    label: SoilDepthLabels = Field(..., description="The soil depth label")
    values: SoilPropertyValues = Field(
        ..., description="The queried soil property values"
    )


class DepthRange(BaseModel):
    top_depth: SoilDepthTop = Field(..., description="The top depth", example=0)
    bottom_depth: SoilDepthBottom = Field(
        ..., description="The bottom depth", example=5
    )
    unit_depth: SoilDepthUnits = Field(
        ..., description="The unit of the depth range", example="cm"
    )


class SoilPropertyJSON(BaseModel):
    type: FeatureType = Field(
        description="The feature type of the geojson-object",
    )
    geometry: PointGeometry = Field(
        ...,
        description="The geometry of the queried location",
    )
    properties: SoilLayerList = Field(
        ...,
        description="The queried soil property information",
    )


class SoilTypes(Enum):
    t0 = "Acrisols"
    t1 = "Albeluvisols"
    t2 = "Alisols"
    t3 = "Andosols"
    t4 = "Arenosols"
    t5 = "Calcisols"
    t6 = "Cambisols"
    t7 = "Chernozems"
    t8 = "Cryosols"
    t9 = "Durisols"
    t10 = "Ferralsols"
    t11 = "Fluvisols"
    t12 = "Gleysols"
    t13 = "Gypsisols"
    t14 = "Histosols"
    t15 = "Kastanozems"
    t16 = "Leptosols"
    t17 = "Lixisols"
    t18 = "Luvisols"
    t19 = "Nitisols"
    t20 = "Phaeozems"
    t21 = "Planosols"
    t22 = "Plinthosols"
    t23 = "Podzols"
    t24 = "Regosols"
    t25 = "Solonchaks"
    t26 = "Solonetz"
    t27 = "Stagnosols"
    t28 = "Umbrisols"
    t29 = "Vertisols"
    No_information = "No information available"


class SoilTypeProbability(BaseModel):
    soil_type: SoilTypes = Field(..., description="The soil type", example="Acrisols")
    probability: int = Field(
        ...,
        description="The probability of the soil type as an integer between 0 and 100",
        example=70,
    )


class SoilTypeInfo(BaseModel):
    most_probable_soil_type: SoilTypes = Field(
        ...,
        description="The most probable soil type at the queried location",
        example="Acrisols",
    )
    probabilities: List[SoilTypeProbability] | None = Field(
        None, description="The soil type probabilities"
    )


class SoilTypeSummary(BaseModel):
    soil_type: SoilTypes = Field(..., description="The soil type", example="Acrisols")
    count: int = Field(
        ...,
        description="The number of occurrences of the soil type within the queried bounding box",
        example=70,
    )


class SoilTypeJSON(BaseModel):
    type: FeatureType = Field(
        description="The feature type of the geojson-object",
    )
    geometry: PointGeometry = Field(
        ...,
        description="The geometry of the queried location",
    )
    properties: SoilTypeInfo = Field(
        ...,
        description="The soil type information at the queried location",
    )


class SoilTypeSummaryInfo(BaseModel):
    summaries: List[SoilTypeSummary] = Field(
        ..., description="The soil type summaries within the queried bounding box"
    )


class SoilTypeSummaryJSON(BaseModel):
    type: FeatureType = Field(
        description="The feature type of this geojson-object",
    )
    geometry: BoundingBoxGeometry = Field(
        ...,
        description="The geometry of the queried location",
    )
    properties: SoilTypeSummaryInfo = Field(
        ...,
        description="The soil type summary information",
    )
