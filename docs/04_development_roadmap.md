## 04 – Kế hoạch phát triển (Development Roadmap)

Roadmap này giả định thời gian đồ án khoảng **10–12 tuần**, có thể điều chỉnh theo thực tế.

---

### 1. Phase 0 – Chuẩn bị & Thiết kế (Tuần 1–2)

**Mục tiêu**: Hiểu rõ bài toán, chốt phạm vi, thiết kế kiến trúc & tài liệu nền tảng.

- **Công việc chính**:
  - Viết các tài liệu:
    - `INTRODUCTION.md`
    - `TECHSTACK.md`
    - `TASKS.md`
    - `docs/01_project_overview.md`
    - `docs/02_system_architecture.md`
    - `docs/03_user_features.md`
  - Chốt:
    - Nền tảng mobile: Android + ARCore.
    - Backend: Python + FastAPI.
    - CSDL: SQLite (giai đoạn đầu).
    - Provider AI/LLM mục tiêu (OpenAI/Gemini).
  - Vẽ sơ đồ kiến trúc hệ thống (dùng draw.io, Figma, v.v.).
  - Thiết kế wireframe UI cho các màn hình chính.

**Deliverables**:
- Bộ tài liệu markdown hoàn chỉnh cho phần giới thiệu, kiến trúc, tính năng.
- Repo khởi tạo với cấu trúc thư mục rõ ràng.

---

### 2. Phase 1 – Prototype AR & Mobile Skeleton (Tuần 3–4)

**Mục tiêu**: Có demo AR cơ bản: nhận diện mặt phẳng & đặt mô hình 3D đơn giản.

- **Công việc chính**:
  - Tạo project Android:
    - Cấu hình minSdk, permissions camera.
  - Tích hợp ARCore:
    - Hiển thị camera preview.
    - Nhận diện mặt phẳng sàn.
  - Đặt mô hình 3D mẫu (hình hộp) lên mặt phẳng:
    - Tap để đặt mô hình.
    - Di chuyển/xoay cơ bản.
  - Prototype chức năng đo kích thước:
    - Tap chọn điểm A và B trên sàn → hiển thị khoảng cách.

**Deliverables**:
- App Android chạy được trên thiết bị thật.
- Video ngắn quay lại thao tác: quét phòng + đặt mô hình 3D mẫu.

---

### 3. Phase 2 – Backend & Catalog nội thất (Tuần 5–6)

**Mục tiêu**: Hoàn thiện backend cơ bản & catalog nội thất đủ dùng demo.

- **Công việc chính**:
  - Thiết kế schema dữ liệu:
    - Bảng `furniture_items` với đầy đủ thuộc tính (kích thước, loại, style, mô tả, link model 3D).
  - Thiết lập backend:
    - FastAPI project skeleton.
    - Kết nối DB (SQLite + SQLAlchemy).
  - Seed dữ liệu:
    - Tạo script populate 10–30 món đồ nội thất.
  - Thiết kế API cơ bản:
    - `GET /furniture` – danh sách.
    - `GET /furniture/{id}` – chi tiết.
    - `POST /recommend/basic` – gợi ý theo kích thước (không dùng AI).

**Deliverables**:
- Backend chạy được local, có thể test bằng Swagger UI.
- Dữ liệu nội thất được lưu trong DB và truy vấn qua API.

---

### 4. Phase 3 – Gợi ý thông minh với AI/LLM (Tuần 7–8)

**Mục tiêu**: Nâng cấp tính năng gợi ý lên phiên bản “thông minh” có AI/LLM.

- **Công việc chính**:
  - Phân tích logic gợi ý:
    - Đầu vào: kích thước, loại phòng, phong cách, ghi chú.
    - Đầu ra: top N món nội thất + lý do chi tiết.
  - Thiết kế prompt:
    - Viết prompt mẫu, thử nghiệm trên playground (OpenAI/Gemini).
  - Tích hợp LLM vào backend:
    - Module gọi API LLM (trong backend).
    - Pipeline: DB filter → chuẩn bị prompt → LLM → parse result.
  - Tạo endpoint:
    - `POST /recommend/ai` – trả về danh sách gợi ý từ LLM.

**Deliverables**:
- API `/recommend/ai` hoạt động ổn định với bộ dữ liệu mẫu.
- Ví dụ response JSON minh họa được tính “thông minh” của hệ thống.

---

### 5. Phase 4 – Tích hợp End-to-End & UX (Tuần 9–10)

**Mục tiêu**: Nối toàn bộ pipeline từ mobile → backend → AI → AR, tối ưu UX.

- **Công việc chính**:
  - Mobile:
    - Gửi request đến backend khi user cung cấp thông tin phòng & ngữ cảnh.
    - Nhận list gợi ý và hiển thị đẹp (card/carousel).
    - Cho phép chọn item → tải model 3D tương ứng → đặt trong AR.
  - Cải thiện AR:
    - Scale mô hình đúng kích thước.
    - Cải thiện điều khiển (drag/rotate).
  - Cải thiện UI/UX:
    - Onboarding/hướng dẫn.
    - Trạng thái loading, error, retry khi backend/AI lỗi.

**Deliverables**:
- Demo hoàn chỉnh:
  - Scan phòng → nhập ngữ cảnh → nhận gợi ý → đặt đồ 3D trong AR.
- Video demo end-to-end (phục vụ bảo vệ).

---

### 6. Phase 5 – Tài liệu, tối ưu & chuẩn bị bảo vệ (Tuần 11–12)

**Mục tiêu**: Hoàn thiện tài liệu, slide, ổn định hệ thống cho buổi bảo vệ.

- **Công việc chính**:
  - Cập nhật tài liệu:
    - Kiến trúc hệ thống.
    - Thiết kế dữ liệu, API.
    - Tích hợp AI/LLM.
    - Yêu cầu phi chức năng, rủi ro & giải pháp.
  - Chuẩn bị slide:
    - Problem → Solution → Demo → Tech → Architecture → Future Work.
  - Luyện demo & trả lời câu hỏi:
    - Các quyết định kỹ thuật quan trọng.
    - Hạn chế hiện tại & hướng mở rộng.

**Deliverables**:
- Bộ tài liệu hoàn chỉnh (Markdown + PDF nếu cần).
- Slide thuyết trình và video demo cuối cùng.

