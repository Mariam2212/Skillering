<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Skillering - Upload CSV</title>
  <link rel="stylesheet" href="{{ asset('css/csv_page/csv.css') }}">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js"></script>
</head>
<body>
  <div class="container">
    <!-- Logo at Top Left -->
    <div class="header">
      <img src="path/to/skillering-logo.png" alt="Skillering Logo" class="logo-top">
    </div>

    <!-- Video Guide Section -->
    <div class="section">
      <h2>Video Guide</h2>
      <p>Watch this video to learn how to upload a CSV file:</p>
      <div class="video-container">
        <iframe width="560" height="315"
                src="https://www.youtube.com/embed/USKsXNYmDoQ"
                title="CSV Upload Guide"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen>
        </iframe>
      </div>
    </div>

    <!-- CSV Upload Section -->
    <div class="section">
      <h2>Upload CSV File</h2>
      <div class="upload-section">
        <input type="file" id="csvFileInput" accept=".csv">
        <button onclick="uploadCSV()">Upload</button>
      </div>
      <table id="csvTable">
        <thead id="tableHead"></thead>
        <tbody id="tableBody"></tbody>
      </table>
    </div>

    <!-- Footer with Small Logo -->
    <div class="footer">
      <img src="path/to/skillering-logo-small.png" alt="Skillering Logo" class="logo-bottom">
      <div class="footer-links">
        <p>
          &copy;2025
          <a href="{{ route('user_agreement') }}">User Agreement</a>
          <a href="{{ route('privacy_policy') }}">Privacy policy</a>
          <a href="{{ route('cookie_policy') }}">Cookie Policy</a>
          <a href="{{ route('send_feedback') }}">Send Feedback</a>
          <a href="{{ route('terms_conditions') }}">Terms & Conditions</a>
        </p>
      </div>
      <div class="language-select">
        <select>
          <option>Language</option>
          <option>English</option>
          <option>العربية</option>
        </select>
      </div>
    </div>
  </div>

  <script>
    function uploadCSV() {
      const file = document.getElementById('csvFileInput').files[0];
      if (file) {
        Papa.parse(file, {
          header: true,
          skipEmptyLines: true,
          complete: function(results) {
            const data = results.data;
            const tableHead = document.getElementById('tableHead');
            const tableBody = document.getElementById('tableBody');

            // Clear previous table content
            tableHead.innerHTML = '';
            tableBody.innerHTML = '';

            // Create table headers
            const headers = Object.keys(data[0]);
            const headerRow = document.createElement('tr');
            headers.forEach(header => {
              const th = document.createElement('th');
              th.textContent = header;
              headerRow.appendChild(th);
            });
            tableHead.appendChild(headerRow);

            // Create table rows
            data.forEach(row => {
              const tr = document.createElement('tr');
              headers.forEach(header => {
                const td = document.createElement('td');
                td.textContent = row[header] || '';
                tr.appendChild(td);
              });
              tableBody.appendChild(tr);
            });
          },
          error: function(error) {
            alert('Error reading file: ' + error.message);
          }
        });
      } else {
        alert('Please select a CSV file first.');
      }
    }
  </script>
</body>
</html>
