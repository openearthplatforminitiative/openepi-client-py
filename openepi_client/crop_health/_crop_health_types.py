# generated by datamodel-codegen:
#   filename:  https://api-test.openepi.io/crop-health/openapi.json
#   timestamp: 2024-06-21T13:07:51+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class BinaryHealthPredictionResponse(BaseModel):
    HLT: Optional[float] = Field(None, description="Healthy")
    NOT_HLT: Optional[float] = Field(None, description="Not Healthy")


class SingleHLTHealthPredictionResponse(BaseModel):
    HLT: Optional[float] = Field(None, description="Healthy")
    CBSD: Optional[float] = Field(None, description="Cassava Brown Streak Disease")
    CMD: Optional[float] = Field(None, description="Cassava Mosaic Disease")
    MLN: Optional[float] = Field(None, description="Maize Lethal Necrosis")
    MSV: Optional[float] = Field(None, description="Maize Streak Virus")
    FAW: Optional[float] = Field(None, description="Fall Armyworm")
    MLB: Optional[float] = Field(None, description="Maize Leaf Blight")
    BR: Optional[float] = Field(None, description="Bean Rust")
    ALS: Optional[float] = Field(None, description="Angular Leaf Spot")
    BS: Optional[float] = Field(None, description="Black Sigatoka")
    FW: Optional[float] = Field(None, description="Fusarium Wilt Race 1")
    ANT: Optional[float] = Field(None, description="Anthracnose")
    CSSVD: Optional[float] = Field(
        None, description="Cocoa Swollen Shoot Virus Disease"
    )


class MultiHLTHealthPredictionResponse(BaseModel):
    HLT_cassava: Optional[float] = Field(None, description="Healthy Cassava")
    CBSD_cassava: Optional[float] = Field(
        None, description="Cassava Brown Streak Disease"
    )
    CMD_cassava: Optional[float] = Field(None, description="Cassava Mosaic Disease")
    MLN_maize: Optional[float] = Field(None, description="Maize Lethal Necrosis")
    HLT_maize: Optional[float] = Field(None, description="Healthy Maize")
    MSV_maize: Optional[float] = Field(None, description="Maize Streak Virus")
    FAW_maize: Optional[float] = Field(None, description="Fall Armyworm")
    MLB_maize: Optional[float] = Field(None, description="Maize Leaf Blight")
    HLT_beans: Optional[float] = Field(None, description="Healthy Beans")
    BR_beans: Optional[float] = Field(None, description="Bean Rust")
    ALS_beans: Optional[float] = Field(None, description="Angular Leaf Spot")
    HLT_bananas: Optional[float] = Field(None, description="Healthy Bananas")
    BS_bananas: Optional[float] = Field(None, description="Black Sigatoka")
    FW_bananas: Optional[float] = Field(None, description="Fusarium Wilt Race 1")
    HLT_cocoa: Optional[float] = Field(None, description="Healthy Cocoa")
    ANT_cocoa: Optional[float] = Field(None, description="Anthracnose")
    CSSVD_cocoa: Optional[float] = Field(
        None, description="Cocoa Swollen Shoot Virus Disease"
    )