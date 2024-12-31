// Footnotes stuff
const footnotesEl = document.querySelector(".footnotes");
if (footnotesEl) {
    const footnotesTitleEl = footnotesEl.querySelector(".title");
    const footnotesTitleSVGEl = footnotesTitleEl.querySelector("svg");
    const footnotesListEl = footnotesEl.querySelector(".list");
    let footnotesActive = false;
    
    footnotesTitleEl.addEventListener("click", () => {
        if (!footnotesActive) {
            footnotesActive = true;
            footnotesTitleSVGEl.setAttribute("active", "")
            footnotesListEl.setAttribute("active", "")
        } else{
            footnotesActive = false;
            footnotesTitleSVGEl.removeAttribute("active");
            footnotesListEl.removeAttribute("active");
        }
    })
    
    footnotesTitleEl.addEventListener("mouseover", () => {
        footnotesTitleEl.style.cursor = "pointer";
    });
    
    footnotesTitleEl.addEventListener("mouseout", () => {
        footnotesTitleEl.style.cursor = "default";
    });
}
