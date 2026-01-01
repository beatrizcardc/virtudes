import base64
import random
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Retiro 2026 • Vistudes", page_icon="🃏", layout="centered")

# -----------------------------
# Dados (extraídos do seu script.js original)
# -----------------------------
CARDS = [
    {
        "id": 1,
        "img": "virtudes/foto1.png",
        "text": "Fluir en el proceso.",
    },
    {
        "id": 2,
        "img": "virtudes/foto2.png",
        "text": "Fluir en la vida misma.",
    },
    {
        "id": 3,
        "img": "virtudes/foto3.png",
        "text": "Fluir hacia la conexión.",
    },
    {
        "id": 4,
        "img": "virtudes/foto4.png",
        "text": "Fluir en la renuncia integral.",
    },
    {
        "id": 5,
        "img": "virtudes/foto5.png",
        "text": "Fluir en la instrospección",
    },
    {
        "id": 6,
        "img": "virtudes/foto6.png",
        "text": "Fluir en la atención.",
    },
    {
        "id": 7,
        "img": "virtudes/foto7.png",
        "text": "Fluir en Egoencia.",
    },
    {
        "id": 8,
        "img": "virtudes/foto8.png",
        "text": "Fluir en Presencia.",
    },
    {
        "id": 9,
        "img": "virtudes/foto9.png",
        "text": "Fluir en la unidad.",
    },
    {
        "id": 10,
        "img": "virtudes/foto10.png",
        "text": "Fluir en Transcendencia.",
    },
    {
        "id": 11,
        "img": "virtudes/foto11.png",
        "text": "Fluir con amor.",
    },
]

ASSETS_DIR = Path(__file__).parent / "virtudes"

HOME_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Retiro 2026</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="home">
        <header class="home-header">
            <h1>Retiro 2026</h1>
            <p>Retiro 2026</p>
        </header>

        <main class="home-main">
            <div class="home-card">
                <h2>Cómo jugar</h2>
                <p>Hacé clic en una carta para descubrir su mensaje. Cada carta se usa una sola vez.</p>
                <p>Cuando termines, verás el mensaje final.</p>
            </div>

            <div class="home-actions">
                <a class="btn" href="index.html">Ir al juego</a>
                <a class="btn secondary" href="deploy.html">Deploy / Ayuda</a>
            </div>
        </main>

        <footer class="home-footer">
            <small>© Retiro 2026</small>
        </footer>
    </div>
</body>
</html>
"""

DEPLOY_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deploy / Ayuda</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="deploy">
        <header class="deploy-header">
            <h1>Deploy / Ayuda</h1>
            <p>Guía rápida para publicar el proyecto.</p>
        </header>

        <main class="deploy-main">
            <div class="deploy-card">
                <h2>Requisitos</h2>
                <ul>
                    <li>GitHub (repositorio)</li>
                    <li>Streamlit Community Cloud</li>
                </ul>
            </div>

            <div class="deploy-card">
                <h2>Pasos</h2>
                <ol>
                    <li>Subí los archivos al repositorio</li>
                    <li>En Streamlit Cloud, conectá el repo</li>
                    <li>Elegí <b>app.py</b> como archivo principal</li>
                </ol>
            </div>

            <div class="deploy-actions">
                <a class="btn" href="index.html">Volver al juego</a>
                <a class="btn secondary" href="home.html">Home</a>
            </div>
        </main>

        <footer class="deploy-footer">
            <small>© Retiro 2026</small>
        </footer>
    </div>
</body>
</html>
"""

# -----------------------------
# CSS (baseado no seu style.css original, com ajustes para Streamlit)
# -----------------------------
BASE_CSS = r"""
/* ===============================
   style.css (original do projeto)
   =============================== */

@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700;800&display=swap");

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: "Montserrat", sans-serif;
  background: linear-gradient(180deg, #0e1a2b 0%, #152a45 55%, #0e1a2b 100%);
  color: #fff;
  min-height: 100vh;
}

a {
  color: inherit;
  text-decoration: none;
}

/* Botões */
.btn {
  display: inline-block;
  padding: 12px 18px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.22);
  font-weight: 700;
  transition: transform 0.15s ease, background 0.15s ease;
}

.btn:hover {
  transform: translateY(-1px);
  background: rgba(255, 255, 255, 0.18);
}

.btn.secondary {
  background: rgba(0, 0, 0, 0.18);
}

/* Home */
.home {
  max-width: 900px;
  margin: 0 auto;
  padding: 28px 18px 50px;
}

.home-header {
  text-align: center;
  padding: 12px 0 24px;
}

.home-header h1 {
  font-size: 44px;
  letter-spacing: 0.5px;
  font-weight: 800;
}

.home-header p {
  opacity: 0.85;
  margin-top: 10px;
}

.home-main {
  display: grid;
  gap: 18px;
  margin-top: 8px;
}

.home-card {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.16);
  box-shadow: 0 18px 50px rgba(0, 0, 0, 0.25);
  border-radius: 18px;
  padding: 22px;
}

.home-card h2 {
  font-size: 22px;
  margin-bottom: 10px;
}

.home-card p {
  opacity: 0.9;
  line-height: 1.5;
}

.home-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  justify-content: center;
}

.home-footer {
  text-align: center;
  margin-top: 28px;
  opacity: 0.7;
}

/* Deploy */
.deploy {
  max-width: 900px;
  margin: 0 auto;
  padding: 28px 18px 50px;
}

.deploy-header {
  text-align: center;
  padding: 12px 0 24px;
}

.deploy-header h1 {
  font-size: 38px;
  font-weight: 800;
}

.deploy-header p {
  opacity: 0.85;
  margin-top: 10px;
}

.deploy-main {
  display: grid;
  gap: 18px;
}

.deploy-card {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.16);
  box-shadow: 0 18px 50px rgba(0, 0, 0, 0.25);
  border-radius: 18px;
  padding: 22px;
}

.deploy-card h2 {
  font-size: 20px;
  margin-bottom: 10px;
}

.deploy-card ul,
.deploy-card ol {
  margin-left: 20px;
  line-height: 1.6;
  opacity: 0.9;
}

.deploy-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  justify-content: center;
}

.deploy-footer {
  text-align: center;
  margin-top: 28px;
  opacity: 0.7;
}

/* ==========================================
   Ajustes / adições para Streamlit (Python)
   ========================================== */

:root {
  --card-w: 140px;
  --card-h: 190px;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
  background: linear-gradient(180deg, #0e1a2b 0%, #152a45 55%, #0e1a2b 100%);
  color: #fff;
}

h1, h2, h3, p, div {
  color: #fff;
}

.game-title {
  text-align: center;
  font-size: 44px;
  margin: 10px 0 18px;
  letter-spacing: .5px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(4, var(--card-w));
  gap: 18px;
  justify-content: center;
}

@media (max-width: 560px) {
  :root { --card-w: 110px; --card-h: 150px; }
  .grid {
    grid-template-columns: repeat(3, var(--card-w));
    gap: 14px;
  }
}

.card-btn {
  width: var(--card-w);
  height: var(--card-h);
  border-radius: 14px;
  border: 2px solid rgba(255,255,255,.25);
  background: rgba(255,255,255,.08);
  box-shadow: 0 12px 24px rgba(0,0,0,.28);
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: transform .15s ease, opacity .2s ease;
}

.card-btn:hover {
  transform: translateY(-2px) scale(1.01);
}

.card-btn.used {
  opacity: .25;
  cursor: not-allowed;
}

.card-btn::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 30% 25%, rgba(255,255,255,.18), transparent 55%),
              radial-gradient(circle at 75% 70%, rgba(255,255,255,.12), transparent 55%);
}

.card-badge {
  position: absolute;
  top: 10px;
  left: 10px;
  font-weight: 700;
  font-size: 13px;
  padding: 6px 9px;
  border-radius: 999px;
  background: rgba(0,0,0,.35);
  border: 1px solid rgba(255,255,255,.18);
}

.end-message {
  text-align:center;
  font-size: 40px;
  margin-top: 30px;
  font-weight: 800;
  opacity: .95;
}

.small-note {
  text-align:center;
  opacity: .85;
  margin-top: 8px;
}
"""

st.markdown(f"<style>{BASE_CSS}</style>", unsafe_allow_html=True)

# -----------------------------
# Estado
# -----------------------------
if "order" not in st.session_state:
    st.session_state.order = [c["id"] for c in CARDS]
    random.shuffle(st.session_state.order)

if "used" not in st.session_state:
    st.session_state.used = set()

if "selected" not in st.session_state:
    st.session_state.selected = None  # id


def reset_game():
    st.session_state.order = [c["id"] for c in CARDS]
    random.shuffle(st.session_state.order)
    st.session_state.used = set()
    st.session_state.selected = None


def img_to_b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("utf-8")


def render_modal(card: dict):
    img_path = ASSETS_DIR / Path(card["img"]).name
    img_b64 = img_to_b64(img_path)
    text = card["text"]

    modal_html = """<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<style>
  body {
    margin: 0;
    font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
    background: transparent;
  }
  .overlay {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,.72);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 22px;
  }
  .card {
    width: min(420px, 92vw);
    height: min(560px, 78vh);
    perspective: 1100px;
  }
  .inner {
    width: 100%;
    height: 100%;
    border-radius: 18px;
    position: relative;
    transform-style: preserve-3d;
    transition: transform .6s ease;
    box-shadow: 0 18px 60px rgba(0,0,0,.55);
    border: 1px solid rgba(255,255,255,.20);
  }
  .inner.flipped {
    transform: rotateY(180deg);
  }
  .face {
    position: absolute;
    inset: 0;
    border-radius: 18px;
    backface-visibility: hidden;
    overflow: hidden;
  }
  .front {
    display:flex;
    align-items:center;
    justify-content:center;
    background: rgba(255,255,255,.06);
  }
  .front img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transform: scale(1.02);
  }
  .back {
    transform: rotateY(180deg);
    display:flex;
    align-items:center;
    justify-content:center;
    padding: 26px;
    background: linear-gradient(160deg, rgba(255,255,255,.08), rgba(255,255,255,.03));
  }
  .back p {
    margin: 0;
    color: #fff;
    font-size: 26px;
    line-height: 1.25;
    text-align: center;
    font-weight: 700;
    text-shadow: 0 6px 18px rgba(0,0,0,.45);
  }
  .hint {
    position: absolute;
    bottom: 14px;
    left: 0;
    right: 0;
    text-align: center;
    color: rgba(255,255,255,.78);
    font-size: 13px;
  }
</style>
</head>
<body>
  <div class="overlay">
    <div class="card" onclick="flip()">
      <div id="inner" class="inner">
        <div class="face front">
          <img src="data:image/png;base64,__IMG__" alt="Carta" />
          <div class="hint">Clique na carta para virar</div>
        </div>
        <div class="face back">
          <p>__TEXT__</p>
          <div class="hint">Clique na carta para voltar</div>
        </div>
      </div>
    </div>
  </div>

<script>
  const el = document.getElementById("inner");
  setTimeout(() => el.classList.add("flipped"), 120);
  function flip() {
    el.classList.toggle("flipped");
  }
</script>
</body>
</html>
"""

    modal_html = modal_html.replace("__IMG__", img_b64).replace("__TEXT__", text)
    components.html(modal_html, height=650, scrolling=False)


# -----------------------------
# Navegação
# -----------------------------
page = st.sidebar.radio("Navegação", ["🏠 Home", "🃏 Jogo (11 Cartas)", "📄 Deploy / Ajuda"], index=1)

if page == "🏠 Home":
    st.title("Retiro 2026")
    st.caption("Conteúdo do arquivo home.html (renderizado em um iframe).")
    components.html(HOME_HTML, height=850, scrolling=True)

elif page == "📄 Deploy / Ajuda":
    st.title("Deploy / Ajuda")
    st.caption("Conteúdo do arquivo deploy.html (renderizado em um iframe).")
    components.html(DEPLOY_HTML, height=950, scrolling=True)

else:
    st.markdown('<div class="game-title">Retiro 2026</div>', unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1])
    with c1:
        if st.button("🔄 Reiniciar"):
            reset_game()
            st.rerun()
    with c2:
        st.markdown(
            f'<div class="small-note">Cartas jogadas: <b>{len(st.session_state.used)}</b> / <b>{len(CARDS)}</b></div>',
            unsafe_allow_html=True,
        )

    if len(st.session_state.used) >= len(CARDS):
        st.markdown('<div class="end-message">Muchas Gracias.</div>', unsafe_allow_html=True)
        st.stop()

    st.markdown('<div class="grid">', unsafe_allow_html=True)

    for card in [next(c for c in CARDS if c["id"] == cid) for cid in st.session_state.order]:
        card_id = card["id"]
        used = card_id in st.session_state.used
        cls = "used" if used else ""

        clicked = st.button(" ", key=f"card_{card_id}", disabled=used, help="Clique para abrir")
        st.markdown(
            f'<div class="card-btn {cls}"><div class="card-badge">#{card_id}</div></div>',
            unsafe_allow_html=True,
        )

        if clicked and not used:
            st.session_state.selected = card_id
            st.session_state.used.add(card_id)
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.selected is not None:
        selected = next(c for c in CARDS if c["id"] == st.session_state.selected)
        render_modal(selected)
        if st.button("Fechar carta"):
            st.session_state.selected = None
            st.rerun()
