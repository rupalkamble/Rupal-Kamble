import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Rupal Kamble", page_icon="🌸", layout="wide")

# Remove Streamlit's default padding/header so the page fills the screen
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {border: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "images"

# Placeholder name -> file name inside the images/ folder
IMAGES = {
    "IMG_BEACH": "beach.jpg",
    "IMG_MIRROR": "mirror.jpg",
    "IMG_CELEBRATION": "celebration.jpg",
    "IMG_SAFARI": "safari.jpg",
}

MIME = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}


def image_to_data_uri(filename: str) -> str:
    """Embed the image as base64 so it loads inside Streamlit's HTML iframe."""
    path = IMAGE_DIR / filename
    if not path.exists():
        # Try other common extensions with the same name
        for ext in MIME:
            alt = path.with_suffix(ext)
            if alt.exists():
                path = alt
                break
        else:
            # Neutral grey placeholder if the photo is missing
            svg = (
                "<svg xmlns='http://www.w3.org/2000/svg' width='600' height='800'>"
                "<rect width='100%' height='100%' fill='#e5e7eb'/>"
                "<text x='50%' y='50%' text-anchor='middle' fill='#6b7280' "
                "font-family='sans-serif' font-size='28'>Photo missing</text></svg>"
            )
            return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()
    mime = MIME.get(path.suffix.lower(), "image/jpeg")
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,500;9..144,600&display=swap" rel="stylesheet">
  <style>
    :root { --ink:#304a3b; --coral:#ef786b; --leaf:#678d68; }
    * { box-sizing:border-box; }
    html { scroll-behavior:smooth; }
    body { margin:0; width:100%; font-family:"DM Sans",sans-serif; color:var(--ink); background:#fff8ed; }
    .site-wrap { width:100%; overflow:hidden; }
    .page-inner { width:100%; max-width:1200px; margin-inline:auto; padding-inline:clamp(20px,5vw,68px); }
    .display { font-family:"Fraunces",serif; font-weight:600; letter-spacing:-.035em; line-height:1.13; }
    .intro { position:relative; overflow:hidden; }
    .intro::before, .intro::after { content:""; position:absolute; border-radius:50%; pointer-events:none; }
    .intro::before { width:340px; height:340px; background:#ffe5a9; left:-155px; top:-130px; opacity:.58; }
    .intro::after { width:280px; height:280px; background:#d5eee0; right:-120px; bottom:-140px; opacity:.8; }
    .floral { position:absolute; font-size:clamp(38px,6vw,78px); opacity:.5; pointer-events:none; line-height:1; }
    .floral-one { right:8%; top:12%; color:#e98e82; transform:rotate(-18deg); }
    .floral-two { left:5%; bottom:9%; color:#78a787; transform:rotate(18deg); }
    .intro-card { position:relative; z-index:1; box-shadow:0 22px 70px rgba(90,91,62,.09); }
    .gallery-card { overflow:hidden; box-shadow:0 12px 34px rgba(48,74,59,.11); transition:transform .25s ease,box-shadow .25s ease; }
    .gallery-card:hover { transform:translateY(-5px); box-shadow:0 20px 42px rgba(48,74,59,.16); }
    .gallery-card img { display:block; width:100%; height:auto; }
    .contact-link { overflow-wrap:anywhere; text-decoration-thickness:2px; text-underline-offset:5px; }
    .contact-link:hover { color:#a6383b; }
    a:focus-visible { outline:3px solid #ad4152; outline-offset:5px; border-radius:5px; }
    @media (prefers-reduced-motion:reduce) {
      html { scroll-behavior:auto; }
      .gallery-card { transition:none; }
    }
  </style>
  <script src="https://cdn.tailwindcss.com/3.4.17"></script>
</head>
<body class="w-full">
  <div class="site-wrap">
    <main>
      <section class="intro py-20 sm:py-24 lg:py-28" style="background:#fff2e8;">
        <span class="floral floral-one" aria-hidden="true">✿</span>
        <span class="floral floral-two" aria-hidden="true">✽</span>
        <div class="page-inner">
          <div class="intro-card mx-auto max-w-3xl rounded-[36px] p-7 sm:p-12 lg:p-16" style="background:#fff;">
            <p class="mb-3 font-bold uppercase tracking-[.18em]" style="color:#b34c56; font-size:13px;">About Me</p>
            <h1 class="display mb-8" style="color:#304a3b; font-size:32px;">Name: Rupal Kamble</h1>
            <div class="grid gap-3 sm:grid-cols-2">
              <p class="rounded-2xl bg-[#fff1da] px-5 py-4 font-semibold" style="color:#304a3b; font-size:16px;">Date of birth: 17 January 2004</p>
              <p class="rounded-2xl bg-[#e7f3e9] px-5 py-4 font-semibold" style="color:#304a3b; font-size:16px;">Age: 22</p>
            </div>
            <p class="mt-8 max-w-2xl leading-relaxed" style="color:#3c5948; font-size:20px; line-height:1.6;">Major Interests: Good food (Vegetarian), Flowers, Jungle Safaris, Exploring Cultures and Watching Movies.
            Currently Aiming Higher & Trying Out Things. On The Path to Liberation.</p>
          </div>
        </div>
      </section>

      <section class="py-16 sm:py-20" style="background:#f0f7ed;">
        <div class="page-inner">
          <h2 class="display mb-9" style="color:#304a3b; font-size:24px;">Photos</h2>
          <div class="grid items-start gap-5 sm:grid-cols-2 lg:grid-cols-4">
            <figure class="gallery-card m-0 rounded-[26px] p-2" style="background:#fff;">
              <img class="rounded-[19px]" src="IMG_BEACH" alt="Rupal sitting beside the sea beneath a wide blue sky, with a tree nearby.">
            </figure>
            <figure class="gallery-card m-0 rounded-[26px] p-2" style="background:#fff;">
              <img class="rounded-[19px]" src="IMG_MIRROR" alt="Rupal taking a mirror selfie indoors, wearing a black top and red trousers.">
            </figure>
            <figure class="gallery-card m-0 rounded-[26px] p-2" style="background:#fff;">
              <img class="rounded-[19px]" src="IMG_CELEBRATION" alt="Rupal standing indoors in an orange and red traditional outfit.">
            </figure>
            <figure class="gallery-card m-0 rounded-[26px] p-2" style="background:#fff;">
              <img class="rounded-[19px]" src="IMG_SAFARI" alt="Rupal standing beside a safari vehicle near a wooded entrance on a sunny day.">
            </figure>
          </div>
        </div>
      </section>

      <section class="py-16 sm:py-20" style="background:#ffe8db;">
        <div class="page-inner">
          <div class="rounded-[34px] p-8 sm:p-12" style="background:#fff;">
            <h2 class="display mb-8" style="color:#304a3b; font-size:24px;">Contact</h2>
            <div class="grid gap-7 sm:grid-cols-2">
              <div>
                <p class="mb-2 font-bold" style="color:#6c6257; font-size:16px;">Mobile</p>
                <a class="contact-link font-semibold underline" href="tel:8459020588" style="color:#304a3b; font-size:20px;">8459020588</a>
              </div>
              <div>
                <p class="mb-2 font-bold" style="color:#6c6257; font-size:16px;">Instagram</p>
                <a class="contact-link font-semibold underline" href="https://www.instagram.com/rupal_kamble_/" target="_blank" rel="noopener noreferrer" style="color:#304a3b; font-size:20px;">rupal_kamble_</a>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</body>
</html>
"""

# Inject the images (plain string replace, so CSS braces are safe)
for placeholder, filename in IMAGES.items():
    HTML = HTML.replace(f'src="{placeholder}"', f'src="{image_to_data_uri(filename)}"')

components.html(HTML, height=2600, scrolling=True)
