<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skillering - لوحة التحكم</title>
    <link rel="stylesheet" href="{{ asset('css/welcomepage/dashbord.css') }}">
</head>
<body>
    <header class="internal-header">
        <div class="logo">LOGO</div>
        <nav>
            <a href="#">Dashboard</a>
            <a href="#">courses</a>
            <a href="#">Community</a>
            <a href="#">events</a>
            <a href="#">Marketplace</a>
            <div class="bell">🔔</div>
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
        </ul>
    </div>

    <main>
        <section class="content-area">
            <!-- المحتوى هنا يمكن تطويره لاحقًا -->
        </section>
    </main>

    <footer>
        <!-- نفس الفوتر من index.html -->
    </footer>

    <script>
        function toggleMenu() {
            const sidebar = document.getElementById('sidebar');
            sidebar.classList.toggle('active');
        }
    </script>
</body>
</html>
