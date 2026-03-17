## INTRODUCTION – Dự án DecoAR / RoomFit

### 1. Bối cảnh & Vấn đề

Khi chuyển vào một căn phòng trống hoặc muốn sắp xếp, cải tạo lại không gian sống, người dùng thường gặp 3 khó khăn lớn:

- **Khó hình dung kích thước thực tế**  
  Rất khó tưởng tượng một chiếc giường, tủ hay sofa khi mang về sẽ chiếm bao nhiêu diện tích, có che lối đi, có đụng tường hoặc cản trở cửa sổ không.

- **Khó đánh giá mức độ phù hợp với tổng thể phòng**  
  Một món đồ có thể đẹp trên website hoặc trong showroom, nhưng khi đặt vào phòng thật có thể lệch tông với màu tường, sàn, hoặc phong cách nội thất sẵn có.

- **Đo đạc thủ công mất thời gian và dễ sai**  
  Việc dùng thước dây, giấy bút để đo và ghi chép rất thủ công, dễ nhầm lẫn, và không trực quan.

Kết quả là người dùng dễ rơi vào các tình huống:
- Mua đồ nội thất không phù hợp kích thước → chật chội, bí bách.
- Mất thời gian đổi trả hoặc chấp nhận dùng tạm dù không ưng ý.

---

### 2. Mục tiêu của dự án

DecoAR / RoomFit được đề xuất như một **ứng dụng trợ lý nội thất thông minh** với hai khả năng chính:

- **Hiểu không gian thật của người dùng** thông qua camera và công nghệ AR.
- **Gợi ý và mô phỏng đồ nội thất** chi tiết và trực quan, giúp người dùng ra quyết định mua sắm và sắp xếp không gian tốt hơn.

Mục tiêu cụ thể:

- Giúp người dùng **nhìn thấy trước** cách đồ nội thất xuất hiện trong phòng của chính họ, với tỷ lệ 1:1, trước khi mua.
- Tự động **gợi ý các món đồ phù hợp** với kích thước phòng, loại phòng (phòng ngủ, phòng khách, phòng trọ, v.v.) và phong cách yêu thích (minimalist, modern, classic…).
- Giảm rủi ro khi mua đồ sai kích thước, sai phong cách và tối ưu hoá việc sử dụng không gian.

---

### 3. Ý tưởng giải pháp

Ý tưởng cốt lõi của DecoAR / RoomFit dựa trên 3 bước:

1. **Hiểu không gian (Spatial Understanding)**  
   Ứng dụng dùng camera và AR để nhận diện mặt phẳng sàn, ước lượng kích thước vùng trống. Người dùng có thể đánh dấu một khu vực cụ thể trên sàn để đo chiều dài, chiều rộng.

2. **Hiểu ngữ cảnh & sở thích (Context & Preference)**  
   Người dùng cung cấp thêm một số thông tin:
   - Loại phòng: phòng ngủ, phòng khách, phòng học, phòng trọ, v.v.
   - Phong cách mong muốn: tối giản, hiện đại, cổ điển, trẻ trung, v.v.
   - Có thể mở rộng bằng input dạng text/voice mô tả yêu cầu.

3. **Gợi ý & mô phỏng (Recommendation & AR Visualization)**  
   Backend sử dụng:
   - Dữ liệu catalog đồ nội thất (kích thước, loại, phong cách).
   - AI/LLM để chọn lọc và giải thích gợi ý.  
   Sau đó ứng dụng hiển thị:
   - **Danh sách gợi ý** (list/carousel) các món đồ phù hợp.
   - **Mô phỏng 3D trong AR**: người dùng có thể “đặt thử” từng món đồ vào phòng, xoay, kéo, di chuyển để xem bố cục.

---

### 4. Phạm vi đồ án

Trong phạm vi đồ án, dự án tập trung vào:

- **Một nền tảng chính**: Android (dùng ARCore) để đảm bảo có demo thực tế.
- **Một số loại phòng cơ bản**: ví dụ phòng ngủ và phòng khách.
- **Một bộ catalog nội thất nhỏ** nhưng được thiết kế kỹ:
  - Một số loại giường, bàn làm việc, tủ, sofa cơ bản.
  - Mỗi món có đầy đủ kích thước và metadata cần thiết.
- **Gợi ý nội thất ở 2 mức**:
  - Mức 1: gợi ý dựa trên kích thước (logic đơn giản, chưa có AI).
  - Mức 2: gợi ý thông minh hơn (kết hợp AI/LLM và phong cách).

Dự án **không đặt mục tiêu**:
- Xây dựng hệ thống thương mại điện tử hoàn chỉnh.
- Tối ưu hoá hiệu năng cho hàng nghìn đồ nội thất.
- Hỗ trợ tất cả các nền tảng (iOS, web) ngay từ đầu.

---

### 5. Giá trị & đóng góp

Về mặt học thuật và kỹ thuật, dự án cho phép:

- Kết hợp **AR (Augmented Reality)** với **AI/LLM** trong một bài toán thực tế.
- Thực hành thiết kế kiến trúc hệ thống gồm nhiều tầng:
  - Mobile AR client.
  - Backend API.
  - Tầng AI/LLM và database.
- Áp dụng tư duy thiết kế trải nghiệm người dùng (UX) cho một bài toán không gian.

Về mặt trải nghiệm người dùng, nếu được phát triển đầy đủ, hệ thống có thể:
- Giảm rủi ro mua đồ nội thất không phù hợp.
- Giúp người dùng tự tin hơn khi đưa ra quyết định sắp xếp không gian sống.
- Tạo cảm giác “chơi mà học” khi sắp xếp nội thất như trong game nhưng áp dụng cho phòng thật.

