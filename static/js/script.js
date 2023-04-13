function showDiv(divId) {
    var div = document.getElementById(divId);
    div.style.display = "block";
    
    var otherDivId = (divId === "box1") ? "box2" : "box1";
    var otherDiv = document.getElementById(otherDivId);
    otherDiv.style.display = "none";
  }