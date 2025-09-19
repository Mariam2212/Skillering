<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Skillering - Can't Access Email</title>
  <link rel="stylesheet" href="{{ asset('css/verify/cant_access_this_email.css') }}">
</head>
<body>
  <img src="logo.png" alt="Skillering Logo" class="logo">
  <div class="container">
    <h2>Can't Access This Email?</h2>
    <p class="description">
      If you no longer have access to ******@gmail.com, we can help you recover your account using an alternative method.
    </p>

    <label for="alt-contact">Enter a new email or phone number</label>
    <input type="text" id="alt-contact" placeholder="New email or phone number">

    <p class="note">
      We'll use this contact to verify your identity and help you regain access to your Skillering account.
    </p>

    <button class="submit">Continue</button>

  </div>
   <center>
     <footer>
       <img src="logo-small.png" alt="Small Logo" class="logo-small">
        <a href="#">@2025</a>&nbsp;&nbsp;
        <a href="{{ route('user_agreement') }}">User Agreement</a>&nbsp;&nbsp;
        <a href="{{ route('privacy_policy') }}">Privacy Policy</a>&nbsp;&nbsp;
        <a href="{{ route('cookie_policy') }}">Cookie Policy</a>&nbsp;&nbsp;
        <a href="{{ route('send_feedback') }}">Send Feedback</a>&nbsp;&nbsp;
        <a href="{{ route('terms_conditions') }}">Terms & Conditions</a>&nbsp;&nbsp;
      </nav>
      <div class="lang">Language ▼</div>
    </footer>
    </center>
</body>
</html>
