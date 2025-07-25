// static/js/puzzle_settings.js

document.addEventListener("DOMContentLoaded", () => {
    console.log("Puzzle Settings page loaded.");

    // === IMAGE SELECTION ===
    const images = document.querySelectorAll(".selectable-image");
    images.forEach(img => {
        img.addEventListener("click", () => {
            images.forEach(i => i.classList.remove("selected"));
            img.classList.add("selected");
            sessionStorage.setItem("selectedImage", img.dataset.image);
            renderPreview();
        });
    });

    // === GRID SELECTION ===
    const gridButtons = document.querySelectorAll(".grid-button");
    gridButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            gridButtons.forEach(b => b.classList.remove("selected"));
            btn.classList.add("selected");
            sessionStorage.setItem("selectedGrid", btn.dataset.grid);
            renderPreview();
        });
    });

    // === START BUTTON ===
    const startBtn = document.querySelector(".start-button");
    if (startBtn) {
        startBtn.addEventListener("click", async () => {
            const image = sessionStorage.getItem("selectedImage");
            const grid = sessionStorage.getItem("selectedGrid");

            if (!image || !grid) {
                alert("Please select an image and a grid size.");
                return;
            }

            try {
                const response = await fetch("/start_game", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ image, grid })
                });

                const result = await response.json();
                if (result.redirect_url) {
                    const sessionID = result.redirect_url.split("/").pop();
                    sessionStorage.setItem("sessionID", sessionID);
                    window.location.href = result.redirect_url;
                } else {
                    alert("Failed to start game.");
                }
            } catch (error) {
                console.error("Error starting game:", error);
            }
        });
    }

    // === PREVIEW RENDER ===
    function renderPreview() {
        const selectedImg = document.querySelector(".selectable-image.selected");
        const selectedGrid = document.querySelector(".grid-button.selected");
        const previewBox = document.getElementById("preview-area");

        if (!previewBox) return;

        if (!selectedImg || !selectedGrid) {
            previewBox.innerHTML = `<div><em>Select image and grid to see preview</em></div>`;
            return;
        }

        const [cols, rows] = selectedGrid.dataset.grid.split("x").map(Number);
        const src = selectedImg.getAttribute("src");

        previewBox.innerHTML = `
            <div class="preview-grid" style="
            display: grid;
            grid-template-columns: repeat(${cols}, 50px);
            grid-template-rows: repeat(${rows}, 50px);
            gap: 2px;
            margin-top: 10px;
            ">
            ${generateTiles(cols, rows, src)}
            </div>
        `;

    }

    // === TILE PREVIEW BUILDER ===
    function generateTiles(cols, rows, src) {
        let tiles = "";
        for (let row = 0; row < rows; row++) {
            for (let col = 0; col < cols; col++) {
                const x = (col * 100) / (cols - 1);
                const y = (row * 100) / (rows - 1);

                tiles += `
                    <div class="tile" style="
                        background-image: url('${src}');
                        background-size: ${cols * 100}% ${rows * 100}%;
                        background-position: ${x}% ${y}%;
                    "></div>
                `;
            }
        }
        return tiles;
    }


    // === INIT ===
    renderPreview();
});
