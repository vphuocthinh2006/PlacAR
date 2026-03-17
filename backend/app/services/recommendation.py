from typing import List

from ..schemas import (
    RecommendationRequest,
    RecommendationResponse,
    RecommendationResponseItem,
    FurnitureItem,
)


def basic_recommendation(req: RecommendationRequest) -> RecommendationResponse:
    """
    Gợi ý cơ bản (chưa dùng AI/LLM).

    - Ở giai đoạn đầu: dùng một danh sách cứng vài món nội thất mẫu.
    - Sau này sẽ thay bằng truy vấn DB + LLM.
    """
    room_area = req.room.width_m * req.room.length_m

    # Danh sách mẫu, sau này sẽ chuyển sang DB
    sample_items: List[FurnitureItem] = [
        FurnitureItem(
            id=1,
            name="Giường đơn 1m2",
            width_cm=120,
            depth_cm=200,
            height_cm=40,
            type="bed",
            style="minimalist",
            description="Giường đơn phù hợp phòng ngủ nhỏ.",
        ),
        FurnitureItem(
            id=2,
            name="Bàn làm việc 1m2",
            width_cm=120,
            depth_cm=60,
            height_cm=75,
            type="desk",
            style="modern",
            description="Bàn làm việc gọn, phù hợp góc học tập.",
        ),
        FurnitureItem(
            id=3,
            name="Sofa nhỏ 2 chỗ",
            width_cm=150,
            depth_cm=80,
            height_cm=85,
            type="sofa",
            style="modern",
            description="Sofa 2 chỗ cho phòng khách nhỏ.",
        ),
    ]

    # Lọc rất đơn giản: tránh gợi ý đồ quá to cho phòng quá nhỏ
    filtered: List[FurnitureItem] = []
    for item in sample_items:
        item_area_m2 = (item.width_cm / 100) * (item.depth_cm / 100)
        if item_area_m2 <= room_area * 0.3:  # dùng tối đa 30% diện tích
            filtered.append(item)

    response_items = [
        RecommendationResponseItem(
            item=item,
            reason="Phù hợp diện tích phòng và công năng cơ bản.",
        )
        for item in filtered[: req.max_items]
    ]

    return RecommendationResponse(items=response_items)

