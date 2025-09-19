<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skillering - الصفحة الرئيسية</title>
    <link rel="stylesheet" href="welcomepage.css">
</head> 
<body>
    <header>
        <div class="logo">LOGO</div>
        <nav>
          <a href="../Sign In/Sign In.html">
            <button>Sign In</button>
            </a>
            <a href="../Sign Up/Sign Up.html">
            <button>Sign Up</button>
            </a>
            <div class="menu" onclick="toggleMenu()">☰</div>
        </nav>
    </header>

    <div class="sidebar" id="sidebar">
        <ul>
            <li><a href="#">الرئيسية</a></li>
            <li><a href="#">الدورات</a></li>
            <li><a href="#">المجتمع</a></li>
            <li><a href="#">الأحداث</a></li>
            <li><a href="#">السوق</a></li>
            <li><a href="../Welcomepage/Dashbord.html">لوحة التحكم</a></li>
        </ul>
    </div>

    <main>
        <section class="hero">
            <div class="big-logo">LOGO</div>
            <div class="about-block">about us</div>
            <button class="analyze-btn">Analyze my screen time now →</button>
            <button class="learn-btn">Learn more</button>
        </section>

        <section class="features">
            <div class="card">
                <div class="icon">LOGO</div>
                <h3>DETECT</h3>
                <p>We analyze your screen time patterns and identify opportunities for growth</p>
            </div>
            <div class="card">
                <div class="icon">LOGO</div>
                <h3>LEARN</h3>
                <p>We analyze your screen time patterns and identify opportunities for growth</p>
            </div>
            <div class="card">
                <div class="icon">LOGO</div>
                <h3>SHARE</h3>
                <p>We analyze your screen time patterns and identify opportunities for growth</p>
            </div>
        </section>
    </main>

    <footer>
        <div class="footer-top">
            <div class="footer-logo">LOGO</div>
            <div class="footer-sections">
                <div class="quick-links">
                    <h4>QUICK LINKS</h4>
                    <ul>
                        <li>About Us</li>
                        <li>How It Works</li>
                        <li>Success Stories</li>
                        <li>Blog</li>
                        <li>Careers</li>
                    </ul>
                </div>
                <div class="community">
                    <h4>COMMUNITY</h4>
                    <ul>
                        <li>Courses</li>
                        <li>Events</li>
                        <li>Marketplace</li>
                        <li>Creator Program</li>
                        <li>Community Guidelines</li>
                    </ul>
                </div>
                <div class="support">
                    <h4>SUPPORT</h4>
                    <ul>
                        <li>Help Center</li>
                        <li>FAQ</li>
                        <li>Contact Support</li>
                        <li>Privacy Policy</li>
                        <li>Terms of Service</li>
                    </ul>
                </div>
                <div class="contact">
                    <h4>CONTACT INFO</h4>
                    <p>📧 hello@Skillering.com</p>
                    <p>☎️ +1 (555) 123-4567</p>
                    <p>📍 Egypt</p>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <div class="social">
                <span>f</span> <span>🕊️</span> <span>📷</span> <span>🔗</span>
            </div>
            <div class="subscribe">
                <p>Stay Updated</p>
                <p>Get the latest updates on new courses, events, and community highlights.</p>
                <select>
                    <option>Language: English</option>
                </select>
                <input type="email" placeholder="Email">
                <button>SUBSCRIBE</button>
            </div>
            <p class="copyright">© 2025 Skillering. All rights reserved. Transforming screen time into skill time since 2024.</p>
        </div>
    </footer>

    <script>
        function toggleMenu() {
            const sidebar = document.getElementById('sidebar');
            sidebar.classList.toggle('active');
        }
    </script>
</body>
</html>