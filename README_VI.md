# BHBot 

Bot nuôi vàng/XP cho Brawlhalla 

Lấy cảm hứng mạnh mẽ từ [BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ) 

### ------ -------------------------------------------------- ----------- 

### BOT ĐANG TRỞ LẠI ĐƯỢC BẢO TRÌ TÍCH CỰC! 
###### Tham gia [Discord](https://discord.gg/2HDmuqqq9p "Discord") để giúp duy trì bot hoặc thêm các tính năng mới! 

### ----------------------------------------------- -------------------- 

**CẢNH BÁO:** Phần mềm ban đầu được phát triển cho mục đích sử dụng cá nhân. 
Mặc dù nó không được thiết kế để làm điều đó nhưng nó có thể dẫn đến những kết quả không lường trước được, bao gồm cả việc thực hiện các giao dịch trong Mallhalla bằng tiền tệ trong trò chơi. 

**Các nhà phát triển từ chối mọi trách nhiệm pháp lý đối với mọi thiệt hại có thể phát sinh từ việc sử dụng phần mềm này. Bạn nên thận trọng khi tiếp tục và sử dụng phần mềm theo quyết định riêng của mình.** 

(Bot đã được nhiều người thử nghiệm trong hơn 3.000 giờ mà không gặp vấn đề gì kể từ ngày 18/4/2024) 

# Cài đặt 
Bản phát hành mới nhất luôn có thể được tải xuống [tại đây ](https://github.com/Nick2bad4u/BHBot/releases) 

# Tính năng 

- Hoạt động hoàn toàn ở chế độ nền 
- Gửi thông tin đầu vào trực tiếp đến Brawlhalla để không làm phiền bạn 
- Tự động khởi chạy trò chơi 
- Tự động tạo/thiết lập sảnh 
- Tự động chọn/thay đổi thời lượng nhân vật và trò chơi 
- Tự động phát hiện và đặt lại giới hạn xp 
- Hỗ trợ các chế độ tùy chỉnh 
- Hỗ trợ ngôn ngữ tùy chỉnh 
- Thậm chí còn hỗ trợ phông chữ tùy chỉnh 
- ~~ Pha cà phê cho bạn~~ (hiện chỉ hỗ trợ trà) 

# Cách sử dụng 
- Quá trình này được thiết kế trực quan. Chỉ cần chọn cài đặt cần thiết bằng cách nhấp vào nút "Cài đặt" 
- Sau khi cài đặt được lưu, hãy khởi động chương trình bằng cách nhấp vào nút "Bắt đầu" 

# Hạn chế 
- Bot yêu cầu đặt "Thu gọn chéo" thành Có. Nếu bạn cho rằng nó nên tự động đặt thành như vậy, vui lòng [mở một vấn đề](https://github.com/nick2bad4u/bhbot/issues) 
- Bot yêu cầu ngôn ngữ trong trò chơi phải được đặt thành tiếng Anh. Nếu bạn cho rằng nó nên tự động đặt thành như vậy, vui lòng [mở một vấn đề](https://github.com/nick2bad4u/bhbot/issues) 

# Tổng quan về kỹ thuật 
- Mã cơ bản luôn có sẵn để mọi người xem xét. 
- Về cơ bản, bot sử dụng API SendMessage của Windows để truyền dữ liệu đầu vào trực tiếp đến cửa sổ Brawlhalla. Nó sử dụng tính năng phát hiện pixel để phân biệt các trạng thái và xác định hành động thích hợp tại bất kỳ thời điểm nào.

- Lớp BrawlhallaBot có thể được sử dụng trực tiếp hoặc bạn có thể phát triển trình bao bọc tùy chỉnh cho nó. Nó được thiết kế để hoạt động độc lập, với gui.py chỉ đóng vai trò là trình bao bọc đồ họa sử dụng PySimpleGUI.
