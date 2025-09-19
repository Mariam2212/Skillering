<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Skillering - Verify Code</title>
  <link rel="stylesheet" href="{{ asset('css/verify/verify.css') }}">
</head>
<body>
      <img src="logo.png" alt="Skillering Logo" class="logo">
     <a href="{{ route('signin') }}">
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <button>Sign In</button>
      </a><a href="{{ route('signup') }}">
      <button>Sign Up</button>
      </a>

  <div class="container">

    <p class="instruction">Enter the 6-digit code</p>
    <p class="check-email">Check ******@gmail.com for a verification code</p>
    <a href="{{ route('forgetpassword') }}" class="change">Change</a>

    <input type="text" maxlength="6" placeholder="6-digit code">

    <div class="buttons">
      <button class="resend">Resend Code</button>
      <button class="submit">Submit</button>
    </div>

    <p class="note">
      If you don't see the email in your inbox, check your spam folder. If it's not there, the email address may not be confirmed or may not match an existing Skillering account.
    </p>

    <a href="{{ route('cant_access_email') }}" class="cant-access">Can't access this email?</a>

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
