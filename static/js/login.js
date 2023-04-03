function togglePasswordVisibility() {
    const passwordInput = document.getElementById("password");
    const togglePassword = document.querySelector(".toggle-password");
  
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      togglePassword.innerHTML = '<i class="fa fa-eye-slash"></i>';
      togglePassword.style.marginRight = "10px";
    } else {
      passwordInput.type = "password";
      togglePassword.innerHTML = '<i class="fa fa-eye"></i>';
      togglePassword.style.marginRight = "auto";
    }
  }


  function showDiv(divId) {
    var div = document.getElementById(divId);
    div.style.display = "block";
    
    var otherDivId = (divId === "div1") ? "div2" : "div1";
    var otherDiv = document.getElementById(otherDivId);
    otherDiv.style.display = "none";
  }
  
  
  