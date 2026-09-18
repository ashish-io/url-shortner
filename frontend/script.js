document.querySelector("button").addEventListener("click", async function (event) {
  event.preventDefault();

  const longUrl = document.getElementById("urlInput").value;

  const response = await fetch("http://localhost:8000/shortern", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ long_url: longUrl })
  });

  const data = await response.json();

  const shortLink = `http://localhost:8000/${data.short_code}`;

  document.getElementById("result").innerHTML = `<a href="${shortLink}">${shortLink}</a>`;
});