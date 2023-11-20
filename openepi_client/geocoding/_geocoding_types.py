# generated by datamodel-codegen:
#   filename:  https://api-test.openepi.io/geocoding/openapi.json
#   timestamp: 2023-11-14T13:47:49+00:00

from __future__ import annotations

from typing import Any, List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Literal


class Coordinate(RootModel[List[Any]]):
    root: List[Any]


class LineString(BaseModel):
    type: Literal['LineString'] = Field(..., title='Type')
    coordinates: List[Coordinate] = Field(..., min_length=2, title='Coordinates')


class MultiLineString(BaseModel):
    type: Literal['MultiLineString'] = Field(..., title='Type')
    coordinates: List[List[Coordinate]] = Field(..., title='Coordinates')


class MultiPoint(BaseModel):
    type: Literal['MultiPoint'] = Field(..., title='Type')
    coordinates: List[List] = Field(..., title='Coordinates')


class MultiPolygon(BaseModel):
    type: Literal['MultiPolygon'] = Field(..., title='Type')
    coordinates: List[List[List[Coordinate]]] = Field(..., title='Coordinates')


class Point(BaseModel):
    type: Literal['Point'] = Field(..., title='Type')
    coordinates: List = Field(
        ...,
        description='Coordinates in the format (lon, lat)',
        max_length=2,
        min_length=2,
        title='Coordinates',
    )


class Polygon(BaseModel):
    type: Literal['Polygon'] = Field(..., title='Type')
    coordinates: List[List[Coordinate]] = Field(..., title='Coordinates')


class Properties(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    name: str = Field(..., description='Name of the OSM-object', title='Name')
    osm_type: str = Field(
        ...,
        description='Whether the OSM object is an OSM node (N), way (W), or relation (R)',
        title='Osm Type',
    )
    osm_id: int = Field(
        ...,
        description='An ID uniquely identifies the OSM-object within the OSM-type',
        title='Osm Id',
    )
    type: Optional[str] = Field(
        None,
        description='The type of the place (e.g. house, street, city, country)',
        title='Type',
    )
    country: Optional[str] = Field(
        None,
        description='Name of the country that the OSM-object is in',
        title='Country',
    )
    county: Optional[str] = Field(
        None, description='Name of the county that the OSM-object is in', title='County'
    )
    city: Optional[str] = Field(
        None, description='Name of the city that the OSM-object is in', title='City'
    )
    countrycode: Optional[str] = Field(
        None,
        description='Country code for the country that the OSM-object is in',
        title='Countrycode',
    )
    osm_key: Optional[str] = Field(
        None,
        description='Key of the main tag of the OSM object (e.g. boundary, highway, amenity)',
        title='Osm Key',
    )
    osm_value: Optional[str] = Field(
        None,
        description='Value of the main tag of the OSM object (e.g. residential, restaurant)',
        title='Osm Value',
    )
    postcode: Optional[str] = Field(
        None, description='Postal code of the OSM-object', title='Postcode'
    )
    extent: Optional[List] = Field(
        None,
        description='The bounding box formatted as (min latitude, max latitude, min longitude, max longitude)',
        title='Extent',
    )


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class Feature(BaseModel):
    type: Literal['Feature'] = Field(..., title='Type')
    geometry: Union[
        Point, MultiPoint, LineString, MultiLineString, Polygon, MultiPolygon
    ] = Field(..., title='Geometry')
    properties: Properties


class FeatureCollection(BaseModel):
    type: Literal['FeatureCollection'] = Field(..., title='Type')
    features: List[Feature] = Field(..., title='Features')


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title='Detail')
