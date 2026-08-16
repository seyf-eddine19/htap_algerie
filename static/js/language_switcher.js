
function toggleLanguageMenu() {
    const menu = document.getElementById("language-menu");
    const button = document.getElementById("language-button");
    const chevron = document.getElementById("language-chevron");

    menu.classList.toggle("hidden");

    const isOpen = !menu.classList.contains("hidden");

    button.setAttribute("aria-expanded", isOpen);
    chevron.classList.toggle("rotate-180", isOpen);
}


document.addEventListener("click", function(event) {
    const switcher = document.getElementById("language-switcher");
    const menu = document.getElementById("language-menu");
    const button = document.getElementById("language-button");
    const chevron = document.getElementById("language-chevron");

    if (switcher && !switcher.contains(event.target)) {
        menu.classList.add("hidden");
        button.setAttribute("aria-expanded", "false");
        chevron.classList.remove("rotate-180");
    }
});