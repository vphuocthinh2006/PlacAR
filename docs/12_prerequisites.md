## 12 – Prerequisites (Công cụ & Môi trường cần có)

Tài liệu này liệt kê các công cụ, phần mềm và kiến thức tối thiểu cần có để setup, phát triển và demo dự án DecoAR / RoomFit.

---

### 1. Công cụ chung

- **Git**:
  - Dùng để quản lý mã nguồn, commit và lưu phiên bản.

- **Editor/IDE**:
  - VS Code / Cursor / PyCharm cho backend.
  - Android Studio cho mobile app.

- **Python**:
  - Phiên bản: **Python 3.10+**.
  - Công cụ tạo môi trường ảo: `venv` hoặc `conda`.

---

### 2. Backend

- **Python 3.10+** đã cài đặt trên máy.
- Thư viện Python (cài qua `pip`):
  - `fastapi`
  - `uvicorn[standard]`
  - `sqlalchemy`
  - `pydantic`
  - `python-dotenv`
  - `httpx`
- (Tuỳ chọn) Công cụ test API:
  - Postman / Insomnia / cURL.

**Kiến thức nên có**:
- REST API cơ bản (GET/POST, JSON).
- Kiến thức cơ bản về SQL và ORM (SQLAlchemy).

---

### 3. Mobile (Android + AR)

- **Android Studio**:
  - Phiên bản mới tương thích Android Gradle Plugin hiện tại.
  - SDK Android đã cài.

- **Thiết bị Android**:
  - Hỗ trợ **ARCore**.
  - Có kết nối internet khi dùng tính năng AI/LLM (hoặc backend deploy trên local cùng mạng).

**Kiến thức nên có**:
- Kotlin/Java cơ bản.
- Android lifecycle, permissions (camera).
- Kiến thức cơ bản về ARCore (plane detection, session, anchors).

---

### 4. AI/LLM Provider

- **Tài khoản & API key**:
  - OpenAI / Gemini hoặc provider tương đương.
  - Quyền truy cập đủ để gửi request từ backend.

- **Kiến thức nên có**:
  - Cách gửi HTTP request đến API LLM.
  - Cách thiết kế prompt cơ bản.
  - Hiểu giới hạn:
    - Độ trễ.
    - Chi phí (nếu có).

---

### 5. Hạ tầng & môi trường demo

- **Mạng internet ổn định** (khi cần dùng AI/LLM).
- **Máy tính** đủ mạnh để:
  - Chạy Android Studio + emulator (nếu dùng).
  - Chạy backend Python.

- (Khuyến nghị) Dùng **thiết bị Android thật** thay vì emulator:
  - ARCore thường hoạt động tốt hơn trên thiết bị thật.

---

### 6. Kỹ năng mềm & tổ chức

- **Quản lý thời gian & task**:
  - Dùng Trello/Notion/GitHub Projects để theo dõi tiến độ các phase (tham chiếu `docs/04_development_roadmap.md`).

- **Viết tài liệu**:
  - Biết cách trình bày logic trong markdown.
  - Cập nhật tài liệu song song với quá trình phát triển để tránh “quên” lý do thiết kế.

