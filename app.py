import streamlit as st

st.set_page_config(
    page_title="Cosmic Multiverse",
    page_icon="🌌",
    layout="wide"
)

st.markdown("""
<style>
html, body, [class*="css"] {
    background: black;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

#MainMenu, footer, header { visibility: hidden; }

.section {
    min-height: 100vh;
    padding: 6rem 1.5rem;
    position: relative;
    z-index: 10;
}

.center {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}

h1 {
    font-size: clamp(2.8rem, 6vw, 4.8rem);
    background: linear-gradient(90deg, #7dd3fc, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 35px rgba(168,85,247,0.9);
}

p {
    max-width: 650px;
    margin-top: 1.2rem;
    font-size: 1.1rem;
    color: #cbd5f5;
}

/* ===== PLANET ===== */
.planet-wrapper {
    position: absolute;
    bottom: -180px;
    right: -180px;
    width: 420px;
    height: 420px;
}

.planet-core {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background:
        repeating-linear-gradient(120deg,#3b0764,#6d28d9 30px),
        radial-gradient(circle at 30% 30%, #8b5cf6, #020617 70%);
    background-blend-mode: overlay;
    box-shadow:
        inset -40px -40px 100px rgba(0,0,0,0.8),
        0 0 120px rgba(124,58,237,0.6);
    animation: spin 90s linear infinite;
}

.clouds {
    position: absolute;
    inset: 0;
    border-radius: 50%;
    background:
        radial-gradient(circle at 40% 30%, rgba(255,255,255,0.15), transparent 60%),
        radial-gradient(circle at 70% 60%, rgba(255,255,255,0.12), transparent 65%);
    filter: blur(2px);
    animation: spin-reverse 120s linear infinite;
}

.shadow {
    position: absolute;
    inset: 0;
    border-radius: 50%;
    box-shadow: inset -60px -30px 140px rgba(0,0,0,0.9);
}

/* ===== ANIMATIONS ===== */
@keyframes spin {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}

@keyframes spin-reverse {
    from { transform: rotate(360deg); }
    to   { transform: rotate(0deg); }
}

/* ===== CANVAS ===== */
canvas {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1;
}

/* MOBILE */
@media (max-width: 768px) {
    .planet-wrapper {
        width: 240px;
        height: 240px;
        bottom: -100px;
        right: -100px;
    }
}
</style>

<canvas id="stars"></canvas>
<canvas id="lava"></canvas>

<script>
/* ===== STAR SYSTEMS ===== */
const starCanvas = document.getElementById("stars");
const sctx = starCanvas.getContext("2d");

function resize() {
    starCanvas.width = innerWidth;
    starCanvas.height = innerHeight;
}
resize(); addEventListener("resize", resize);

let systems = [
    { speed: 0.2, color: "white" },
    { speed: 0.4, color: "#7dd3fc" },
    { speed: 0.7, color: "#f472b6" }
];

let currentSystem = 0;

let stars = Array.from({length: 180}, () => ({
    x: Math.random()*innerWidth,
    y: Math.random()*innerHeight,
    r: Math.random()*1.5
}));

/* ===== LAVA PARTICLES ===== */
const lavaCanvas = document.getElementById("lava");
const lctx = lavaCanvas.getContext("2d");

function resizeLava() {
    lavaCanvas.width = innerWidth;
    lavaCanvas.height = innerHeight;
}
resizeLava(); addEventListener("resize", resizeLava);

let lava = [];

function spawnLava() {
    for(let i=0;i<6;i++){
        lava.push({
            x: innerWidth*0.8 + Math.random()*20,
            y: innerHeight*0.8,
            vx: (Math.random()-0.5)*1.5,
            vy: -Math.random()*4 - 3,
            life: 100
        });
    }
}

addEventListener("scroll", () => {
    const y = scrollY;
    currentSystem = Math.min(
        systems.length-1,
        Math.floor(y / innerHeight)
    );
});

/* ===== ANIMATION LOOP ===== */
function animate() {
    // STARS
    sctx.clearRect(0,0,starCanvas.width,starCanvas.height);
    let sys = systems[currentSystem];
    sctx.fillStyle = sys.color;
    stars.forEach(st => {
        sctx.beginPath();
        sctx.arc(st.x, st.y, st.r, 0, Math.PI*2);
        sctx.fill();
        st.y += sys.speed;
        if(st.y > innerHeight){ st.y = 0; st.x = Math.random()*innerWidth; }
    });

    // LAVA
    lctx.clearRect(0,0,lavaCanvas.width,lavaCanvas.height);
    spawnLava();
    lava.forEach(p => {
        lctx.fillStyle = "rgba(255,120,0,0.8)";
        lctx.beginPath();
        lctx.arc(p.x, p.y, 3, 0, Math.PI*2);
        lctx.fill();
        p.x += p.vx;
        p.y += p.vy;
        p.vy += 0.15;
        p.life--;
    });
    lava = lava.filter(p => p.life > 0);

    requestAnimationFrame(animate);
}
animate();
</script>
""", unsafe_allow_html=True)

# ===== CONTENT =====
st.markdown("""
<section class="section center">
    <h1>Volcanic System</h1>
    <p>Hành tinh dung nham – các tia lửa phun trào từ lõi hành tinh.</p>

    <div class="planet-wrapper">
        <div class="planet-core"></div>
        <div class="clouds"></div>
        <div class="shadow"></div>
    </div>
</section>

<section class="section center">
    <h1>Blue Star System</h1>
    <p>Cuộn xuống – bạn đã bước sang một hệ sao xanh lạnh.</p>
</section>

<section class="section center">
    <h1>Crimson Galaxy</h1>
    <p>Mỗi hệ sao là một vũ trụ khác biệt.</p>
</section>
""", unsafe_allow_html=True)
