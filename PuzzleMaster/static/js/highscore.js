// static/js/highscore.js

document.addEventListener("DOMContentLoaded", () => {
    console.log("High Score page loaded.");

    const buttons = document.querySelectorAll(".category-button");
    const rows = Array.from(document.querySelectorAll("#score-body tr"));
    const sortBtn = document.getElementById("toggle-sort");

    let currentSort = defaultSort || "duration";
    let currentFilter = defaultDifficulty || "3x3";

    function updateButtonStates() {
        buttons.forEach(btn => {
            btn.classList.toggle("selected", btn.dataset.filter === currentFilter);
        });
        sortBtn.textContent = `Sort by ${currentSort === "moves" ? "Duration" : "Moves"}`;
    }

    function applyFilter() {
        rows.forEach(row => {
            const difficulty = row.dataset.difficulty;
            row.style.display = (difficulty === currentFilter) ? "" : "none";
        });
    }

    updateButtonStates();
    applyFilter();

    // === Difficulty button click ===
    buttons.forEach(btn => {
        btn.addEventListener("click", () => {
            const difficulty = btn.dataset.filter;
            window.location.href = `/highscore/${difficulty}?sort=${currentSort}`;
        });
    });

    // === Sort toggle click ===
    sortBtn.addEventListener("click", () => {
        const newSort = currentSort === "moves" ? "duration" : "moves";
        window.location.href = `/highscore/${currentFilter}?sort=${newSort}`;
    });
});
