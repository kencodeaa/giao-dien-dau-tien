"""Trang cổng chọn thiết bị (Điện thoại / Máy tính) chạy trực tiếp bằng Streamlit.

Giúp người dùng mở một đường link duy nhất, chọn giao diện phù hợp (Điện thoại hoặc Máy tính)
và chuyển hướng tới 2 ứng dụng Streamlit khác nhau.
"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="L² Dev | Màn hình thông minh – Giấc ngủ an lành",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================================
# CẤU HÌNH 2 ĐƯỜNG LINK DẪN TỚI 2 WEB KHÁC NHAU (THAY LINK CỦA BẠN VÀO ĐÂY)
# =========================================================================
MOBILE_APP_URL = "https://miniappcuanhombb.streamlit.app"
DESKTOP_APP_URL = "https://miniappcuanhomb.streamlit.app"

st.markdown(
    """
    <style>
    header[data-testid="stHeader"], footer {
        display: none !important;
    }
    .stApp {
        background-color: #060913;
    }
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    iframe {
        display: block;
        width: 100%;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

html_code = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>L² Dev | Màn hình thông minh – Giấc ngủ an lành</title>
  <style>
    :root {{
      --bg-main: #060913;
      --bg-card: #0F172A;
      --bg-card-hover: #131E36;
      --border-subtle: #1E293B;
      --primary: #3B82F6;
      --primary-light: #60A5FA;
      --indigo: #818CF8;
      --text-main: #F8FAFC;
      --text-muted: #94A3B8;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Inter, sans-serif;
      background-color: var(--bg-main);
      background-image:
        radial-gradient(circle at 18% 15%, rgba(59, 130, 246, 0.14) 0%, transparent 45%),
        radial-gradient(circle at 82% 85%, rgba(129, 140, 248, 0.12) 0%, transparent 45%);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 24px 18px;
    }}

    .topbar {{
      max-width: 980px;
      width: 100%;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .brand-logo {{
      width: 42px;
      height: 42px;
      border-radius: 12px;
      background: linear-gradient(135deg, #3B82F6, #2563EB);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 900;
      font-size: 1rem;
      color: #fff;
      box-shadow: 0 4px 18px rgba(59, 130, 246, 0.45);
    }}

    .brand-title {{
      font-size: 1.1rem;
      font-weight: 800;
      letter-spacing: 0.03em;
    }}

    .brand-sub {{
      font-size: 0.72rem;
      color: var(--text-muted);
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }}

    .badge-stem {{
      font-size: 0.75rem;
      font-weight: 600;
      color: #93C5FD;
      background: rgba(59, 130, 246, 0.12);
      border: 1px solid rgba(96, 165, 250, 0.28);
      padding: 6px 14px;
      border-radius: 999px;
    }}

    .container {{
      max-width: 920px;
      width: 100%;
      margin: auto;
      text-align: center;
      padding: 28px 0;
    }}

    .hero-tag {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.8rem;
      color: var(--primary-light);
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid var(--border-subtle);
      padding: 6px 16px;
      border-radius: 999px;
      margin-bottom: 18px;
    }}

    .dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--primary-light);
      box-shadow: 0 0 8px var(--primary-light);
    }}

    h1 {{
      font-size: clamp(1.75rem, 4vw, 2.65rem);
      font-weight: 900;
      line-height: 1.18;
      margin-bottom: 14px;
      letter-spacing: -0.01em;
    }}

    h1 span {{
      background: linear-gradient(90deg, #60A5FA, #818CF8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .subtitle {{
      font-size: 0.96rem;
      color: var(--text-muted);
      max-width: 580px;
      margin: 0 auto 36px auto;
      line-height: 1.6;
    }}

    .cards {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 22px;
      text-align: left;
    }}

    .device-card {{
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      background: linear-gradient(160deg, rgba(15, 23, 42, 0.96), rgba(9, 13, 24, 0.98));
      border: 1px solid var(--border-subtle);
      border-radius: 20px;
      padding: 28px 26px;
      text-decoration: none;
      color: inherit;
      transition: all 0.28s cubic-bezier(0.25, 0.8, 0.25, 1);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.45);
      overflow: hidden;
    }}

    .device-card:hover {{
      transform: translateY(-6px);
      background: var(--bg-card-hover);
      border-color: var(--primary-light);
      box-shadow: 0 18px 38px rgba(37, 99, 235, 0.28), 0 0 18px rgba(96, 165, 250, 0.2);
    }}

    .device-card.recommended {{
      border-color: rgba(96, 165, 250, 0.55);
      box-shadow: 0 12px 34px rgba(37, 99, 235, 0.22);
    }}

    .rec-badge {{
      position: absolute;
      top: 18px;
      right: 18px;
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      background: rgba(59, 130, 246, 0.2);
      color: #93C5FD;
      border: 1px solid rgba(96, 165, 250, 0.4);
      padding: 4px 10px;
      border-radius: 999px;
      display: none;
    }}

    .device-card.recommended .rec-badge {{
      display: inline-block;
    }}

    .icon-box {{
      width: 54px;
      height: 54px;
      border-radius: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 20px;
    }}

    .icon-mobile {{
      background: rgba(59, 130, 246, 0.15);
      border: 1px solid rgba(96, 165, 250, 0.3);
      color: #60A5FA;
    }}

    .icon-desktop {{
      background: rgba(129, 140, 248, 0.15);
      border: 1px solid rgba(165, 180, 252, 0.3);
      color: #A5B4FC;
    }}

    .card-title {{
      font-size: 1.3rem;
      font-weight: 800;
      margin-bottom: 8px;
      color: #FFFFFF;
    }}

    .card-desc {{
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.55;
      margin-bottom: 22px;
    }}

    .feature-list {{
      list-style: none;
      margin-bottom: 24px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .feature-list li {{
      font-size: 0.82rem;
      color: #CBD5E1;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .feature-list li::before {{
      content: "✓";
      color: var(--primary-light);
      font-weight: 800;
    }}

    .cta-btn {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      width: 100%;
      padding: 13px 18px;
      border-radius: 12px;
      font-size: 0.92rem;
      font-weight: 700;
      transition: all 0.2s ease;
    }}

    .cta-mobile {{
      background: linear-gradient(135deg, #3B82F6, #2563EB);
      color: #FFFFFF;
      box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);
    }}

    .cta-desktop {{
      background: #1E293B;
      color: #F8FAFC;
      border: 1px solid #334155;
    }}

    .device-card:hover .cta-desktop {{
      background: linear-gradient(135deg, #4F46E5, #3B82F6);
      border-color: transparent;
    }}

    footer {{
      max-width: 980px;
      width: 100%;
      margin: 0 auto;
      text-align: center;
      font-size: 0.78rem;
      color: #64748B;
      padding-top: 16px;
      border-top: 1px solid rgba(30, 41, 59, 0.6);
    }}

    @media (max-width: 720px) {{
      .topbar {{
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
      }}
      .cards {{
        grid-template-columns: 1fr;
        gap: 16px;
      }}
      .device-card {{
        padding: 22px 20px;
      }}
      .subtitle {{
        margin-bottom: 24px;
        font-size: 0.9rem;
      }}
    }}
  </style>
</head>
<body>

  <header class="topbar">
    <div class="brand">
      <div class="brand-logo">LL</div>
      <div>
        <div class="brand-title">LongLe Dev</div>
        <div class="brand-sub">Phone Usage &amp; Sleep Analytics</div>
      </div>
    </div>
    <div class="badge-stem">STEM Tin học 9 • Nhóm B</div>
  </header>

  <main class="container">
    <div class="hero-tag">
      <span class="dot"></span>
      <span>Chọn giao diện phù hợp với thiết bị của bạn</span>
    </div>

    <h1>MÀN HÌNH THÔNG MINH.<br><span>GIẤC NGỦ AN LÀNH.</span></h1>
    <p class="subtitle">
      Hệ thống phân tích dữ liệu khảo sát thời gian sử dụng điện thoại và chất lượng giấc ngủ.
      Vui lòng chọn phiên bản hiển thị tối ưu cho thiết bị bạn đang dùng.
    </p>

    <div class="cards">
      <a id="link-mobile" href="{MOBILE_APP_URL}" target="_top" class="device-card">
        <span class="rec-badge">Gợi ý cho thiết bị này</span>
        <div>
          <div class="icon-box icon-mobile">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="6" y="2" width="12" height="20" rx="2.5"></rect>
              <line x1="12" y1="18" x2="12.01" y2="18"></line>
            </svg>
          </div>
          <div class="card-title">Phiên bản Điện thoại</div>
          <p class="card-desc">
            Giao diện dọc tinh gọn, tối ưu thao tác một tay và màn hình cảm ứng (iPhone / Android).
          </p>
          <ul class="feature-list">
            <li>Bố cục 1 cột dọc chống tràn viền</li>
            <li>Nút bấm lớn, biểu đồ khóa cuộn nhầm</li>
            <li>Tải nhanh khi quét mã QR trên lớp</li>
          </ul>
        </div>
        <div class="cta-btn cta-mobile">Mở bản Điện thoại →</div>
      </a>

      <a id="link-desktop" href="{DESKTOP_APP_URL}" target="_top" class="device-card">
        <span class="rec-badge">Gợi ý cho thiết bị này</span>
        <div>
          <div class="icon-box icon-desktop">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="3" width="20" height="14" rx="2"></rect>
              <line x1="8" y1="21" x2="16" y2="21"></line>
              <line x1="12" y1="17" x2="12" y2="21"></line>
            </svg>
          </div>
          <div class="card-title">Phiên bản Máy tính</div>
          <p class="card-desc">
            Dashboard màn hình rộng đầy đủ tính năng, phù hợp trình chiếu, nhập liệu Excel và phân tích sâu.
          </p>
          <ul class="feature-list">
            <li>Hiển thị đa cột KPI &amp; biểu đồ song song</li>
            <li>Đầy đủ bảng tra cứu &amp; công thức Excel</li>
            <li>Tối ưu cho Laptop, PC &amp; Máy chiếu lớp học</li>
          </ul>
        </div>
        <div class="cta-btn cta-desktop">Mở bản Máy tính →</div>
      </a>
    </div>
  </main>

  <footer>
    Sản phẩm học tập STEM – Tin học 9 | Made by LongLe Dev | Dữ liệu ẩn danh vì sức khỏe học đường
  </footer>

  <script>
    const mobileCard = document.getElementById("link-mobile");
    const desktopCard = document.getElementById("link-desktop");

    const isMobileDevice = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)
      || window.innerWidth <= 768;

    if (isMobileDevice) {{
      mobileCard.classList.add("recommended");
    }} else {{
      desktopCard.classList.add("recommended");
    }}
  </script>
</body>
</html>
"""

components.html(html_code, height=920, scrolling=True)
