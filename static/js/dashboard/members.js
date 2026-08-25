document.addEventListener("DOMContentLoaded", function () {
    // Input elements
    const fileInput = document.querySelector('input[type="file"][name$="photo"]');
    const photoPreviewContainer = document.getElementById('photo-preview-container');
    const photoPreviewImg = document.getElementById('photo-preview-img');
    const noPhotoPlaceholder = document.getElementById('no-photo-placeholder');
    const removePhotoBtn = document.getElementById('remove-photo-btn');
    const fileInfo = document.getElementById('file-info');

    const cardPreviewImg = document.getElementById('card-preview-img');
    const cardPreviewIcon = document.getElementById('card-preview-icon');
    const cardPreviewName = document.getElementById('card-preview-name');
    const cardPreviewRole = document.getElementById('card-preview-role');

    const nameInput = document.querySelector('.member-name-input');
    const nameArInput = document.querySelector('.member-name-ar-input');
    const roleEnInput = document.querySelector('.member-role-en-input');
    const roleArInput = document.querySelector('.member-role-ar-input');
    const roleFrInput = document.querySelector('.member-role-fr-input');

    const submitBtn = document.getElementById('submit-btn');
    const memberForm = document.getElementById('member-form');

    // Fallback translation texts from DOM data attributes
    const defaultNameText = cardPreviewName ? cardPreviewName.dataset.defaultText || 'Member Name' : 'Member Name';
    const defaultRoleText = cardPreviewRole ? cardPreviewRole.dataset.defaultText || 'Role / Position' : 'Role / Position';

    // Dynamic Name Preview
    function updateNamePreview() {
        if (!cardPreviewName) return;
        const primary = nameInput ? nameInput.value.trim() : '';
        const arabic = nameArInput ? nameArInput.value.trim() : '';
        cardPreviewName.textContent = primary || arabic || defaultNameText;
    }

    if (nameInput) nameInput.addEventListener('input', updateNamePreview);
    if (nameArInput) nameArInput.addEventListener('input', updateNamePreview);

    // Dynamic Role Preview (EN -> AR -> FR)
    function updateRolePreview() {
        if (!cardPreviewRole) return;
        const en = roleEnInput ? roleEnInput.value.trim() : '';
        const ar = roleArInput ? roleArInput.value.trim() : '';
        const fr = roleFrInput ? roleFrInput.value.trim() : '';
        cardPreviewRole.textContent = en || ar || fr || defaultRoleText;
    }

    if (roleEnInput) roleEnInput.addEventListener('input', updateRolePreview);
    if (roleArInput) roleArInput.addEventListener('input', updateRolePreview);
    if (roleFrInput) roleFrInput.addEventListener('input', updateRolePreview);

    // Image Upload & Preview Handler
    function handleFile(file) {
        if (file && photoPreviewImg && cardPreviewImg) {
            const url = URL.createObjectURL(file);
            photoPreviewImg.src = url;
            cardPreviewImg.src = url;

            if (photoPreviewContainer) photoPreviewContainer.classList.remove('hidden');
            cardPreviewImg.classList.remove('hidden');
            if (noPhotoPlaceholder) noPhotoPlaceholder.classList.add('hidden');
            if (cardPreviewIcon) cardPreviewIcon.classList.add('hidden');

            if (fileInfo) {
                fileInfo.textContent = `${file.name} (${(file.size / (1024 * 1024)).toFixed(2)} MB)`;
                fileInfo.classList.remove('hidden');
            }
        }
    }

    if (fileInput) {
        fileInput.addEventListener('change', (e) => {
            if (e.target.files && e.target.files[0]) {
                handleFile(e.target.files[0]);
            }
        });
    }

    if (removePhotoBtn) {
        removePhotoBtn.addEventListener('click', () => {
            if (fileInput) fileInput.value = '';
            if (photoPreviewImg) photoPreviewImg.src = '';
            if (cardPreviewImg) cardPreviewImg.src = '';

            if (photoPreviewContainer) photoPreviewContainer.classList.add('hidden');
            if (cardPreviewImg) cardPreviewImg.classList.add('hidden');
            if (noPhotoPlaceholder) noPhotoPlaceholder.classList.remove('remove', 'hidden');
            if (cardPreviewIcon) cardPreviewIcon.classList.remove('hidden');

            if (fileInfo) {
                fileInfo.textContent = '';
                fileInfo.classList.add('hidden');
            }
        });
    }

    // Drag-and-Drop Dropzone Functionality
    const dropzone = document.getElementById('dropzone');
    if (dropzone && fileInput) {
        ['dragover', 'dragenter'].forEach(eventName => {
            dropzone.addEventListener(eventName, (e) => {
                e.preventDefault();
                dropzone.classList.add('border-purple-500');
            });
        });

        ['dragleave', 'drop'].forEach(eventName => {
            dropzone.addEventListener(eventName, (e) => {
                e.preventDefault();
                dropzone.classList.remove('border-purple-500');
            });
        });

        dropzone.addEventListener('drop', (e) => {
            const files = e.dataTransfer.files;
            if (files.length > 0) {
                fileInput.files = files;
                handleFile(files[0]);
            }
        });
    }

    // Header Submit Button Binding
    if (submitBtn && memberForm) {
        submitBtn.addEventListener('click', () => {
            memberForm.submit();
        });
    }
});