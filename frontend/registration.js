const registrationForm = document.getElementById("RegistrationForm")
const message = document.getElementById("message")
registrationForm.addEventListener("submit", async function(event){

  event.preventDefault();

  const username = document.getElementById("username").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  if(password.length < 6){
    message.textContent = "Password lenght must be greater than 6"
    return ;
  }
  
  const response = await fetch("http://localhost:8000/register", {
    method:"POST",
    headers:{

      "Content-Type":"application/json"
    },
    body: JSON.stringify(
      {
        username:username,
        email:email,
        password:password
      }
    )

  }

  );

  const data = await response.json();

 
  if(response.status === 200){
  message.textContent = data.message;

  window.location.href = "login.html";
  }
  else{
    message.textContent = data.detail;
  }


});


