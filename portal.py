"""Trang cổng chọn thiết bị (Điện thoại / Máy tính) chạy trực tiếp bằng Streamlit.

Sử dụng st.link_button ở cấp trang chính để chuyển hướng 100% không bị chặn sandbox iframe trên Safari/iOS.
"""
import streamlit as st

st.set_page_config(
    page_title="L² Dev | Màn hình thông minh – Giấc ngủ an lành",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================================
# 2 ĐƯỜNG LINK DẪN TỚI 2 WEB KHÁC NHAU CỦA BẠN
# =========================================================================
MOBILE_APP_URL = "https://miniappcuanhombb.streamlit.app"
DESKTOP_APP_URL = "https://miniappcuanhomb.streamlit.app"

st.markdown(
    """
    <style>
    header[data-testid="stHeader"],
    div[data-testid="stToolbar"],
    div[data-testid="stDecoration"],
    footer {
        display: none !important;
    }

    .stApp {
        background-color: #060913;
        background-image:
            radial-gradient(circle at 18% 15%, rgba(59, 130, 246, 0.14) 0%, transparent 45%),
            radial-gradient(circle at 82% 85%, rgba(129, 140, 248, 0.12) 0%, transparent 45%);
        color: #F8FAFC;
    }

    .block-container {
        max-width: 960px !important;
        padding-top: 1.5rem !important;
        padding-bottom: 2.5rem !important;
        padding-left: 1.1rem !important;
        padding-right: 1.1rem !important;
    }

    /* TOPBAR */
    .topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 12px;
        margin-bottom: 28px;
    }
    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .brand-logo {
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
    }
    .brand-title {
        font-size: 1.12rem;
        font-weight: 800;
        color: #FFFFFF;
    }
    .brand-sub {
        font-size: 0.72rem;
        color: #94A3B8;
        letter-spacing: 0.06em;
        text-transform: uppercase;
    }
    .badge-stem {
        font-size: 0.75rem;
        font-weight: 600;
        color: #93C5FD;
        background: rgba(59, 130, 246, 0.12);
        border: 1px solid rgba(96, 165, 250, 0.28);
        padding: 6px 14px;
        border-radius: 999px;
    }

    /* HERO */
    .hero-wrap {
        text-align: center;
        margin-bottom: 28px;
    }
    .hero-tag {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-size: 0.8rem;
        color: #60A5FA;
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid #1E293B;
        padding: 6px 16px;
        border-radius: 999px;
        margin-bottom: 16px;
    }
    .dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: #60A5FA;
        box-shadow: 0 0 8px #60A5FA;
    }
    .hero-h1 {
        font-size: clamp(1.7rem, 4.5vw, 2.6rem);
        font-weight: 900;
        line-height: 1.18;
        margin: 0 0 12px 0;
        color: #FFFFFF;
    }
    .hero-h1 span {
        background: linear-gradient(90deg, #60A5FA, #818CF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-sub {
        font-size: 0.94rem;
        color: #94A3B8;
        max-width: 580px;
        margin: 0 auto;
        line-height: 1.6;
    }

    /* DEVICE CARDS */
    .device-card {
        background: linear-gradient(160deg, rgba(15, 23, 42, 0.96), rgba(9, 13, 24, 0.98));
        border: 1px solid #1E293B;
        border-radius: 18px;
        padding: 24px 22px 18px 22px;
        margin-bottom: 10px;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.45);
    }
    .device-card.mobile-highlight {
        border-color: rgba(96, 165, 250, 0.55);
        box-shadow: 0 12px 34px rgba(37, 99, 235, 0.22);
    }
    .icon-box {
        width: 50px;
        height: 50px;
        border-radius: 13px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 16px;
    }
    .icon-mobile {
        background: rgba(59, 130, 246, 0.15);
        border: 1px solid rgba(96, 165, 250, 0.3);
        color: #60A5FA;
    }
    .icon-desktop {
        background: rgba(129, 140, 248, 0.15);
        border: 1px solid rgba(165, 180, 252, 0.3);
        color: #A5B4FC;
    }
    .card-title {
        font-size: 1.25rem;
        font-weight: 800;
        margin-bottom: 8px;
        color: #FFFFFF;
    }
    .card-desc {
        font-size: 0.87rem;
        color: #94A3B8;
        line-height: 1.55;
        margin-bottom: 16px;
    }
    .feature-list {
        list-style: none;
        padding: 0;
        margin: 0;
        display: flex;
        flex-direction: column;
        gap: 7px;
    }
    .feature-list li {
        font-size: 0.82rem;
        color: #CBD5E1;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .feature-list li::before {
        content: "✓";
        color: #60A5FA;
        font-weight: 800;
    }

    /* TÙY CHỈNH ST.LINK_BUTTON THÀNH NÚT CHUYỂN HƯỚNG LỚN */
    div[data-testid="stLinkButton"] > a {
        border-radius: 12px !important;
        min-height: 48px !important;
        font-weight: 700 !important;
        font-size: 0.94rem !important;
        transition: all 0.2s ease !important;
        text-decoration: none !important;
    }
    div[data-testid="stLinkButton"] > a[kind="primary"] {
        background: linear-gradient(135deg, #3B82F6, #2563EB) !important;
        border: 1px solid #60A5FA !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 16px rgba(37, 99, 235, 0.45) !important;
    }
    div[data-testid="stLinkButton"] > a[kind="secondary"] {
        background-color: #1E293B !important;
        border: 1px solid #334155 !important;
        color: #F8FAFC !important;
    }
    div[data-testid="stLinkButton"] > a[kind="secondary"]:hover {
        border-color: #60A5FA !important;
        background: linear-gradient(135deg, #4F46E5, #3B82F6) !important;
        color: #FFFFFF !important;
    }

    .portal-footer {
        text-align: center;
        font-size: 0.78rem;
        color: #64748B;
        margin-top: 32px;
        padding-top: 16px;
        border-top: 1px solid rgba(30, 41, 59, 0.6);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# TOPBAR
st.markdown(
    """
    <div class="topbar">
        <div class="brand">
            <div class="brand-logo">LL</div>
            <div>
                <div class="brand-title">LongLe Dev</div>
                <div class="brand-sub">Phone Usage &amp; Sleep Analytics</div>
            </div>
        </div>
        <div class="badge-stem">STEM Tin học 9 • Nhóm B</div>
    </div>

    <div class="hero-wrap">
        <div class="hero-tag">
            <span class="dot"></span>
            <span>Chọn giao diện phù hợp với thiết bị của bạn</span>
        </div>
        <h1 class="hero-h1">MÀN HÌNH THÔNG MINH.<br><span>GIẤC NGỦ AN LÀNH.</span></h1>
        <p class="hero-sub">
            Hệ thống phân tích dữ liệu khảo sát thời gian sử dụng điện thoại và chất lượng giấc ngủ.
            Vui lòng chọn phiên bản hiển thị tối ưu cho thiết bị bạn đang dùng.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# 2 THẺ LỰA CHỌN + ST.LINK_BUTTON CHUYỂN HƯỚNG TRỰC TIẾP
col_mobile, col_desktop = st.columns(2, gap="medium")

with col_mobile:
    st.markdown(
        """
        <div class="device-card mobile-highlight">
            <div class="icon-box icon-mobile">
                <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
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
                <li>Menu gọn 1 dòng, biểu đồ khóa cuộn nhầm</li>
                <li>Tải nhanh khi quét mã QR trên lớp</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.link_button(
        "📱 Mở bản Điện thoại →",
        url=MOBILE_APP_URL,
        type="primary",
        use_container_width=True,
    )

with col_desktop:
    st.markdown(
        """
        <div class="device-card">
            <div class="icon-box icon-desktop">
                <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
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
        """,
        unsafe_allow_html=True,
    )
    st.link_button(
        "💻 Mở bản Máy tính →",
        url=DESKTOP_APP_URL,
        type="secondary",
        use_container_width=True,
    )

st.markdown(
    """
    <div class="portal-footer">
        Sản phẩm học tập STEM – Tin học 9 | Made by LongLe Dev | Dữ liệu ẩn danh vì sức khỏe học đường
    </div>
    """,
    unsafe_allow_html=True,
)
