function toggleMenu(){
  const textnames = ["Home", " About Us"]
  const sidebarE1 = document.getElementsByClassName("sidebar")[0];
  const contentE1 = document.getElementsByClassName("content")[0];
  let menuItems = document.getElementsByClassName("fa");
  sidebarE1.classList.toggle("sidebar--isHidden");
  contentE1.classList.toggle("content--isHidden");
  for(item in menuItems){
    if(menuItems[item].innerHTML === textnames[item]){
      menuItems[item].innerHTML = "";
    }else{
      menuItems[item].innerHTML = textnames[item];
    }
  }
  if(window.sessionStorage.getItem("MenuState") != "--isHidden"){
    window.sessionStorage.setItem("MenuState", "--isHidden");
  }else{
    window.sessionStorage.setItem("MenuState", "");
  }
}

function setMenuState(){
  const sidebarE1 = document.getElementsByClassName("sidebar")[0];
  const contentE1 = document.getElementsByClassName("content")[0];
  if (window.sessionStorage.getItem("MenuState") == null){
    window.sessionStorage.setItem("MenuState", "--isHidden");
  }

  if(window.sessionStorage.getItem("MenuState") != "--isHidden"){
    toggleMenu();
    window.sessionStorage.setItem("MenuState", "");
  }
  setTimeout(()=>{
  if(!sidebarE1.classList.contains("sidebar-animated")){
    sidebarE1.classList.add("sidebar-animated");
    contentE1.classList.add("content-animated");
  }}, 250);
}

function expandMenu(evt, menuItem) {
  var i, tabitems, tabselect, isActive;
  const clickTarget = document.getElementById(menuItem);
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