const COLOURS = [
  "black",
  "white",
  "red",
  "green",
  "blue",
  "orange",
  "brown",
  "pink",
]

const boardContainer = document.getElementById("board-container")
let board = []

function addRow() {
  row = []
  for (let i = 0; i < 5; i++) {
    row.push(Math.floor(Math.random() * 7))
  }
  board.push(row)
  updateBoard(boardContainer, 50)
}

function updateOpponentStatus() {
  
}

function updateBoard(boardEl, size) {
  boardHTML = ""
  for (let row of board) {
    rowHTML = ""
    for (let piece of row) {
      rowHTML += `<div class="piece" style="background-color: ${COLOURS[piece]}; width: ${size}px; height: ${size}px;"></div>`
    }
    boardHTML += `<div class="row">${rowHTML}</div>`
  }
  boardEl.innerHTML = boardHTML
}
