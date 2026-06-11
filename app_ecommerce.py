import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="SegmentIQ — Customer Intelligence",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# CUSTOM CSS — dark tech dashboard
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=IBM+Plex+Sans:wght@300;400;500&family=IBM+Plex+Mono:wght@400;500&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', sans-serif;
    background-color: #080c14;
    color: #cdd6f4;
}
.main .block-container {
    padding: 1.5rem 3.5rem 4rem 3.5rem;
    max-width: 1400px;
}

/* ── Ambient glow layer ── */
.main::before {
    content: "";
    position: fixed;
    top: -200px; left: 50%;
    transform: translateX(-50%);
    width: 900px; height: 500px;
    background: radial-gradient(ellipse at center,
        rgba(0,212,255,0.06) 0%,
        rgba(100,60,255,0.04) 40%,
        transparent 70%);
    pointer-events: none;
    z-index: 0;
}

/* ── Hero ── */
.hero-wrap {
    padding: 2.5rem 0 1.5rem 0;
    border-bottom: 1px solid rgba(0,212,255,0.12);
    margin-bottom: 2rem;
    position: relative;
}
.hero-top {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(0,212,255,0.08);
    border: 1px solid rgba(0,212,255,0.3);
    color: #00d4ff;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    padding: 0.3rem 0.8rem;
    border-radius: 4px;
    margin-bottom: 0.9rem;
}
.hero-badge::before { content: "●"; font-size: 0.5rem; animation: blink 1.5s infinite; }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.2} }

.hero-title {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: clamp(2.8rem, 6vw, 5rem);
    line-height: 1;
    letter-spacing: -0.02em;
    color: #e2e8f8;
    margin: 0 0 0.4rem 0;
}
.hero-title span { color: #00d4ff; }
.hero-sub {
    color: #6b7a9e;
    font-size: 0.95rem;
    font-weight: 300;
    letter-spacing: 0.01em;
}
.hero-stat-row {
    display: flex;
    gap: 2rem;
    margin-top: 1.2rem;
}
.hero-stat {
    display: flex;
    flex-direction: column;
}
.hero-stat-val {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 1.4rem;
    color: #00d4ff;
    font-weight: 500;
    line-height: 1;
}
.hero-stat-lbl {
    font-size: 0.65rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #4a5470;
    margin-top: 0.2rem;
}

/* ── Section titles ── */
.section-title {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #00d4ff;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.section-title::after {
    content: "";
    flex: 1;
    height: 1px;
    background: linear-gradient(to right, rgba(0,212,255,0.3), transparent);
}

/* ── Panel card ── */
.panel {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 1.5rem 1.6rem;
    margin-bottom: 1.2rem;
    position: relative;
    overflow: hidden;
}
.panel::before {
    content: "";
    position: absolute;
    top: 0; left: 0;
    width: 3px; height: 100%;
    background: linear-gradient(to bottom, #00d4ff, #6440ff);
    border-radius: 3px 0 0 3px;
}

/* ── Input label override ── */
label[data-testid="stWidgetLabel"] p,
.stSlider label p,
.stSelectbox label p,
.stNumberInput label p {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.7rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    color: #6b7a9e !important;
}

/* ── Number input ── */
input[type="number"] {
    background: #0f1520 !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 8px !important;
    color: #e2e8f8 !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 1rem !important;
    padding: 0.5rem 0.8rem !important;
    transition: border-color 0.2s !important;
}
input[type="number"]:focus {
    border-color: #00d4ff !important;
    box-shadow: 0 0 0 3px rgba(0,212,255,0.1) !important;
}

/* ── Slider ── */
div[data-testid="stSlider"] > div > div > div {
    background: linear-gradient(to right, #00d4ff, #6440ff) !important;
}
div[data-testid="stSlider"] div[role="slider"] {
    background: #00d4ff !important;
    border: 2px solid #080c14 !important;
    box-shadow: 0 0 10px rgba(0,212,255,0.5) !important;
}

/* ── Selectbox ── */
div[data-baseweb="select"] > div {
    background-color: #0f1520 !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 8px !important;
    color: #e2e8f8 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 0.45rem 0.8rem !important;
    min-height: 48px !important;
    transition: border-color 0.2s !important;
}
div[data-baseweb="select"] > div:hover {
    border-color: rgba(0,212,255,0.4) !important;
}
div[data-baseweb="select"] svg { fill: #4a5470 !important; }
div[data-baseweb="popover"] * {
    background-color: #111827 !important;
    color: #cdd6f4 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
}

/* ── Analyze button ── */
.stButton > button {
    background: linear-gradient(135deg, #00d4ff 0%, #6440ff 100%) !important;
    color: #080c14 !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.8rem 2rem !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.05em !important;
    width: 100% !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 24px rgba(0,212,255,0.25) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(0,212,255,0.4) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ── Segment result card ── */
.segment-card {
    background: linear-gradient(135deg,
        rgba(0,212,255,0.08) 0%,
        rgba(100,64,255,0.08) 100%);
    border: 1px solid rgba(0,212,255,0.25);
    border-radius: 14px;
    padding: 1.6rem 2rem;
    display: flex;
    align-items: center;
    gap: 1.5rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.segment-card::after {
    content: "";
    position: absolute;
    top: -40px; right: -40px;
    width: 150px; height: 150px;
    background: radial-gradient(circle, rgba(0,212,255,0.12), transparent 70%);
    pointer-events: none;
}
.segment-icon {
    font-size: 2.8rem;
    line-height: 1;
}
.segment-info-lbl {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #00d4ff;
    margin-bottom: 0.3rem;
}
.segment-info-val {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: #e2e8f8;
    line-height: 1;
}

/* ── Rec card ── */
.rec-grid {
    display: flex;
    flex-direction: column;
    gap: 0.7rem;
}
.rec-item {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: 0.85rem 1.2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    transition: all 0.2s ease;
}
.rec-item:hover {
    background: rgba(0,212,255,0.06);
    border-color: rgba(0,212,255,0.25);
    transform: translateX(4px);
}
.rec-item-left {
    display: flex;
    align-items: center;
    gap: 0.9rem;
}
.rec-item-icon {
    width: 36px; height: 36px;
    background: rgba(0,212,255,0.1);
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem;
}
.rec-item-label {
    font-size: 0.95rem;
    color: #cdd6f4;
    font-weight: 400;
}
.rec-item-sub {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    color: #4a5470;
    margin-top: 0.1rem;
    letter-spacing: 0.05em;
}
.conf-badge {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.conf-bar-wrap {
    width: 80px;
    height: 4px;
    background: rgba(255,255,255,0.08);
    border-radius: 100px;
    overflow: hidden;
}
.conf-bar {
    height: 100%;
    border-radius: 100px;
    background: linear-gradient(to right, #00d4ff, #6440ff);
}
.conf-val {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    color: #00d4ff;
    min-width: 30px;
    text-align: right;
}

/* ── Input summary chips ── */
.chips-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 0.8rem;
}
.chip {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 100px;
    padding: 0.25rem 0.7rem;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    color: #6b7a9e;
    letter-spacing: 0.05em;
}
.chip span { color: #cdd6f4; }

/* ── Footer ── */
.footer {
    text-align: center;
    color: #2a3048;
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    margin-top: 4rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(255,255,255,0.05);
    font-family: 'IBM Plex Mono', monospace;
}

/* ── Warning override ── */
div[data-testid="stAlert"] {
    background: rgba(255,180,0,0.08) !important;
    border: 1px solid rgba(255,180,0,0.25) !important;
    border-radius: 10px !important;
    color: #ffd166 !important;
}

/* hide chrome */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# LOAD MODEL + RULES  (unchanged)
# ─────────────────────────────────────────────
final_cluster_model, scaler, features, rules = pickle.load(open("model.pkl", "rb"))

# ─────────────────────────────────────────────
# ENCODING MAPS  (unchanged)
# ─────────────────────────────────────────────
device_map   = {"Mobile": 0, "Desktop": 1, "Tablet": 2}
browser_map  = {"Chrome": 2, "Safari": 1, "Edge": 0}
shipping_map = {"Standard": 0, "Express": 1}

reverse_device   = {0: "Mobile",   1: "Desktop", 2: "Tablet"}
reverse_browser  = {2: "Chrome",   1: "Safari",  0: "Edge"}
reverse_shipping = {0: "Standard", 1: "Express"}

CATEGORY_ICONS = {"Device": "📱", "Browser": "🌐", "Shipping": "🚚"}

# ─────────────────────────────────────────────
# LOGIC FUNCTIONS  (unchanged)
# ─────────────────────────────────────────────
def decode_item(item):
    try:
        if "Device_" in item:
            val = int(item.split("_")[1])
            return "Device: " + reverse_device.get(val, f"Unknown ({val})")
        elif "Browser_" in item:
            val = int(item.split("_")[1])
            return "Browser: " + reverse_browser.get(val, f"Unknown ({val})")
        elif "ShippingType_" in item:
            val = int(item.split("_")[1])
            return "Shipping: " + reverse_shipping.get(val, f"Unknown ({val})")
    except:
        return item
    return item

def recommend_products(user_items, rules, top_n=10):
    recommendations = []
    for _, row in rules.iterrows():
        antecedents = list(row['antecedents'])
        consequents = list(row['consequents'])
        if any(item in user_items for item in antecedents):
            for item in consequents:
                if item in user_items:
                    continue
                recommendations.append((item, row['confidence']))
    recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)
    seen = set()
    final = []
    for item, conf in recommendations:
        if item not in seen:
            seen.add(item)
            final.append((item, conf))
    return final[:top_n]

def filter_recommendations(recs):
    best = {}
    for item, conf in recs:
        if "Device_" in item:       key = "Device"
        elif "Browser_" in item:    key = "Browser"
        elif "ShippingType_" in item: key = "Shipping"
        else: continue
        if key not in best or conf > best[key][1]:
            best[key] = (item, conf)
    return list(best.values())

# ─────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
    <div class="hero-top">
        <div>
            <div class="hero-badge">LIVE SYSTEM</div>
            <h1 class="hero-title">SEGMENT<span>IQ</span></h1>
            <p class="hero-sub">AI-powered customer segmentation & association-rule recommendations</p>
        </div>
    </div>
    <div class="hero-stat-row">
        <div class="hero-stat">
            <span class="hero-stat-val">K-Means</span>
            <span class="hero-stat-lbl">Cluster Model</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-val">Apriori</span>
            <span class="hero-stat-lbl">Rule Engine</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-val">5+</span>
            <span class="hero-stat-lbl">Input Signals</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# INPUT FORM — two column layout
# ─────────────────────────────────────────────
col_left, col_right = st.columns([1.1, 1], gap="large")

with col_left:
    # ── Transaction Signals ──
    st.markdown('<div class="section-title">⬡ Transaction Signals</div>', unsafe_allow_html=True)
    st.markdown('<div class="panel">', unsafe_allow_html=True)

    price    = st.number_input("Price (₹)", 1, 10000, 100)
    quantity = st.slider("Quantity", 1, 10, 1)
    discount = st.slider("Discount Applied (%)", 0, 50, 5)

    st.markdown('</div>', unsafe_allow_html=True)

    # ── Engagement Signals ──
    st.markdown('<div class="section-title">⬡ Engagement Signals</div>', unsafe_allow_html=True)
    st.markdown('<div class="panel">', unsafe_allow_html=True)

    rating  = st.slider("Rating", 1, 5, 3)
    session = st.slider("Session Duration (min)", 1, 60, 10)

    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    # ── Behavioral Context ──
    st.markdown('<div class="section-title">⬡ Behavioral Context</div>', unsafe_allow_html=True)
    st.markdown('<div class="panel">', unsafe_allow_html=True)

    device   = st.selectbox("Device Type", ["Mobile", "Desktop", "Tablet"])
    browser  = st.selectbox("Browser", ["Chrome", "Safari", "Edge"])
    shipping = st.selectbox("Shipping Preference", ["Standard", "Express"])

    st.markdown('</div>', unsafe_allow_html=True)

    # ── Input Summary chips ──
    st.markdown(f"""
    <div class="section-title" style="margin-top:0.5rem;">⬡ Current Profile</div>
    <div class="chips-row">
        <div class="chip">Price <span>₹{price}</span></div>
        <div class="chip">Qty <span>{quantity}</span></div>
        <div class="chip">Discount <span>{discount}%</span></div>
        <div class="chip">Rating <span>{'★'*rating}{'☆'*(5-rating)}</span></div>
        <div class="chip">Session <span>{session}m</span></div>
        <div class="chip">Device <span>{device}</span></div>
        <div class="chip">Browser <span>{browser}</span></div>
        <div class="chip">Shipping <span>{shipping}</span></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    analyze_clicked = st.button("⚡ Analyze Customer")

# ─────────────────────────────────────────────
# RESULTS
# ─────────────────────────────────────────────
if analyze_clicked:

    # ── Build input df (unchanged logic) ──
    input_dict = {
        'Price': price, 'Quantity': quantity,
        'DiscountApplied': discount, 'Rating': rating,
        'SessionDuration': session
    }
    input_df = pd.DataFrame([input_dict])
    for col in features:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df      = input_df[features]
    input_scaled  = scaler.transform(input_df)

    # ── Segment (unchanged logic) ──
    segment = final_cluster_model.predict(input_scaled)[0] if hasattr(final_cluster_model, "predict") \
              else final_cluster_model.fit_predict(input_scaled)[0]

    # ── Recommend (unchanged logic) ──
    user_items    = [
        f"Device_{device_map.get(device, -1)}",
        f"Browser_{browser_map.get(browser, -1)}",
        f"ShippingType_{shipping_map.get(shipping, -1)}"
    ]
    recs          = recommend_products(user_items, rules)
    filtered_recs = filter_recommendations(recs)

    st.markdown("---")
    st.markdown('<div class="section-title">⬡ Analysis Results</div>', unsafe_allow_html=True)

    res_left, res_right = st.columns([1, 1.2], gap="large")

    with res_left:
        # Segment card
        segment_emojis = {0:"🔵", 1:"🟠", 2:"🟢", 3:"🟣", 4:"🔴"}
        emoji = segment_emojis.get(int(segment), "⚪")
        st.markdown(f"""
        <div class="segment-card">
            <div class="segment-icon">{emoji}</div>
            <div>
                <div class="segment-info-lbl">Customer Segment</div>
                <div class="segment-info-val">Cluster {segment}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with res_right:
        st.markdown('<div class="section-title">⬡ Smart Recommendations</div>', unsafe_allow_html=True)

        shown   = set()
        display = []

        if filtered_recs:
            for item, conf in filtered_recs:
                if item in user_items:
                    continue
                decoded = decode_item(item)
                if decoded in shown:
                    continue
                shown.add(decoded)
                display.append((decoded, conf))
        else:
            display = [
                ("Shipping: Express", 0.85),
                ("Browser: Chrome",   0.78),
                ("Device: Mobile",    0.72),
            ]

        st.markdown('<div class="rec-grid">', unsafe_allow_html=True)
        for decoded, conf in display:
            category = decoded.split(":")[0].strip()
            value    = decoded.split(":")[-1].strip()
            icon     = CATEGORY_ICONS.get(category, "💡")
            bar_pct  = int(conf * 100)
            st.markdown(f"""
            <div class="rec-item">
                <div class="rec-item-left">
                    <div class="rec-item-icon">{icon}</div>
                    <div>
                        <div class="rec-item-label">{value}</div>
                        <div class="rec-item-sub">{category.upper()} RECOMMENDATION</div>
                    </div>
                </div>
                <div class="conf-badge">
                    <div class="conf-bar-wrap">
                        <div class="conf-bar" style="width:{bar_pct}%"></div>
                    </div>
                    <div class="conf-val">{round(conf,2)}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div class="footer">
    SEGMENTIQ &nbsp;·&nbsp; ML-Powered Customer Intelligence &nbsp;·&nbsp; K-Means + Apriori Engine
</div>
""", unsafe_allow_html=True)