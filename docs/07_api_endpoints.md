## 07 – API Endpoints (Dự kiến)

Tài liệu này mô tả các endpoint chính của backend DecoAR / RoomFit.  
Trong giai đoạn đầu, tập trung vào API phục vụ mobile app.

---

### 1. Quy ước chung

- **Base URL (local)**: `http://127.0.0.1:8000`
- **Format dữ liệu**: JSON.
- **Auth**: Giai đoạn đầu **không yêu cầu**, chỉ dùng cho demo (có thể mở rộng sau).

---

### 2. Health Check

#### 2.1. `GET /health`

- **Mô tả**: Kiểm tra backend đang hoạt động.
- **Request**:
  - No body.
- **Response 200** (ví dụ):

```json
{
  "status": "ok",
  "app": "DecoAR / RoomFit Backend",
  "env": "development"
}
```

---

### 3. Furniture Catalog (dự kiến)

Các endpoint này dùng để lấy danh sách đồ nội thất từ DB.

#### 3.1. `GET /furniture`

- **Mô tả**: Lấy danh sách đồ nội thất.
- **Query params (dự kiến)**:
  - `type` (optional): lọc theo loại (bed, desk, sofa…).
  - `style` (optional): lọc theo phong cách (minimalist, modern…).
- **Response 200** (ví dụ):

```json
[
  {
    "id": 1,
    "name": "Giường đơn 1m2",
    "width_cm": 120,
    "depth_cm": 200,
    "height_cm": 40,
    "type": "bed",
    "style": "minimalist",
    "description": "Giường đơn phù hợp phòng ngủ nhỏ.",
    "image_url": "https://example.com/bed_1m2.png",
    "model_url": "https://example.com/bed_1m2.glb"
  }
]
```

#### 3.2. `GET /furniture/{id}`

- **Mô tả**: Lấy thông tin chi tiết một món đồ nội thất.
- **Path params**:
  - `id`: ID của item.
- **Response 200**: giống 1 object trong response của `/furniture`.

---

### 4. Recommendation – Gợi ý cơ bản

#### 4.1. `POST /recommend/basic`

- **Mô tả**: Gợi ý nội thất dựa trên kích thước phòng & loại phòng, **chưa dùng AI/LLM**.
- **Request Body**:

```json
{
  "room": {
    "width_m": 2.0,
    "length_m": 3.0,
    "room_type": "bedroom",
    "style": "minimalist"
  },
  "max_items": 5
}
```

- **Thuộc tính**:
  - `room.width_m`: chiều rộng vùng trống (mét).
  - `room.length_m`: chiều dài vùng trống (mét).
  - `room_type`: `"living_room" | "bedroom" | "studio" | "other"`.
  - `style`: chuỗi mô tả phong cách (optional).
  - `max_items`: số lượng gợi ý tối đa cần trả về.

- **Response 200** (ví dụ):

```json
{
  "items": [
    {
      "item": {
        "id": 2,
        "name": "Bàn làm việc 1m2",
        "width_cm": 120,
        "depth_cm": 60,
        "height_cm": 75,
        "type": "desk",
        "style": "modern",
        "description": "Bàn làm việc gọn, phù hợp góc học tập."
      },
      "reason": "Phù hợp diện tích phòng và công năng cơ bản."
    }
  ]
}
```

---

### 5. Recommendation – Gợi ý thông minh (AI/LLM) – Dự kiến

Endpoint này sẽ được hiện thực trong Phase 3.

#### 5.1. `POST /recommend/ai`

- **Mô tả**: Gợi ý nội thất sử dụng AI/LLM.
- **Request Body (dự kiến)**:

```json
{
  "room": {
    "width_m": 2.0,
    "length_m": 3.0,
    "room_type": "bedroom",
    "style": "minimalist"
  },
  "max_items": 5,
  "notes": "Cần giường cho 1 người, vẫn còn chỗ để bàn học nhỏ."
}
```

- **Response 200 (dự kiến)**:

```json
{
  "items": [
    {
      "item": {
        "id": 1,
        "name": "Giường đơn 1m2",
        "width_cm": 120,
        "depth_cm": 200,
        "height_cm": 40,
        "type": "bed",
        "style": "minimalist",
        "description": "Giường đơn phù hợp phòng ngủ nhỏ."
      },
      "reason": "Phòng có diện tích hạn chế, giường đơn 1m2 giúp chừa lại không gian cho bàn học."
    },
    {
      "item": {
        "id": 2,
        "name": "Bàn làm việc 1m2",
        "width_cm": 120,
        "depth_cm": 60,
        "height_cm": 75,
        "type": "desk",
        "style": "modern",
        "description": "Bàn làm việc gọn, đủ chỗ cho laptop và vài quyển sách."
      },
      "reason": "Phù hợp với yêu cầu có góc học tập nhỏ gọn trong phòng ngủ."
    }
  ]
}
```

---

### 6. Lưu ý mở rộng

- Có thể bổ sung:
  - Endpoint cho user layout (lưu vị trí các món đồ).
  - Endpoint cho cấu hình phòng (nhiều phòng, nhiều layout).
- Tài liệu này sẽ được cập nhật khi backend hoàn thiện thêm chức năng.

