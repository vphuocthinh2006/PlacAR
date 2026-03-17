## 08 – Yêu cầu phi chức năng (Non-Functional Requirements)

Tài liệu này mô tả các yêu cầu phi chức năng quan trọng cho hệ thống DecoAR / RoomFit.

---

### 1. Hiệu năng (Performance)

- **Thời gian phản hồi backend**:
  - Mục tiêu cho các API cơ bản (không AI): `< 300ms` trên môi trường local.
  - Với API dùng AI/LLM: phụ thuộc provider, chấp nhận `1–3s`.
- **Trải nghiệm AR mượt**:
  - Tốc độ khung hình (FPS) ổn định, hạn chế lag/giật khi đặt mô hình 3D.
  - Số lượng mô hình 3D hiển thị đồng thời ở mức vừa phải (ví dụ 1–3 vật thể).

---

### 2. Khả năng sử dụng (Usability)

- **Đơn giản, dễ hiểu**:
  - Onboarding rõ ràng cho bước quét phòng và đặt đồ.
  - Các bước sử dụng ít thao tác nhất có thể.
- **Hướng dẫn trong ngữ cảnh**:
  - Tooltip ngắn giải thích khi user lần đầu dùng một tính năng.
  - Thông báo lỗi/ngầm hiểu rõ ràng (VD: “Không phát hiện được mặt phẳng, hãy di chuyển máy chậm quanh phòng”).

---

### 3. Độ tin cậy (Reliability)

- **Ổn định ứng dụng**:
  - Hạn chế crash, đặc biệt trong chế độ AR.
- **Xử lý lỗi mạng**:
  - Nếu không gọi được backend/AI:
    - Hiển thị thông báo thân thiện.
    - Cho phép retry.
  - App vẫn cho phép user dùng một số tính năng offline (ví dụ: xem lại layout đã lưu – nếu implement).

---

### 4. Bảo mật (Security) – Phù hợp phạm vi đồ án

- **API Key LLM**:
  - Không lưu API key trong mobile app.
  - API key chỉ nằm ở backend (qua biến môi trường).
- **Dữ liệu cá nhân**:
  - Giai đoạn đầu: không lưu / hoặc lưu rất ít dữ liệu nhạy cảm.
  - Không yêu cầu thông tin nhạy cảm của người dùng cuối nếu không cần thiết.

---

### 5. Khả năng mở rộng (Scalability) – Định hướng

- Giai đoạn đồ án:
  - Hệ thống chạy trên 1 backend đơn lẻ, CSDL nhỏ.
- Định hướng sau:
  - Có thể deploy backend lên cloud và scale theo số lượng user.
  - Chia nhỏ thành nhiều service nếu khối lượng tính toán gợi ý/AI tăng cao.

---

### 6. Bảo trì & Mở rộng (Maintainability & Extensibility)

- Code backend:
  - Tách rõ layer (router, service, data).
  - Có tài liệu API (`docs/07_api_endpoints.md`) để team khác dễ tiếp cận.
- Tài liệu:
  - Toàn bộ kiến thức và quyết định kỹ thuật được lưu dưới dạng markdown.
  - Dễ dàng cập nhật khi hệ thống thay đổi.

---

### 7. Khả năng kiểm thử (Testability)

- Backend:
  - Thiết kế API đơn giản, JSON-based → dễ viết test.
  - Có thể viết unit test cho service gợi ý cơ bản.
- Mobile:
  - Partial test (manual test) cho AR và UI.
  - Video demo dùng như minh chứng hành vi hệ thống.

