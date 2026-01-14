import streamlit as st

st.set_page_config(
    page_title="Living Galaxy",
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
    text-shadow: 0 0 40px rgba(168,85,247,0.9);
}

p {
    max-width: 680px;
    margin-top: 1.2rem;
    font-size: 1.1rem;
    color: #cbd5f5;
}

/* CANVAS */
canvas {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1;
}
</style>

<canvas id="galaxy"></canvas>

<script>
const canvas = document.getElementById("galaxy");
const ctx = canvas.getContext("2d");

function resize(){
    canvas.width = innerWidth;
    canvas.height = innerHeight;
}
resize();
addEventListener("resize", resize);

// ===== GALAXY STAR FIELD =====
const STAR_COUNT = 1400;
let stars = [];
let angleOffset = 0;

function createGalaxy(){
    stars = [];
    for(let i=0;i<STAR_COUNT;i++){
        const arm = i % 4;
        const radius = Math.random() ** 0.5 * Math.min(innerWidth, innerHeight) * 0.45;
        const angle = radius * 0.03 + arm * Math.PI/2;
        stars.push({
            r: radius,
            a: angle,
            size: Math.random()*1.6 + 0.4,
            speed: Math.random()*0.0006 + 0.0002,
            hue: 200 + Math.random()*80
        });
    }
}
createGalaxy();

// ===== SCROLL EFFECT =====
addEventListener("scroll", () => {
    angleOffset = scrollY * 0.0003;
});

// ===== ANIMATION =====
function animate(){
    ctx.clearRect(0,0,canvas.width,canvas.height);

    // core glow
    const cx = canvas.width/2;
    const cy = canvas.height/2;
    const grd = ctx.createRadialGradient(cx,cy,0,cx,cy,200);
    grd.addColorStop(0,"rgba(255,255,255,0.9)");
    grd.addColorStop(0.4,"rgba(180,200,255,0.4)");
    grd.addColorStop(1,"rgba(0,0,0,0)");
    ctx.fillStyle = grd;
    ctx.beginPath();
    ctx.arc(cx,cy,200,0,Math.PI*2);
    ctx.fill();

    // stars
    stars.forEach(s=>{
        s.a += s.speed;
        const a = s.a + angleOffset;
        const x = cx + Math.cos(a) * s.r;
        const y = cy + Math.sin(a) * s.r;

        ctx.fillStyle = `hsla(${s.hue},80%,70%,0.9)`;
        ctx.beginPath();
        ctx.arc(x,y,s.size,0,Math.PI*2);
        ctx.fill();
    });

    requestAnimationFrame(animate);
}
animate();
</script>
""", unsafe_allow_html=True)

# ===== CONTENT =====
st.markdown("""
<section class="section center">
    <h1>Living Spiral Galaxy</h1>
    <p>
        Một thiên hà xoắn sống động – các vì sao quay quanh lõi sáng rực,
        tạo nên chiều sâu và chuyển động như ngoài vũ trụ thật.
    </p>
</section>

<section class="section center">
    <h1>Infinite Depth</h1>
    <p>
        Cuộn xuống để cảm nhận sự chuyển dịch của không gian và thời gian.
    </p>
</section>
""", unsafe_allow_html=True)
