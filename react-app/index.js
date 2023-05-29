//const Player = require("./player");

const ROWS = 6;
const COLS = 7;

let display = []
let board
let active

let INTERVAL_POINTER = null;

let opponent
let currentPlayer = 1
let gameOver = false
let previousHover

function initialize() {
  buildGrid();
  initDropButtons();
  initButtons();
  board = Array(ROWS).fill().map(col => Array(COLS).fill(0))
  active = Array(COLS).fill(5)
  opponent = new Player(1, 2)

}

function resetGame(){
  document.querySelectorAll(".dropButton").forEach(child => child.style.visibility = "visible")
  document.getElementById("endGame").innerText = ""
  board = Array(ROWS).fill().map(col => Array(COLS).fill(0))
  active = Array(COLS).fill(5)
  const grid = document.getElementById("grid");
  for (let y = 0; y < ROWS; y++) {
    for (let x = 0; x < COLS; x++) {
      const current = document.getElementById(`${x},${y}`);
      current.setAttribute("class", "empty");
    }
  }
}

function clearScreen() {
  for (let y = 0; y < ROWS; y++) {
    for (let x = 0; x < COLS; x++) {
      const current = document.getElementById(`${x},${y}`);
      current.setAttribute("class", "dead");
    }
  }
}

function startGame() {
  const start = document.getElementById("start");
  start.innerHTML = "NEW GAME";
  gameOver = false
  resetGame()
}


function initButtons() {
  //const clear = document.getElementById("clear");
  //const next = document.getElementById("next");
  const start = document.getElementById("start");
  start.addEventListener("click", () => startGame());
  //clear.addEventListener("click", () => clearScreen());
  //  next.addEventListener("click", () => nextState());
}

function checkForWin([x, y], board, player){
  const chain = Player.longestChainAtLocation([x, y], board, player)
  //console.log(chain, [x,y], board, player)

  return chain >= 3? 1 : 0
}

function endGame(player){
  gameOver = true
  const dropButtons = document.querySelectorAll(".dropButton")
  const endMessage = document.getElementById("endGame")
  endMessage.innerText = player === 2 ? "You Lose!" : "You Win"
  //endMessage.setAttribute("display", "visible")
  dropButtons.forEach(child => child.style.visibility = "hidden")
}

const pressButton = function(player, column){
  //console.log(column, active[column], board)
  //board[active[column]][column].setAttribute("class", player === 1 ? "black" : "red")
  return () => {
    if(gameOver) return
    let recentMove = columnDrop(player, column)
    if(checkForWin(recentMove, board, 1)){
      endGame(1)
      return
    }
    recentMove = columnDrop(currentPlayer, opponent.decide(board, active))
    if(checkForWin(recentMove, board, 2)){
      endGame(2)
      return
    }
  }
}

const columnDrop = function(player, column){
  if(currentPlayer && currentPlayer !== player) return
  const [y, x] = [active[column], column]
  //console.log(`Hello Player ${player}.  You've selected ${x}, ${y}`)
  display[y][x].setAttribute("class", player === 1 ? "black" : "red")
  board[y][x] = player
  previousHover = null
  currentPlayer = 3 - currentPlayer

  return [x, active[column]--]
}

const columnHover = function(player, column){
  return () => {
    if(gameOver) return
    const [y , x] = [active[column], column]
    display[y][x].setAttribute("class", player === 1 ? "grey" : "pink")
    if(previousHover) previousHover.setAttribute("class", "empty")
    previousHover = display[y][x]
  }
}

function buildGrid() {
  const grid = document.getElementById("grid");
  for (let y = 0; y < ROWS; y++) {
    const row = []
    for (let x = 0; x < COLS; x++) {
      const cell = document.createElement("div");
      cell.setAttribute("class", "empty");
      cell.setAttribute("id", `${x},${y}`);
      //cell.addEventListener("click", pressButton(currentPlayer, x))
      grid.appendChild(cell);
      row.push(cell)
    }
    display.push(row)
  }
  //display = display.reverse()
  //console.log(board)
}

function initDropButtons(){
  const buttonRow = document.getElementById("dropButtons");
  for(let x = 0; x < COLS; x++){
    const button = document.createElement("button")
    button.setAttribute("class", "dropButton")
    button.setAttribute("id", x)
    button.addEventListener("click", pressButton(1, x));
    button.addEventListener("mouseover", columnHover(1, x));
    buttonRow.appendChild(button)
    console.log(`Building button ${x}`)
  }
}

window.onload = initialize;
