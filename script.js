function predictColleges() {
  const name = document.getElementById("name").value;
  const marks12 = parseFloat(document.getElementById("marks12").value);
  const cetjee = parseFloat(document.getElementById("cetjee").value);

  if (!name || isNaN(marks12) || isNaN(cetjee)) {
      alert("Please fill in all fields correctly.");
      return;
  }

  fetch("http://127.0.0.1:3001/api/predict", {
      method: "POST",
      headers: {
          "Content-Type": "application/json",
      },
      body: JSON.stringify({
          name,
          marks12,
          cetjee,
      }),
  })
  .then(response => response.json())
  .then(data => {
      const suggestionsDiv = document.getElementById("suggestions");
      if (data.colleges && data.colleges.length > 0) {
          let html = "";
          data.colleges.forEach(college => {
              html += `
                  <div class="college-card">
                      <h4>${college.name}</h4>
                      <p>Cutoff: ${college.cutoff}%</p>
                      <p>Location: ${college.location}</p>
                  </div>
              `;
          });
          suggestionsDiv.innerHTML = html;
      } else {
          suggestionsDiv.innerHTML = "<p>No colleges found matching your input.</p>";
      }
  })
  .catch(() => {
      document.getElementById("suggestions").innerHTML = "<p>Error contacting server.</p>";
  });
}