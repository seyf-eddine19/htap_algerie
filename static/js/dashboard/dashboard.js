document.addEventListener("DOMContentLoaded", function () {
    // 1. Theme Toggle Logic
    const savedTheme = localStorage.getItem("theme");
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

    if (savedTheme === "dark" || (!savedTheme && prefersDark)) {
        document.documentElement.classList.add("dark");
    } else {
        document.documentElement.classList.remove("dark");
    }

    // 2. Lucide Icons Initialization
    if (typeof lucide !== "undefined") {
        lucide.createIcons();
    }

    // 3. Global Event Delegation
    document.addEventListener("click", function (event) {
        // Toggle Mobile Sidebar
        const sidebarBtn = event.target.closest("[data-action='toggle-sidebar']");
        if (sidebarBtn) {
            const sidebar = document.getElementById("mobile-sidebar");
            if (sidebar) sidebar.classList.toggle("hidden");
            return;
        }

        // Toggle Language Menu
        const langBtn = event.target.closest("[data-action='toggle-language']");
        if (langBtn) {
            const menu = document.getElementById("language-menu");
            if (menu) menu.classList.toggle("hidden");
            return;
        }

        // Toggle Dark Mode
        const themeBtn = event.target.closest("[data-action='toggle-theme']");
        if (themeBtn) {
            const html = document.documentElement;
            if (html.classList.contains("dark")) {
                html.classList.remove("dark");
                localStorage.setItem("theme", "light");
            } else {
                html.classList.add("dark");
                localStorage.setItem("theme", "dark");
            }
            return;
        }

        // Close Alert Messages
        const dismissBtn = event.target.closest("[data-action='dismiss-alert']");
        if (dismissBtn) {
            const alertBox = dismissBtn.closest("[data-alert]");
            if (alertBox) alertBox.remove();
            return;
        }

        // Close Lightbox
        const closeLightboxBtn = event.target.closest("[data-action='close-lightbox']");
        if (closeLightboxBtn) {
            closeGalleryModal();
            return;
        }

        // Close Language Dropdown on Outside Click
        const langMenu = document.getElementById("language-menu");
        if (langMenu && !langMenu.contains(event.target) && !langBtn) {
            langMenu.classList.add("hidden");
        }
    });
});

// Lightbox Helper Functions
function openGalleryModal(imageSrc, title = "", caption = "") {
    const modal = document.getElementById("gallery-lightbox");
    const img = document.getElementById("lightbox-image");
    const titleEl = document.getElementById("lightbox-title");
    const captionEl = document.getElementById("lightbox-caption");

    if (modal && img && titleEl && captionEl) {
        img.src = imageSrc;
        titleEl.textContent = title;
        captionEl.textContent = caption;
        modal.classList.remove("hidden");
    }
}

function closeGalleryModal() {
    const modal = document.getElementById("gallery-lightbox");
    const img = document.getElementById("lightbox-image");

    if (modal && img) {
        modal.classList.add("hidden");
        img.src = "";
    }
}