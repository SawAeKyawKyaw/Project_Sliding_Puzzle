// static/js/index.js

console.log("Main page loaded.");

document.addEventListener("DOMContentLoaded", () => {
    const playButton = document.getElementById("play-btn");
    const highScoreButton = document.getElementById("score-btn");

    playButton.addEventListener("click", () => {
        window.location.href = "/puzzle_settings";
    });

    highScoreButton.addEventListener("click", () => {
        window.location.href = "/highscore/3x3?sort=duration";
    });
});

