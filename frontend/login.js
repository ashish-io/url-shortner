const loginForm = document.getElementById("LoginForm")
const message = document.getElementById("message")

loginForm.addEventListener("submit", async function(event){

  event.preventDefault();

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const formData = new URLSearchParams();

  formData.append("username", username);
  formData.append("password", password);

  const response = await fetch("http://localhost:8000/login", 
    {
      method: "POST",
      headers: {
         "Content-Type":"application/x-www-form-urlencoded"

      },

      body: formData


  });

  const data = await response.json();

  if(response.status === 404){
     message.textContent = data.detail
  }
  else if(response.status === 401){
     message.textContent = data.detail
  }

  else if(response.status === 200){

    localStorage.setItem("access_token", data.access_token)
    message.textContent = "login successful"
    

     window.location.href = "index.html";
  }



});