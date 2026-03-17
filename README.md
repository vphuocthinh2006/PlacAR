 # DecoAR / RoomFit – Hệ thống gợi ý và mô phỏng nội thất AR

## 1. Giới thiệu

- **Mục tiêu**: Ứng dụng hỗ trợ người dùng hình dung đồ nội thất trong không gian thật bằng công nghệ AR và AI.
- **Bài toán**: Người dùng khó ước lượng kích thước và mức độ phù hợp của đồ nội thất với không gian thực.
- **Giải pháp**: Phân tích không gian phòng → gợi ý đồ phù hợp → mô phỏng 3D tỷ lệ 1:1 ngay trong phòng bằng AR.

## 2. Kiến trúc tổng quan

- **Mobile App (Android + ARCore)**:
  - Quét phòng, phát hiện mặt phẳng sàn.
  - Hiển thị mô hình 3D đồ nội thất trong không gian thật.
- **Backend (Python + FastAPI)**:
  - Quản lý catalog đồ nội thất (kích thước, phong cách, loại phòng).
  - Cung cấp API gợi ý đồ nội thất dựa trên thông tin không gian và ngữ cảnh.
  - Tích hợp LLM (OpenAI/Gemini) để chọn lọc và giải thích gợi ý.

## 3. Cấu trúc thư mục (dự kiến)

```text
PlacAR/
  README.md
  backend/
    app/
      __init__.py
      main.py
      models.py
      schemas.py
      config.py
      services/
        __init__.py
        recommendation.py
    requirements.txt
```

> Giai đoạn này chỉ mới khởi tạo phần backend, phần mobile sẽ được tạo ở bước sau (ví dụ thư mục `mobile/` cho Android).

## 4. Tech Stack

- **Backend**:
  - Python 3.10+
  - FastAPI
  - Uvicorn
  - SQLAlchemy / SQLite (giai đoạn đầu)
- **AI/LLM**:
  - OpenAI / Gemini API (tùy môi trường cho phép).

## 5. Roadmap ngắn gọn

1. **M1 – Backend Skeleton**
   - Khởi tạo FastAPI.
   - Health check endpoint.
2. **M2 – Catalog nội thất**
   - Mô hình dữ liệu, seed dữ liệu mẫu.
   - API lấy danh sách đồ nội thất.
3. **M3 – Gợi ý cơ bản (chưa AI)**
   - API nhận kích thước phòng → trả về danh sách phù hợp.
4. **M4 – Gợi ý kết hợp AI/LLM**
   - Tích hợp OpenAI/Gemini ở backend.
   - API gợi ý thông minh theo phong cách/loại phòng.
5. **M5 – Tối ưu & tài liệu**
   - Hoàn thiện README, tài liệu kiến trúc, demo.

## 6. Cách chạy backend (dự kiến)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Chi tiết cụ thể về API và cấu hình LLM sẽ được bổ sung sau khi hoàn thiện skeleton.

