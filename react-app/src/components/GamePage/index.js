//const Player = require("./player");
import Player from './player.js'
import './style.css'
import { useState, useEffect } from "react";


const ROWS = 6;
const COLS = 7;

let display = Array(ROWS).fill().map(col => Array(COLS).fill(' '))
let board
let active = Array(COLS).fill(5)

let opponent
let currentPlayer = 1
let gameOver = false
let previousHover

// function initialize() {
//   // buildGrid();
//   initDropButtons();
//   board = Array(ROWS).fill().map(col => Array(COLS).fill(0))
//   active = Array(COLS).fill(5)
//   opponent = new Player(1, 2)
// }

function resetGame(){
  document.querySelectorAll(".dropButton").forEach(child => child.style.visibility = "visible")
  document.getElementById("endGame").innerText = ""
  // board = Array(ROWS).fill().map(col => Array(COLS).fill(0))
  // active = Array(COLS).fill(5)
//   const grid = document.getElementById("grid");
//   for (let y = 0; y < ROWS; y++) {
//     for (let x = 0; x < COLS; x++) {
//       const current = document.getElementById(`${x},${y}`);
//       current.setAttribute("class", "empty");
//     }
//   }
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


// function initButtons() {
//   //const clear = document.getElementById("clear");
//   //const next = document.getElementById("next");
//   const start = document.getElementById("start");
//   start.addEventListener("click", () => startGame());
//   //clear.addEventListener("click", () => clearScreen());
//   //  next.addEventListener("click", () => nextState());
// }

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
  console.log(`Column drop.  Player: ${player}, Column: ${column}`)
  //if(currentPlayer && currentPlayer !== player) return
  const [y, x] = [active[column], column]
  //console.log(`Hello Player ${player}.  You've selected ${x}, ${y}`)
  // display[y][x] = player === 1 ? "B" : "R"
  previousHover = null
  currentPlayer = 3 - currentPlayer

  active[column]--
}

const columnHover = function(player, column){
  console.log(player, column)
  return () => {
    if(gameOver) return
    const [y , x] = [active[column], column]
    display[y][x] = 'G'
  }
}


const Grid = () => {
  //console.log("Grid: ")
  return (
    <div id="grid">
      {
        Array(ROWS * COLS).fill().map((r, val) =>{
          const y = Math.floor(val / COLS)
          const x = val % COLS
          const color = display[y][x]
          return <Square x={x} y={y} val={color} key={val}/>
        })
      }
    </div>
  )
}


const Square = ({val, x, y}) => {
  let color;
  console.log(x, y, val)
  switch(val){
    case('G'):
      color = "grey"
      break
    case('R'):
      color = "red"
      break
    case('B'):
      color = "black"
      break
    case('P'):
      color = "pink"
      break
    default:
      color = "empty"
  }


  if(val === 'G') return <div class={`square grey`}/>
  if(val === 'R') return <div class={`square red`}/>
  if(val === 'B') return <div class={`square black`}/>
  if(val === 'P') return <div class={`square pink`}/>

  return <div class={`square empty`}/>
}

const GameBoard = () => {
  const [colors, setColors] = useState([])
  let display = Array(ROWS).fill().map(col => Array(COLS).fill(' '))
  return (
    <div id="container">
      <h1>Connect 4</h1>
      <div id="app">
        <p id="endGame"></p>
        <div id="dropButtons">
        {
          Array(COLS).fill().map((i, x) => {
            return(
              <button
              key={x}
              class="dropButton"
              onClick={e => columnDrop(1, x)}
              onmouseover={e => columnHover(1, x)}
                />
            )
          })
        }
        </div>
        <Grid/>
        <div class="toolbar">
          <button id="start" class="off" onClick={() => startGame()}>NEW GAME</button>

          {/* <button id="clear">PLAY AI</button>
          <button id="next">PLAY ML</button> */}

        </div>
      </div>
    </div>
  )
}

export default GameBoard

// window.onload = initialize;
