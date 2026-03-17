## TECH STACK – Dự án DecoAR / RoomFit

File này mô tả các công nghệ chính của hệ thống, lý do lựa chọn và phạm vi sử dụng trong đồ án.

---

### 1. Kiến trúc tổng quan

- **Mobile App (AR Client)**: Android ứng dụng AR để quét phòng và hiển thị nội thất 3D.
- **Backend API (Python)**: Cung cấp API gợi ý nội thất, quản lý catalog, tích hợp LLM.
- **AI/LLM Layer**: Dùng dịch vụ LLM bên ngoài (OpenAI, Gemini, v.v.).
- **Database**: Lưu catalog nội thất và các dữ liệu cần thiết khác.

---

### 2. Mobile App (Android + ARCore)

- **Nền tảng**: Android Native.
- **Ngôn ngữ**: Kotlin (ưu tiên) hoặc Java.
- **IDE**: Android Studio.

- **AR Framework**:
  - **ARCore**:
    - Theo dõi chuyển động thiết bị.
    - Phát hiện mặt phẳng sàn và ước lượng độ sâu.
  - **Thư viện render 3D** (ví dụ: Sceneform/SceneView hoặc tương đương):
    - Render mô hình 3D (.gltf/.glb).
    - Xử lý tương tác chạm, kéo, xoay mô hình.

- **UI Layer**:
  - Jetpack Compose hoặc XML Layout.

**Vai trò chính**:
- Thu thập dữ liệu không gian (spatial data).
- Gửi ngữ cảnh (loại phòng, phong cách, yêu cầu) lên backend.
- Hiển thị danh sách gợi ý và mô hình 3D trong AR.

---

### 3. Backend API (Python + FastAPI)

- **Ngôn ngữ**: Python 3.10+.
- **Framework**: **FastAPI**
  - Tạo REST API nhanh, gọn, có tài liệu tự động (OpenAPI/Swagger).
- **ASGI Server**: **Uvicorn**.
- **Thư viện cấu hình**: `python-dotenv` (đọc biến môi trường).
- **HTTP Client**: `httpx` (gọi API LLM).

**Nhiệm vụ chính**:
- Định nghĩa các endpoint:
  - Health check.
  - Lấy danh sách/cụ thể đồ nội thất.
  - Gợi ý cơ bản (dựa trên kích thước).
  - Gợi ý thông minh (kết hợp AI/LLM).
- Xử lý logic nghiệp vụ:
  - Lọc đồ nội thất theo kích thước, loại phòng, phong cách.
  - Kết hợp kết quả từ LLM để cải thiện thứ hạng gợi ý.

---

### 4. Database & Dữ liệu nội thất

- **CSDL đề xuất**:
  - Giai đoạn đầu: **SQLite** (dễ setup, file-based, đủ dùng cho demo).
  - Có thể nâng cấp lên PostgreSQL/MySQL nếu cần.

- **ORM**:
  - **SQLAlchemy** để mapping dữ liệu Python ↔ bảng SQL.

- **Dữ liệu nội thất** (ví dụ trường):
  - `id`, `name`, `width_cm`, `depth_cm`, `height_cm`.
  - `type` (bed, desk, sofa, ...).
  - `style` (minimalist, modern, classic, ...).
  - `description`.
  - `image_url`, `model_url` (link file 3D).

---

### 5. AI/LLM Layer

- **Provider có thể sử dụng**:
  - OpenAI API.
  - Google Gemini API.
  - Hoặc mô hình LLM tương tự hỗ trợ HTTP.

- **Kết nối từ backend**:
  - Backend gọi API LLM qua HTTP (dùng `httpx`).
  - Prompt chứa:
    - Thông tin phòng (kích thước, loại).
    - Phong cách mong muốn.
    - Danh sách các furniture candidate lấy từ DB.

- **Vai trò LLM**:
  - Hiểu yêu cầu người dùng.
  - Chọn top N món nội thất phù hợp nhất.
  - Sinh ra lý do gợi ý (text) để hiển thị cho người dùng.

---

### 6. Công cụ & Hạ tầng phụ trợ

- **Quản lý mã nguồn**: Git + GitHub.
- **Môi trường phát triển**:
  - Python virtualenv/venv cho backend.
  - Android Studio cho mobile.
- **Triển khai (tuỳ phạm vi đồ án)**:
  - Backend có thể chạy local khi demo.
  - Nếu cần deploy: dùng dịch vụ PaaS (Heroku/Render/Railway, v.v.).

