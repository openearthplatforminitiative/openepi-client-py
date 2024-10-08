# generated by datamodel-codegen:
#   filename:  https://api.openepi.io/crop-health/openapi.json
#   timestamp: 2024-10-08T08:01:18+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class BinaryPredictionResponse(BaseModel):
    HLT: float = Field(..., description="Healthy")
    NOT_HLT: float = Field(..., description="Not Healthy")


class SingleHLTPredictionResponse(BaseModel):
    HLT: float = Field(..., description="Healthy")
    CBSD: float = Field(..., description="Cassava Brown Streak Disease")
    CMD: float = Field(..., description="Cassava Mosaic Disease")
    MLN: float = Field(..., description="Maize Lethal Necrosis")
    MSV: float = Field(..., description="Maize Streak Virus")
    FAW: float = Field(..., description="Fall Armyworm")
    MLB: float = Field(..., description="Maize Leaf Blight")
    BR: float = Field(..., description="Bean Rust")
    ALS: float = Field(..., description="Angular Leaf Spot")
    BS: float = Field(..., description="Black Sigatoka")
    FW: float = Field(..., description="Fusarium Wilt Race 1")
    ANT: float = Field(..., description="Anthracnose")
    CSSVD: float = Field(..., description="Cocoa Swollen Shoot Virus Disease")


class MultiHLTPredictionResponse(BaseModel):
    HLT_cassava: float = Field(..., description="Healthy Cassava")
    CBSD_cassava: float = Field(..., description="Cassava Brown Streak Disease")
    CMD_cassava: float = Field(..., description="Cassava Mosaic Disease")
    MLN_maize: float = Field(..., description="Maize Lethal Necrosis")
    HLT_maize: float = Field(..., description="Healthy Maize")
    MSV_maize: float = Field(..., description="Maize Streak Virus")
    FAW_maize: float = Field(..., description="Fall Armyworm")
    MLB_maize: float = Field(..., description="Maize Leaf Blight")
    HLT_beans: float = Field(..., description="Healthy Beans")
    BR_beans: float = Field(..., description="Bean Rust")
    ALS_beans: float = Field(..., description="Angular Leaf Spot")
    HLT_bananas: float = Field(..., description="Healthy Bananas")
    BS_bananas: float = Field(..., description="Black Sigatoka")
    FW_bananas: float = Field(..., description="Fusarium Wilt Race 1")
    HLT_cocoa: float = Field(..., description="Healthy Cocoa")
    ANT_cocoa: float = Field(..., description="Anthracnose")
    CSSVD_cocoa: float = Field(..., description="Cocoa Swollen Shoot Virus Disease")
