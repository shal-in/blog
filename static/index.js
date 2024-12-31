const essayPreviewEls = document.querySelectorAll(".essay-preview");

essayPreviewEls.forEach(essayPreviewEl => {
    let titleEl = essayPreviewEl.querySelector(".title");
    let metadataEl = essayPreviewEl.querySelector(".metadata");
    let textEl = essayPreviewEl.querySelector(".text-container");
    essayPreviewEl.addEventListener("mouseover", () => {
        titleEl.style.color = "gray";
        metadataEl.style.color = "gray";
        textEl.style.color = "gray";

        essayPreviewEl.style.cursor = "pointer";
    })

    essayPreviewEl.addEventListener("mouseout", () => {
        titleEl.style.color = "black";
        metadataEl.style.color = "black";
        textEl.style.color = "black";
    })
})