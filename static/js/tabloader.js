function openTab(evt, tabName) {
  var i, tabitems, tabselect, isActive;
  const clickTarget = document.getElementById(tabName);
  console.log(evt.currentTarget.className.indexOf(" active"));
  console.log(evt.currentTarget.className.indexOf(" active") > 0);
  isActive = evt.currentTarget.className.indexOf(" active") > 0;

  tabitems = document.getElementsByClassName("content-tab__item");
  for (i = 0; i < tabitems.length; i++) {
    tabitems[i].style.display = "none";
  }

  tabselect = document.getElementsByClassName("tab-selector");
  for (i = 0; i < tabselect.length; i++) {
    tabselect[i].className = tabselect[i].className.replace(" active", "");
  }

  if (!isActive) {
    clickTarget.style.display = "block";
    evt.currentTarget.className += " active";
  }
} 