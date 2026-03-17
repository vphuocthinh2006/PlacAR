## 06 – Cấu trúc dự án (Project Structure)

### 1. Mục tiêu

Mục tiêu của cấu trúc dự án là:

- Tách bạch rõ ràng giữa:
  - Tài liệu (docs).
  - Backend.
  - Mobile app.
- Thuận tiện cho việc:
  - Phát triển, bảo trì.
  - Trình bày trong báo cáo/bảo vệ đồ án.

---

### 2. Cấu trúc tổng quan (dự kiến)

```text
PlacAR/
  INTRODUCTION.md
  TECHSTACK.md
  TASKS.md
  README.md

  backend/
    requirements.txt
    app/
      __init__.py
      main.py
      config.py
      models.py        # (dự kiến)
      schemas.py
      db.py            # (dự kiến) kết nối DB
      services/
        __init__.py
        recommendation.py
        furniture.py    # (dự kiến) service quản lý catalog

  mobile/              # (dự kiến)
    app/               # source Android app (Kotlin)
    README.md          # hướng dẫn build & run

  docs/
    01_project_overview.md
    02_system_architecture.md
    03_user_features.md
    04_development_roadmap.md
    06_project_structure.md
    07_api_endpoints.md           # (dự kiến)
    08_non_functional_requirements.md
    09_risks_and_solutions.md
    10_expansion_direction.md
    12_prerequisites.md
```

Các file/bộ phận được đánh **(dự kiến)** là những phần sẽ được bổ sung dần trong các phase tiếp theo.

---

### 3. Mô tả các phần chính

#### 3.1. Thư mục gốc (Root)

- `INTRODUCTION.md`  
  Giới thiệu bối cảnh, vấn đề, mục tiêu và ý tưởng giải pháp của dự án.

- `TECHSTACK.md`  
  Mô tả chi tiết các công nghệ sử dụng cho từng phần: Mobile, Backend, AI, DB, hạ tầng.

- `TASKS.md`  
  Danh sách task chi tiết theo giai đoạn, đóng vai trò như “backlog” tổng quan.

- `README.md`  
  Mô tả tổng quát repo, hướng dẫn nhanh về cách chạy backend, roadmap ngắn gọn.

#### 3.2. Backend

- `backend/requirements.txt`  
  Danh sách thư viện Python cần cài cho backend.

- `backend/app/`  
  - `main.py`: entry point FastAPI, định nghĩa các route chính.
  - `config.py`: cấu hình hệ thống (tên app, ENV, key LLM, v.v.).
  - `schemas.py`: Pydantic models cho request/response.
  - `models.py`: (dự kiến) SQLAlchemy models mapping DB.
  - `db.py`: (dự kiến) logic kết nối database, session.
  - `services/`: chứa các module xử lý business logic.
    - `recommendation.py`: logic gợi ý cơ bản.
    - `furniture.py`: (dự kiến) quản lý catalog đồ nội thất.

#### 3.3. Mobile

- `mobile/`  
  - Thư mục sẽ được tạo và điền nội dung khi bắt đầu Phase 1.
  - Bao gồm:
    - Source code Android (Kotlin).
    - File cấu hình Gradle.
    - README riêng cho việc build & run app mobile.

#### 3.4. Docs

- `docs/01_project_overview.md`  
  Tổng quan dự án: bối cảnh, mục tiêu, phạm vi, đối tượng người dùng, giá trị.

- `docs/02_system_architecture.md`  
  Kiến trúc hệ thống: các thành phần, luồng dữ liệu, quyết định kiến trúc.

- `docs/03_user_features.md`  
  Tính năng người dùng, user flow, use cases và ưu tiên tính năng.

- `docs/04_development_roadmap.md`  
  Roadmap phát triển theo phase/tuần, mục tiêu và deliverables của từng giai đoạn.

- `docs/06_project_structure.md`  
  Tài liệu hiện tại, mô tả cấu trúc thư mục và vai trò từng phần.

- `docs/07_api_endpoints.md` (dự kiến)  
  Sẽ mô tả chi tiết các endpoint của backend, bao gồm input/output JSON.

- `docs/08_non_functional_requirements.md`  
  Các yêu cầu phi chức năng: hiệu năng, bảo mật, usability, maintainability…

- `docs/09_risks_and_solutions.md`  
  Phân tích rủi ro (technical & non-technical), kèm giải pháp/mitigation.

- `docs/10_expansion_direction.md`  
  Định hướng mở rộng hệ thống trong tương lai (tính năng, kiến trúc, scale).

- `docs/12_prerequisites.md`  
  Liệt kê các công cụ và môi trường cần có để chạy/đóng góp cho dự án.

---

### 4. Nguyên tắc tổ chức & đặt tên

- Tài liệu:
  - Đặt tên file theo format `NN_title_khong_dau.md` để:
    - Dễ sắp xếp theo thứ tự logic.
    - Dễ tham chiếu trong báo cáo.

- Code:
  - Tách backend và mobile rõ ràng theo thư mục cấp 1.
  - Bên trong backend:
    - Phân tầng: `app/` (code), `services/` (business logic), `models/schemas` (data).

---

### 5. Hướng mở rộng cấu trúc

Trong tương lai, nếu hệ thống lớn hơn, có thể:

- Thêm thư mục:
  - `tests/` cho unit test và integration test.
  - `scripts/` cho các script tiện ích (seed data, migrate, deploy).
  - `infra/` hoặc `deploy/` cho tài liệu và cấu hình hạ tầng (Docker, CI/CD).

- Tách nhỏ backend thành nhiều module/service nếu muốn tiến tới kiến trúc microservices.

