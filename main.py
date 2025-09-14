from flask import Flask, render_template_string

app = Flask(__name__)

# Yahan aapka HTML rakha hai
html_code = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Server Panel Banners</title>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@300;600;800&display=swap" rel="stylesheet">
  <style>
    :root{
      --banner-height:340px;
      --panel-height:120px;
      --accent:linear-gradient(90deg,#0ea5a0,#06b6d4);
    }
    *{box-sizing:border-box}
    body{margin:0;font-family:Montserrat, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial; background:#0f1724; color:#fff}
    .container{max-width:1000px;margin:40px auto;padding:20px}.banner-wrap{margin-bottom:44px;border-radius:14px;overflow:hidden;box-shadow:0 12px 40px rgba(2,6,23,0.7)}

.banner{
  position:relative;
  height:var(--banner-height);
  display:flex;
  align-items:center;
  justify-content:center;
  background-position:center center;
  background-size:cover;
  background-repeat:no-repeat;
}
.banner::before{
  content:"";
  position:absolute;inset:0;
  background:linear-gradient(180deg, rgba(2,6,23,0.18), rgba(2,6,23,0.5));
  z-index:0;
}
.banner .label{
  position:relative;z-index:1;
  font-size:clamp(28px, 4vw, 48px);
  font-weight:800;
  color:#fff;
  text-shadow:0 6px 28px rgba(2,6,23,0.7);
  padding:14px 26px;
  border-radius:10px;
  background: none;
  letter-spacing:1px;
}

.long-panel{
  display:flex;align-items:center;justify-content:center;
  height:var(--panel-height);
  background: linear-gradient(90deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
  border-top:1px solid rgba(255,255,255,0.04);
  gap:18px;padding:18px 28px;
}
.long-panel .left-deco{
  width:6px;height:100%;border-radius:4px;background:var(--accent);
  box-shadow:0 6px 18px rgba(6,182,212,0.12), 0 1px 0 rgba(255,255,255,0.03) inset;
}
.long-panel .title{
  font-family:'Bebas Neue', sans-serif;
  font-size:48px;line-height:1;
  letter-spacing:6px;text-transform:uppercase;color:#fff;
  text-shadow:0 6px 24px rgba(2,6,23,0.6);
  display:flex;align-items:center;gap:12px;
}
.long-panel .subtitle{
  margin-left:6px;color:rgba(255,255,255,0.65);font-size:14px;letter-spacing:1px;font-weight:600;
  transform:translateY(2px);
}

@media(min-width:1000px){
  :root{--panel-height:140px;--banner-height:380px}
  .long-panel .title{font-size:64px}
}

@media (max-width:520px){
  :root{--banner-height:220px;--panel-height:92px}
  .container{padding:12px;margin:20px auto}
  .long-panel{padding:12px}
  .long-panel .title{font-size:32px;letter-spacing:4px}
}
  </style>
</head>
<body>
  <div class="container">
    <!-- Wrapper for first banner -->
    <div class="banner-wrap">
      <a href="http://fi4.bot-hosting.net:22504" target="_blank">
        <section class="banner" style="background-image:url('https://iili.io/KTLPx1f.md.jpg')">
          <div class="label"></div>
        </section>
      </a>
      <div class="long-panel">
        <div class="left-deco" aria-hidden></div>
        <div>
          <div class="title">Server 1</div>
          <div class="subtitle">Terror Rulex</div>
        </div>
      </div>
    </div>

    <!-- Wrapper for second banner -->
    <div class="banner-wrap">
      <a href="https://server-terror-panel1.onrender.com" target="_blank">
        <section class="banner" style="background-image:url('https://iili.io/KTLPAeS.md.jpg')">
          <div class="label"></div>
        </section>
      </a>
      <div class="long-panel">
        <div class="left-deco" aria-hidden></div>
        <div>
          <div class="title">Panel 2</div>
          <div class="subtitle">Terror Rulex 2.0 Server</div>
        </div>
      </div>
    </div>

    <p style="color:rgba(255,255,255,0.65);text-align:center;margin-top:6px;font-size:13px">
      - The Legend Boiiz Off Teror Faiizu Stuner Awiso Waqas Zaiin Bawa On fire
    </p>
  </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html_code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
