const essayPreviewEls = document.querySelectorAll(".essay-preview");

essayPreviewEls.forEach(essayPreviewEl => {
    let titleContainerEl = essayPreviewEl.querySelector(".title-container");
    let titleSVGEl = titleContainerEl.querySelector("svg");
    let textContainerEl = essayPreviewEl.querySelector(".text-container");

    titleContainerEl.addEventListener("click", () => {
        showEssayPreview(essayPreviewEl);
    });
    
    essayPreviewEl.addEventListener("keydown", (event) => {
        if (document.activeElement === essayPreviewEl) {
            if (event.key === "Enter" && titleSVGEl.classList.contains("active")){
                textContainerEl.click();
            }
            else if (event.key === "Enter" || event.key === " ") {
                event.preventDefault();
                showEssayPreview(essayPreviewEl);
            }
        }
    })

});

function showEssayPreview(essayPreviewEl) {
    const titleContainerEl = essayPreviewEl.querySelector(".title-container");
    const titleSVGEl = titleContainerEl.querySelector("svg");
    const textContainerEl = essayPreviewEl.querySelector(".text-container");

    titleSVGEl.classList.toggle("active");

    if (textContainerEl.classList.contains("active")) {
        // Collapse
        textContainerEl.style.maxHeight = textContainerEl.scrollHeight + "px"; // Set to scrollHeight first
        requestAnimationFrame(() => {
            textContainerEl.style.maxHeight = "0"; // Then collapse
            textContainerEl.style.opacity = 0;
        });
        textContainerEl.classList.remove("active");
    } else {
        // Expand
        textContainerEl.style.maxHeight = "0"; // Set to 0 first
        textContainerEl.style.opacity = 0; // Make sure it's hidden
        requestAnimationFrame(() => {
            textContainerEl.style.maxHeight = textContainerEl.scrollHeight + "px"; // Expand smoothly
            textContainerEl.style.opacity = 1;
        });
        textContainerEl.classList.add("active");
    }
}


const sortEl = document.querySelector(".sort");
const newestEl = sortEl.querySelector(".newest");
const oldestEl = sortEl.querySelector(".oldest");
const previewListEl = document.querySelector(".preview-list");

newestEl.addEventListener("click", () => {
    console.log("newest");
    if (previewListEl.classList.contains("oldest")) {
        previewListEl.classList.remove("oldest");

        newestEl.classList.toggle("active");
        oldestEl.classList.toggle("active");
    }
})

oldestEl.addEventListener("click", () => {
    console.log("oldest");
    if (!previewListEl.classList.contains("oldest")) {
        previewListEl.classList.add("oldest");

        newestEl.classList.toggle("active");
        oldestEl.classList.toggle("active");
    }
})