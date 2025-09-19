<!DOCTYPE html><html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Skills Selection</title>
  <link rel="stylesheet" href="{{ asset('css/suggest_page/suggest.css') }}">
</head>
<body>
  <div class="page">
    <!-- header with logo -->
    <header class="topbar">
      <div class="logo-box">
        <img src="logo.png" alt="logo" class="logo-img">
      </div>
    </header><div class="container">
  <h1>Choose a Skill</h1>
  <div class="bubbles">
    <div class="bubble">Skill 1</div>
    <div class="bubble">Skill 2</div>
    <div class="bubble">Skill 3</div>
  </div>

  <div class="chat-box">
    <input type="text" placeholder="Or type your own skill...">
    <button>Submit</button>
  </div>

  <div class="actions">
    <button class="regenerate">Regenerate Skills</button>
  </div>
</div>

<!-- footer -->
<footer class="page-footer">
  <div class="footer-left">Logo small</div>
  <nav class="footer-links">
    <a href="#">@2025</a><br>
    <a href="{{ route('user_agreement') }}">User Agreement</a><br>
    <a href="{{ route('privacy_policy') }}">Privacy policy</a><br>
    <a href="{{ route('cookie_policy') }}">Cookie Policy</a><br>
    <a href="{{ route('send_feedback') }}">Send Feedback</a><br>
    <a href="{{ route('terms_conditions') }}">Terms & Conditions</a>
  </nav>
  <div class="lang">Language ▾</div>
</footer>

  </div>
</body>
</html>
