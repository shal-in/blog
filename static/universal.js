const linkEls = document.querySelectorAll(".link");

linkEls.forEach(linkEl => {
    let href = linkEl.getAttribute("href");

    linkEl.addEventListener("click", () => {
        window.location.href = href;
    })
})