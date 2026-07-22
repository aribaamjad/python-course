const searchInput = document.getElementById("searchInput");

if (searchInput) {
    searchInput.addEventListener("keyup", function () {

        let value = searchInput.value.toLowerCase();

        let cards = document.querySelectorAll(".card");

        cards.forEach(function(card){

            let text = card.innerText.toLowerCase();

            if(text.includes(value)){
                card.style.display = "block";
            }else{
                card.style.display = "none";
            }

        });

    });
}
function toggleMenu(){

let menu=document.getElementById("navLinks");

menu.classList.toggle("active");

}
function toggleMenu() {

let menu = document.getElementById("navLinks");

menu.classList.toggle("active");

}
function toggleMenu() {
    document.getElementById("navLinks").classList.toggle("show");
}
function toggleTheme() {

document.body.classList.toggle("light-mode");

let btn = document.getElementById("themeBtn");

if(document.body.classList.contains("light-mode")){

btn.innerHTML="☀️";

}else{

btn.innerHTML="🌙";

}

}