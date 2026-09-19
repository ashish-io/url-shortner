document.querySelector("button").addEventListener("click", async function (event) {
  event.preventDefault();

  const longUrl = document.getElementById("urlInput").value;
  const token = localStorage.getItem("access_token");

  const response = await fetch("http://localhost:8000/link/shortern", {
    method: "POST",
    headers: { "Content-Type": "application/json",
               "Authorization": `Bearer ${token}`

     },
    body: JSON.stringify({ long_url: longUrl })
  });

  const data = await response.json();

  const shortLink = `http://localhost:8000/link/${data.short_code}`;

  document.getElementById("result").innerHTML = `<a href="${shortLink}">${shortLink}</a>`;
});