from pydantic import BaseModel
from typing import Literal


class RoomContext(BaseModel):
    width_m: float
    length_m: float
    room_type: Literal["living_room", "bedroom", "studio", "other"]
    style: str | None = None  # ví dụ: "minimalist", "modern"


class FurnitureItem(BaseModel):
    id: int
    name: str
    width_cm: int
    depth_cm: int
    height_cm: int
    type: str
    style: str
    description: str | None = None


class RecommendationRequest(BaseModel):
    room: RoomContext
    max_items: int = 5


class RecommendationResponseItem(BaseModel):
    item: FurnitureItem
    reason: str | None = None


class RecommendationResponse(BaseModel):
    items: list[RecommendationResponseItem]

