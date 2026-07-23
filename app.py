from typing import Optional

import requests
import streamlit as st

# =============================
# CONFIG
# =============================
API_BASE = "https://movies-rec-832v.onrender.com/" or "http://127.0.0.1:8000"
TMDB_IMG = "https://image.tmdb.org/t/p/w500"

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

# =============================
# STYLES (premium dark cinematic theme)
# =============================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

:root {
    --accent: #1C39BB;
    --accent-light: #3D5AFE;
    --bg: #0B1120;
    --sidebar-bg: #111827;
    --card-bg: #172554;
    --text-white: #F8FAFC;
    --text-muted: #94A3B8;
}

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background: radial-gradient(circle at 15% 0%, rgba(28,57,187,0.18), transparent 45%),
                radial-gradient(circle at 85% 10%, rgba(61,90,255,0.12), transparent 40%),
                var(--bg);
    color: var(--text-white);
}

.block-container {
    padding-top: 1.2rem;
    padding-bottom: 3rem;
    max-width: 1440px;
}

/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, var(--sidebar-bg) 0%, #0D1424 100%);
    border-right: 1px solid rgba(148,163,184,0.08);
}
section[data-testid="stSidebar"] .stMarkdown h2,
section[data-testid="stSidebar"] .stMarkdown h3 {
    color: var(--text-white);
    letter-spacing: 0.02em;
}
section[data-testid="stSidebar"] hr {
    border-color: rgba(148,163,184,0.15);
}

/* ---------- Typography ---------- */
h1, h2, h3, h4, h5 {
    color: var(--text-white);
    font-weight: 800;
    letter-spacing: -0.02em;
}
p, span, label, div {
    color: var(--text-white);
}
.small-muted {
    color: var(--text-muted) !important;
    font-size: 0.92rem;
    font-weight: 500;
}

/* ---------- Hero ---------- */
.hero-wrap {
    position: relative;
    padding: 56px 40px;
    border-radius: 28px;
    margin-bottom: 28px;
    background: linear-gradient(135deg, rgba(28,57,187,0.35) 0%, rgba(23,37,84,0.55) 55%, rgba(11,17,32,0.9) 100%);
    border: 1px solid rgba(61,90,255,0.25);
    box-shadow: 0 30px 60px -20px rgba(28,57,187,0.35), inset 0 1px 0 rgba(255,255,255,0.04);
    overflow: hidden;
}
.hero-wrap::before {
    content: "";
    position: absolute;
    top: -40%;
    right: -10%;
    width: 60%;
    height: 180%;
    background: radial-gradient(circle, rgba(61,90,255,0.25) 0%, transparent 70%);
    pointer-events: none;
}
.hero-eyebrow {
    display: inline-block;
    color: #A5B4FC;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    padding: 6px 14px;
    border-radius: 999px;
    background: rgba(61,90,255,0.15);
    border: 1px solid rgba(61,90,255,0.35);
    margin-bottom: 18px;
}
.hero-title {
    font-size: 3.4rem;
    font-weight: 900;
    line-height: 1.05;
    margin: 0 0 14px 0;
    background: linear-gradient(90deg, #FFFFFF 0%, #C7D2FE 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    color: var(--text-muted);
    font-size: 1.15rem;
    font-weight: 400;
    max-width: 620px;
    margin: 0;
}

/* ---------- Section dividers ---------- */
.section-divider {
    height: 1px;
    width: 100%;
    margin: 30px 0;
    background: linear-gradient(90deg, rgba(61,90,255,0.5), rgba(148,163,184,0.08), transparent);
    border: none;
}
.section-heading {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 1.35rem;
    font-weight: 800;
    color: var(--text-white);
    margin: 6px 0 18px 0;
}
.section-heading .bar {
    width: 5px;
    height: 22px;
    border-radius: 3px;
    background: linear-gradient(180deg, var(--accent-light), var(--accent));
    display: inline-block;
}

/* ---------- Search bar ---------- */
div[data-testid="stTextInput"] input {
    background: rgba(23,37,84,0.55) !important;
    border: 1.5px solid rgba(61,90,255,0.3) !important;
    border-radius: 16px !important;
    color: var(--text-white) !important;
    padding: 14px 18px !important;
    font-size: 1.02rem !important;
    box-shadow: 0 8px 24px -12px rgba(0,0,0,0.5);
    transition: all 0.25s ease;
}
div[data-testid="stTextInput"] input:focus {
    border-color: var(--accent-light) !important;
    box-shadow: 0 0 0 3px rgba(61,90,255,0.25), 0 8px 24px -12px rgba(0,0,0,0.6) !important;
}
div[data-testid="stTextInput"] input::placeholder {
    color: #64748B !important;
}
div[data-testid="stTextInput"] label {
    color: var(--text-muted) !important;
    font-weight: 600;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* ---------- Selectbox ---------- */
div[data-testid="stSelectbox"] > div > div {
    background: rgba(23,37,84,0.55) !important;
    border: 1.5px solid rgba(61,90,255,0.25) !important;
    border-radius: 14px !important;
    color: var(--text-white) !important;
}
div[data-testid="stSelectbox"] label {
    color: var(--text-muted) !important;
    font-weight: 600;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* ---------- Slider ---------- */
div[data-testid="stSlider"] label {
    color: var(--text-muted) !important;
    font-weight: 600;
}

/* ---------- Buttons (gradient, rounded, smooth) ---------- */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, var(--accent-light) 0%, var(--accent) 100%);
    color: #FFFFFF !important;
    border: none;
    border-radius: 12px;
    padding: 9px 16px;
    font-weight: 700;
    font-size: 0.88rem;
    letter-spacing: 0.01em;
    box-shadow: 0 6px 16px -6px rgba(28,57,187,0.6);
    transition: transform 0.18s ease, box-shadow 0.18s ease, filter 0.18s ease;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 22px -6px rgba(61,90,255,0.7);
    filter: brightness(1.08);
}
.stButton > button:active {
    transform: translateY(0px);
}

/* ---------- Movie cards (glassmorphism) ---------- */
.card {
    border: 1px solid rgba(148,163,184,0.12);
    border-radius: 18px;
    padding: 14px;
    background: linear-gradient(180deg, rgba(23,37,84,0.65) 0%, rgba(17,24,39,0.65) 100%);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    box-shadow: 0 10px 30px -14px rgba(0,0,0,0.6);
}
.poster-card {
    border: 1px solid rgba(148,163,184,0.12);
    border-radius: 16px;
    padding: 10px;
    background: linear-gradient(180deg, rgba(23,37,84,0.55) 0%, rgba(17,24,39,0.55) 100%);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    box-shadow: 0 8px 20px -12px rgba(0,0,0,0.55);
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    margin-bottom: 14px;
}
.poster-card:hover {
    transform: translateY(-6px) scale(1.015);
    box-shadow: 0 20px 40px -16px rgba(28,57,187,0.55);
    border-color: rgba(61,90,255,0.4);
}

div[data-testid="stImage"] img {
    border-radius: 12px;
    transition: transform 0.35s ease, filter 0.35s ease;
}
div[data-testid="stImage"]:hover img {
    transform: scale(1.035);
    filter: brightness(1.05);
}

.movie-title {
    font-size: 0.92rem;
    font-weight: 600;
    line-height: 1.2rem;
    height: 2.4rem;
    overflow: hidden;
    color: var(--text-white);
    margin-top: 8px;
}

/* ---------- Badges ---------- */
.badge {
    display: inline-block;
    padding: 5px 12px;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 700;
    margin: 3px 6px 3px 0;
}
.badge-genre {
    background: rgba(61,90,255,0.16);
    color: #A5B4FC;
    border: 1px solid rgba(61,90,255,0.35);
}
.badge-rating {
    background: linear-gradient(135deg, #F59E0B, #D97706);
    color: #1a1200;
}

/* ---------- Info / warning / error boxes ---------- */
div[data-testid="stAlert"] {
    border-radius: 14px;
    border: 1px solid rgba(148,163,184,0.15);
    background: rgba(23,37,84,0.4);
    backdrop-filter: blur(8px);
}

/* ---------- Spinner ---------- */
div[data-testid="stSpinner"] > div {
    border-top-color: var(--accent-light) !important;
}

/* ---------- Detail page hero card ---------- */
.detail-card {
    border-radius: 22px;
    border: 1px solid rgba(148,163,184,0.12);
    background: linear-gradient(180deg, rgba(23,37,84,0.6) 0%, rgba(17,24,39,0.6) 100%);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    padding: 26px;
    box-shadow: 0 20px 50px -20px rgba(0,0,0,0.65);
}
.detail-card img {
    border-radius: 16px;
}

hr {
    border-color: rgba(148,163,184,0.15);
}
</style>
""",
    unsafe_allow_html=True,
)

# =============================
# STATE + ROUTING (single-file pages)
# =============================
if "view" not in st.session_state:
    st.session_state.view = "home"  # home | details
if "selected_tmdb_id" not in st.session_state:
    st.session_state.selected_tmdb_id = None

qp_view = st.query_params.get("view")
qp_id = st.query_params.get("id")
if qp_view in ("home", "details"):
    st.session_state.view = qp_view
if qp_id:
    try:
        st.session_state.selected_tmdb_id = int(qp_id)
        st.session_state.view = "details"
    except:
        pass


def goto_home():
    st.session_state.view = "home"
    st.query_params["view"] = "home"
    if "id" in st.query_params:
        del st.query_params["id"]
    st.rerun()


def goto_details(tmdb_id: int):
    st.session_state.view = "details"
    st.session_state.selected_tmdb_id = int(tmdb_id)
    st.query_params["view"] = "details"
    st.query_params["id"] = str(int(tmdb_id))
    st.rerun()


# =============================
# API HELPERS
# =============================
@st.cache_data(ttl=30)  # short cache for autocompletefrom typing import Dict, Optional
def api_get_json(path: str, params: dict | None = None):
    try:
        r = requests.get(f"{API_BASE}{path}", params=params, timeout=25)
        if r.status_code >= 400:
            return None, f"HTTP {r.status_code}: {r.text[:300]}"
        return r.json(), None
    except Exception as e:
        return None, f"Request failed: {e}"


def poster_grid(cards, cols=6, key_prefix="grid"):
    if not cards:
        st.info("No movies to show.")
        return

    rows = (len(cards) + cols - 1) // cols
    idx = 0
    for r in range(rows):
        colset = st.columns(cols)
        for c in range(cols):
            if idx >= len(cards):
                break
            m = cards[idx]
            idx += 1

            tmdb_id = m.get("tmdb_id")
            title = m.get("title", "Untitled")
            poster = m.get("poster_url")

            with colset[c]:
                st.markdown("<div class='poster-card'>", unsafe_allow_html=True)
                if poster:
                    st.image(poster, use_column_width=True)
                else:
                    st.write("🖼️ No poster")

                if st.button("▶ Open", key=f"{key_prefix}_{r}_{c}_{idx}_{tmdb_id}"):
                    if tmdb_id:
                        goto_details(tmdb_id)

                st.markdown(
                    f"<div class='movie-title'>{title}</div>", unsafe_allow_html=True
                )
                st.markdown("</div>", unsafe_allow_html=True)


def to_cards_from_tfidf_items(tfidf_items):
    cards = []
    for x in tfidf_items or []:
        tmdb = x.get("tmdb") or {}
        if tmdb.get("tmdb_id"):
            cards.append(
                {
                    "tmdb_id": tmdb["tmdb_id"],
                    "title": tmdb.get("title") or x.get("title") or "Untitled",
                    "poster_url": tmdb.get("poster_url"),
                }
            )
    return cards


# =============================
# IMPORTANT: Robust TMDB search parsing
# Supports BOTH API shapes:
# 1) raw TMDB: {"results":[{id,title,poster_path,...}]}
# 2) list cards: [{tmdb_id,title,poster_url,...}]
# =============================
def parse_tmdb_search_to_cards(data, keyword: str, limit: int = 24):
    """
    Returns:
      suggestions: list[(label, tmdb_id)]
      cards: list[{tmdb_id,title,poster_url}]
    """
    keyword_l = keyword.strip().lower()

    # A) If API returns dict with 'results'
    if isinstance(data, dict) and "results" in data:
        raw = data.get("results") or []
        raw_items = []
        for m in raw:
            title = (m.get("title") or "").strip()
            tmdb_id = m.get("id")
            poster_path = m.get("poster_path")
            if not title or not tmdb_id:
                continue
            raw_items.append(
                {
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": f"{TMDB_IMG}{poster_path}" if poster_path else None,
                    "release_date": m.get("release_date", ""),
                }
            )

    # B) If API returns already as list
    elif isinstance(data, list):
        raw_items = []
        for m in data:
            # might be {tmdb_id,title,poster_url}
            tmdb_id = m.get("tmdb_id") or m.get("id")
            title = (m.get("title") or "").strip()
            poster_url = m.get("poster_url")
            if not title or not tmdb_id:
                continue
            raw_items.append(
                {
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": poster_url,
                    "release_date": m.get("release_date", ""),
                }
            )
    else:
        return [], []

    # Word-match filtering (contains)
    matched = [x for x in raw_items if keyword_l in x["title"].lower()]

    # If nothing matched, fallback to raw list (so never blank)
    final_list = matched if matched else raw_items

    # Suggestions = top 10 labels
    suggestions = []
    for x in final_list[:10]:
        year = (x.get("release_date") or "")[:4]
        label = f"{x['title']} ({year})" if year else x["title"]
        suggestions.append((label, x["tmdb_id"]))

    # Cards = top N
    cards = [
        {"tmdb_id": x["tmdb_id"], "title": x["title"], "poster_url": x["poster_url"]}
        for x in final_list[:limit]
    ]
    return suggestions, cards


# =============================
# SIDEBAR (clean)
# =============================
with st.sidebar:
    st.markdown("## 🎬 Menu")
    if st.button("🏠 Home"):
        goto_home()

    st.markdown("---")
    st.markdown("### 🏠 Home Feed (only home)")
    home_category = st.selectbox(
        "Category",
        ["trending", "popular", "top_rated", "now_playing", "upcoming"],
        index=0,
    )
    grid_cols = st.slider("Grid columns", 4, 8, 6)

# =============================
# HEADER
# =============================
st.markdown(
    """
<div class="hero-wrap">
    <span class="hero-eyebrow">AI-Powered Recommendations</span>
    <h1 class="hero-title">🎬 CineVerse</h1>
    <p class="hero-sub">Discover your next obsession with AI-powered recommendations.</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='small-muted'>Type keyword → dropdown suggestions + matching results → open → details + recommendations</div>",
    unsafe_allow_html=True,
)
st.markdown("<hr class='section-divider' />", unsafe_allow_html=True)

# ==========================================================
# VIEW: HOME
# ==========================================================
if st.session_state.view == "home":
    typed = st.text_input(
        "Search by movie title (keyword)", placeholder="Type: avenger, batman, love..."
    )

    st.markdown("<hr class='section-divider' />", unsafe_allow_html=True)

    # SEARCH MODE (Autocomplete + word-match results)
    if typed.strip():
        if len(typed.strip()) < 2:
            st.caption("Type at least 2 characters for suggestions.")
        else:
            data, err = api_get_json("/tmdb/search", params={"query": typed.strip()})

            if err or data is None:
                st.error(f"Search failed: {err}")
            else:
                suggestions, cards = parse_tmdb_search_to_cards(
                    data, typed.strip(), limit=24
                )

                # Dropdown
                if suggestions:
                    labels = ["-- Select a movie --"] + [s[0] for s in suggestions]
                    selected = st.selectbox("Suggestions", labels, index=0)

                    if selected != "-- Select a movie --":
                        # map label -> id
                        label_to_id = {s[0]: s[1] for s in suggestions}
                        goto_details(label_to_id[selected])
                else:
                    st.info("No suggestions found. Try another keyword.")

                st.markdown(
                    "<div class='section-heading'><span class='bar'></span>Results</div>",
                    unsafe_allow_html=True,
                )
                poster_grid(cards, cols=grid_cols, key_prefix="search_results")

        st.stop()

    # HOME FEED MODE
    st.markdown(
        f"<div class='section-heading'><span class='bar'></span>🏠 Home — {home_category.replace('_',' ').title()}</div>",
        unsafe_allow_html=True,
    )

    home_cards, err = api_get_json(
        "/home", params={"category": home_category, "limit": 24}
    )
    if err or not home_cards:
        st.error(f"Home feed failed: {err or 'Unknown error'}")
        st.stop()

    poster_grid(home_cards, cols=grid_cols, key_prefix="home_feed")

# ==========================================================
# VIEW: DETAILS
# ==========================================================
elif st.session_state.view == "details":
    tmdb_id = st.session_state.selected_tmdb_id
    if not tmdb_id:
        st.warning("No movie selected.")
        if st.button("← Back to Home"):
            goto_home()
        st.stop()

    # Top bar
    a, b = st.columns([3, 1])
    with a:
        st.markdown(
            "<div class='section-heading'><span class='bar'></span>📄 Movie Details</div>",
            unsafe_allow_html=True,
        )
    with b:
        if st.button("← Back to Home"):
            goto_home()

    # Details (your FastAPI safe route)
    data, err = api_get_json(f"/movie/id/{tmdb_id}")
    if err or not data:
        st.error(f"Could not load details: {err or 'Unknown error'}")
        st.stop()

    # Layout: Poster LEFT, Details RIGHT
    left, right = st.columns([1, 2.4], gap="large")

    with left:
        st.markdown("<div class='detail-card'>", unsafe_allow_html=True)
        if data.get("poster_url"):
            st.image(data["poster_url"], use_column_width=True)
        else:
            st.write("🖼️ No poster")
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown("<div class='detail-card'>", unsafe_allow_html=True)
        st.markdown(f"## {data.get('title','')}")
        release = data.get("release_date") or "-"
        genres = [g["name"] for g in data.get("genres", [])]
        rating = data.get("vote_average")

        st.markdown(
            f"<div class='small-muted'>Release: {release}</div>", unsafe_allow_html=True
        )

        badges_html = ""
        if rating:
            badges_html += f"<span class='badge badge-rating'>⭐ {rating}</span>"
        for g in genres:
            badges_html += f"<span class='badge badge-genre'>{g}</span>"
        if badges_html:
            st.markdown(f"<div style='margin-top:10px'>{badges_html}</div>", unsafe_allow_html=True)
        elif genres == [] and not rating:
            st.markdown("<div class='small-muted'>Genres: -</div>", unsafe_allow_html=True)

        st.markdown("<hr class='section-divider' />", unsafe_allow_html=True)
        st.markdown("### Overview")
        st.write(data.get("overview") or "No overview available.")
        st.markdown("</div>", unsafe_allow_html=True)

    if data.get("backdrop_url"):
        st.markdown(
            "<div class='section-heading' style='margin-top:24px'><span class='bar'></span>Backdrop</div>",
            unsafe_allow_html=True,
        )
        st.image(data["backdrop_url"], use_column_width=True)

    st.markdown("<hr class='section-divider' />", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-heading'><span class='bar'></span>✅ Recommendations</div>",
        unsafe_allow_html=True,
    )

    # Recommendations (TF-IDF + Genre) via your bundle endpoint
    title = (data.get("title") or "").strip()
    if title:
        bundle, err2 = api_get_json(
            "/movie/search",
            params={"query": title, "tfidf_top_n": 12, "genre_limit": 12},
        )

        if not err2 and bundle:
            st.markdown(
                "<div class='section-heading' style='font-size:1.1rem'><span class='bar'></span>🔎 Similar Movies (TF-IDF)</div>",
                unsafe_allow_html=True,
            )
            poster_grid(
                to_cards_from_tfidf_items(bundle.get("tfidf_recommendations")),
                cols=grid_cols,
                key_prefix="details_tfidf",
            )

            st.markdown(
                "<div class='section-heading' style='font-size:1.1rem'><span class='bar'></span>🎭 More Like This (Genre)</div>",
                unsafe_allow_html=True,
            )
            poster_grid(
                bundle.get("genre_recommendations", []),
                cols=grid_cols,
                key_prefix="details_genre",
            )
        else:
            st.info("Showing Genre recommendations (fallback).")
            genre_only, err3 = api_get_json(
                "/recommend/genre", params={"tmdb_id": tmdb_id, "limit": 18}
            )
            if not err3 and genre_only:
                poster_grid(
                    genre_only, cols=grid_cols, key_prefix="details_genre_fallback"
                )
            else:
                st.warning("No recommendations available right now.")
    else:
        st.warning("No title available to compute recommendations.")