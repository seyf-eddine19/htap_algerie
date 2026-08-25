document.addEventListener("DOMContentLoaded", () => {
    const categoryModal = document.getElementById("category-modal");
    const deleteModal = document.getElementById("delete-modal");
    const categoryForm = document.getElementById("category-form");

    const categoryAction = document.getElementById("category-action");
    const categoryId = document.getElementById("category-id");
    const categoryName = document.getElementById("category-name");
    const categorySlug = document.getElementById("category-slug");
    const categoryOrder = document.getElementById("category-order");
    const categoryActive = document.getElementById("category-active");

    const modalTitle = document.getElementById("category-modal-title");
    const modalDescription = document.getElementById("category-modal-description");
    const submitText = document.querySelector("#category-submit span");

    const deleteCategoryId = document.getElementById("delete-category-id");
    const deleteCategoryName = document.getElementById("delete-category-name");

    function openModal(modal) {
        if (!modal) {
            return;
        }

        modal.classList.remove("hidden");
        modal.classList.add("flex");
        document.body.classList.add("overflow-hidden");
    }

    function closeModal(modal) {
        if (!modal) {
            return;
        }

        modal.classList.add("hidden");
        modal.classList.remove("flex");

        if (
            categoryModal &&
            deleteModal &&
            categoryModal.classList.contains("hidden") &&
            deleteModal.classList.contains("hidden")
        ) {
            document.body.classList.remove("overflow-hidden");
        }
    }

    function resetCategoryForm() {
        if (!categoryForm) {
            return;
        }

        categoryForm.reset();

        if (categoryAction) {
            categoryAction.value = "create";
        }

        if (categoryId) {
            categoryId.value = "";
        }

        if (categoryOrder) {
            categoryOrder.value = "0";
        }

        if (categoryActive) {
            categoryActive.checked = true;
        }
    }

    function openCreateModal() {
        resetCategoryForm();

        if (modalTitle) {
            modalTitle.textContent = modalTitle.dataset.createTitle || "Add Category";
        }

        if (modalDescription) {
            modalDescription.textContent = modalDescription.dataset.createDescription || "Create a new article category.";
        }

        if (submitText) {
            submitText.textContent = submitText.dataset.createText || "Save Category";
        }

        openModal(categoryModal);

        if (categoryName) {
            categoryName.focus();
        }
    }

    function openEditModal(button) {
        resetCategoryForm();

        const id = button.dataset.id || "";
        const name = button.dataset.name || "";
        const slug = button.dataset.slug || "";
        const order = button.dataset.order || "0";
        const active = button.dataset.active === "true";

        if (categoryAction) {
            categoryAction.value = "update";
        }

        if (categoryId) {
            categoryId.value = id;
        }

        if (categoryName) {
            categoryName.value = name;
        }

        if (categorySlug) {
            categorySlug.value = slug;
        }

        if (categoryOrder) {
            categoryOrder.value = order;
        }

        if (categoryActive) {
            categoryActive.checked = active;
        }

        if (modalTitle) {
            modalTitle.textContent = modalTitle.dataset.editTitle || "Edit Category";
        }

        if (modalDescription) {
            modalDescription.textContent = modalDescription.dataset.editDescription || "Update this article category.";
        }

        if (submitText) {
            submitText.textContent = submitText.dataset.editText || "Update Category";
        }

        openModal(categoryModal);

        if (categoryName) {
            categoryName.focus();
        }
    }

    function openDeleteModal(button) {
        const id = button.dataset.id || "";
        const name = button.dataset.name || "";

        if (deleteCategoryId) {
            deleteCategoryId.value = id;
        }

        if (deleteCategoryName) {
            deleteCategoryName.textContent = name;
        }

        openModal(deleteModal);
    }

    function closeCategoryModal() {
        closeModal(categoryModal);
    }

    function closeDeleteModal() {
        closeModal(deleteModal);
    }

    document.querySelectorAll("[data-action='open-create']").forEach((button) => {
        button.addEventListener("click", openCreateModal);
    });

    document.querySelectorAll("[data-action='open-edit']").forEach((button) => {
        button.addEventListener("click", () => {
            openEditModal(button);
        });
    });

    document.querySelectorAll("[data-action='open-delete']").forEach((button) => {
        button.addEventListener("click", () => {
            openDeleteModal(button);
        });
    });

    document.querySelectorAll("[data-action='close-category-modal']").forEach((button) => {
        button.addEventListener("click", closeCategoryModal);
    });

    document.querySelectorAll("[data-action='close-delete-modal']").forEach((button) => {
        button.addEventListener("click", closeDeleteModal);
    });

    categoryModal?.addEventListener("click", (event) => {
        if (event.target === categoryModal) {
            closeCategoryModal();
        }
    });

    deleteModal?.addEventListener("click", (event) => {
        if (event.target === deleteModal) {
            closeDeleteModal();
        }
    });

    document.addEventListener("keydown", (event) => {
        if (event.key !== "Escape") {
            return;
        }

        closeCategoryModal();
        closeDeleteModal();
    });

    if (categoryForm && categoryAction) {
        categoryForm.addEventListener("submit", () => {
            const submitButton = document.getElementById("category-submit");

            if (submitButton) {
                submitButton.disabled = true;
                submitButton.classList.add("opacity-70", "cursor-not-allowed");
            }
        });
    }

    const searchInput = document.querySelector("input[name='q']");

    if (searchInput) {
        searchInput.addEventListener("keydown", (event) => {
            if (event.key === "Escape") {
                searchInput.value = "";
            }
        });
    }
});