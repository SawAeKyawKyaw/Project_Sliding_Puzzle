// static/js/puzzle_play.js

document.addEventListener("DOMContentLoaded", () => {
  const gridContainer = document.getElementById("puzzle-grid");
  const movesDisplay = document.getElementById("moves");
  const resetBtn = document.getElementById("reset-btn");
  const timeDisplay = document.getElementById("time");

  const [rows, cols] = gridSize.split("x").map(Number);

  let board = [];
  let emptyTile = { row: 0, col: 0 };
  let moveCount = 0;

  let elapsedSeconds = 0;
  let timerInterval;

  gridContainer.style.gridTemplateColumns = `repeat(${cols}, 80px)`;
  gridContainer.style.gridTemplateRows = `repeat(${rows}, 80px)`;

  function initBoard() {
    let n = 1;
    board = [];
    for (let r = 0; r < rows; r++) {
      const row = [];
      for (let c = 0; c < cols; c++) {
        row.push(n++);
      }
      board.push(row);
    }
    board[0][0] = null;
    emptyTile = { row: 0, col: 0 };
    moveCount = 0;

    // Timer reset
    clearInterval(timerInterval);
    elapsedSeconds = 0;
    updateTimerDisplay();
    timerInterval = setInterval(() => {
      elapsedSeconds++;
      updateTimerDisplay();
    }, 1000);

    updateUI();
    shuffleBoard(200);
  }

  function shuffleBoard(times) {
    for (let i = 0; i < times; i++) {
      const { row, col } = emptyTile;
      const neighbors = getMovableTiles(row, col);
      const rand = neighbors[Math.floor(Math.random() * neighbors.length)];
      moveTile(rand.row, rand.col, true);
    }
    moveCount = 0;
    updateUI();
  }

  function getMovableTiles(r, c) {
    const moves = [];
    if (r > 0) moves.push({ row: r - 1, col: c });
    if (r < rows - 1) moves.push({ row: r + 1, col: c });
    if (c > 0) moves.push({ row: r, col: c - 1 });
    if (c < cols - 1) moves.push({ row: r, col: c + 1 });
    return moves;
  }

  function moveTile(r, c, silent = false) {
    const { row: er, col: ec } = emptyTile;
    const isAdjacent =
      (r === er && Math.abs(c - ec) === 1) ||
      (c === ec && Math.abs(r - er) === 1);
    if (!isAdjacent) return;

    board[er][ec] = board[r][c];
    board[r][c] = null;
    emptyTile = { row: r, col: c };

    if (!silent) {
      moveCount++;
      updateUI();
      if (checkWin()) {
        clearInterval(timerInterval);

        // Prepare score data
        const scoreData = {
          duration: elapsedSeconds,
          moves: moveCount,
          session_id: sessionId 
        };

        console.log(scoreData)

        fetch('/submit_score', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(scoreData)
        })
        .then(response => {
          if (!response.ok) throw new Error("Failed to save score");
          return response.json();
        })
        .then(data => {
          window.location.href = `/highscore/${gridSize}?sort=duration`;
        })
        .catch(err => {
          alert("Could not save score: " + err.message);
        });
      }

    }
  }

  function updateUI() {
    gridContainer.innerHTML = '';
    movesDisplay.textContent = moveCount;

    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const val = board[r][c];
        const tile = document.createElement("div");
        tile.className = val === null ? "tile empty" : "tile";

        if (val !== null) {
          const index = val - 1;
          const srcCol = index % cols;
          const srcRow = Math.floor(index / cols);
          const x = (srcCol * 100) / (cols - 1);
          const y = (srcRow * 100) / (rows - 1);

          tile.style.backgroundImage = `url('${imageSrc}')`;
          tile.style.backgroundSize = `${cols * 100}% ${rows * 100}%`;
          tile.style.backgroundPosition = `${x}% ${y}%`;

          tile.addEventListener("click", () => moveTile(r, c));
        }

        gridContainer.appendChild(tile);
      }
    }
  }

  function updateTimerDisplay() {
    const minutes = String(Math.floor(elapsedSeconds / 60)).padStart(2, "0");
    const seconds = String(elapsedSeconds % 60).padStart(2, "0");
    timeDisplay.textContent = `${minutes}:${seconds}`;
  }

  function checkWin() {
    let expected = 2;
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        if (r === 0 && c === 0) {
          if (board[r][c] !== null) return false;
        } else {
          if (board[r][c] !== expected++) return false;
        }
      }
    }
    return true;
  }

  resetBtn.addEventListener("click", initBoard);
  initBoard();
});
