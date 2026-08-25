document.addEventListener("DOMContentLoaded", function () {
    // 1. Refresh Lucide Icons
    if (window.lucide) {
        lucide.createIcons();
    }

    // 2. Submit Button Handler
    const submitBtn = document.getElementById("submit-btn");
    const activityForm = document.getElementById("activity-form");
    if (submitBtn && activityForm) {
        submitBtn.addEventListener("click", function () {
            activityForm.submit();
        });
    }

    // 3. Featured Cover Image Dropzone & Preview Handlers
    const photoInput = document.querySelector('input[type="file"][name$="featured_image"]');
    const previewContainer = document.getElementById("photo-preview-container");
    const previewImg = document.getElementById("photo-preview-img");
    const placeholder = document.getElementById("no-photo-placeholder");
    const removeBtn = document.getElementById("remove-photo-btn");
    const fileInfo = document.getElementById("file-info");

    // Live Sidebar elements
    const cardPreviewImg = document.getElementById("card-preview-img");
    const cardPreviewIcon = document.getElementById("card-preview-icon");

    if (photoInput) {
        photoInput.addEventListener("change", function () {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    if (previewImg) previewImg.src = e.target.result;
                    if (previewContainer) previewContainer.classList.remove("hidden");
                    if (placeholder) placeholder.classList.add("hidden");

                    if (cardPreviewImg) {
                        cardPreviewImg.src = e.target.result;
                        cardPreviewImg.classList.remove("hidden");
                    }
                    if (cardPreviewIcon) cardPreviewIcon.classList.add("hidden");
                };
                reader.readAsDataURL(file);

                if (fileInfo) {
                    fileInfo.textContent = file.name;
                    fileInfo.classList.remove("hidden");
                }
            }
        });
    }

    if (removeBtn) {
        removeBtn.addEventListener("click", function (e) {
            e.preventDefault();
            if (photoInput) photoInput.value = "";
            if (previewContainer) previewContainer.classList.add("hidden");
            if (placeholder) placeholder.classList.remove("hidden");
            if (fileInfo) fileInfo.classList.add("hidden");

            if (cardPreviewImg) cardPreviewImg.classList.add("hidden");
            if (cardPreviewIcon) cardPreviewIcon.classList.remove("hidden");
        });
    }

    // 4. Dynamic Gallery Formset Handler
    const addGalleryBtn = document.getElementById("add-gallery-btn");
    const galleryWrapper = document.getElementById("gallery-wrapper");
    const galleryTotal = document.getElementById("id_gallery-TOTAL_FORMS");
    const galleryTemplate = document.getElementById("gallery-empty-template");

    if (addGalleryBtn && galleryWrapper && galleryTotal && galleryTemplate) {
        addGalleryBtn.addEventListener("click", function () {
            const count = parseInt(galleryTotal.value, 10);
            const content = galleryTemplate.innerHTML.replace(/__prefix__/g, count);
            galleryWrapper.insertAdjacentHTML("beforeend", content);
            galleryTotal.value = count + 1;
            if (window.lucide) lucide.createIcons();
        });
    }

    // 5. Dynamic Block Formset Event Delegation
    document.addEventListener("click", function (e) {
        // Add Block
        const addBlockBtn = e.target.closest("[data-add-block]");
        if (addBlockBtn) {
            const prefix = addBlockBtn.getAttribute("data-add-block");
            const totalInput = document.getElementById("id_" + prefix + "-TOTAL_FORMS");
            const container = document.getElementById("blocks-wrapper-" + prefix);
            const template = document.getElementById("block-template-" + prefix);

            if (totalInput && container && template) {
                const count = parseInt(totalInput.value, 10);
                const content = template.innerHTML.replace(/__prefix__/g, count);
                container.insertAdjacentHTML("beforeend", content);
                totalInput.value = count + 1;
                if (window.lucide) lucide.createIcons();
            }
        }

        // Remove Block / Card
        const removeCardBtn = e.target.closest("[data-remove-card]");
        if (removeCardBtn) {
            const card = removeCardBtn.closest(".block-form-card, .gallery-card");
            if (card) card.remove();
        }
    });

    // 6. Live Text Preview Syncing
    const titleInputs = document.querySelectorAll('input[name$="-title"]');
    const locationInput = document.querySelector('input[name="location"]');
    const cardTitle = document.getElementById("card-preview-title");
    const cardLocation = document.getElementById("card-preview-location");

    titleInputs.forEach(input => {
        input.addEventListener("input", function () {
            if (cardTitle && this.value.trim() !== "") {
                cardTitle.textContent = this.value;
            }
        });
    });

    if (locationInput && cardLocation) {
        locationInput.addEventListener("input", function () {
            const span = cardLocation.querySelector("span");
            if (span) span.textContent = this.value || "Location";
        });
    }
});