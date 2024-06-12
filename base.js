const burger = document.querySelector(".burger");
const nav = document.querySelector(".nav_links");
const navLinks = document.querySelectorAll(".nav_links li");


burger.addEventListener("click", () => {
    nav.classList.toggle("nav-active");


    navLinks.forEach((link, inndex) => {
        if (link.style.animation) {
            link.style.animation = "";
        } else {
            link.style.animation = `navLinksFade 0.2s ease forwards ${inndex / 7 + 0.4}s`
        }
    });
    burger.classList.toggle("toggle")
});
