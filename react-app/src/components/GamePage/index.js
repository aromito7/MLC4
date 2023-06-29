//const Player = require("./player");
import Player from './player.js'
import Modal from './modal.js'
import './style.css'
import { useState, useEffect } from "react";


const ROWS = 6;
const COLS = 7;
const display = Array(ROWS).fill().map(col => Array(COLS).fill(' '))
const colors = {
  'B': 'black',
  'R': 'red',
  'G': 'grey',
  'P': 'pink',
  ' ': 'empty'
}


const Grid = () => {
  //console.log("Rerendering Grid")
  //console.log(display)
  return (
    <div id="grid">
      {
        Array(ROWS * COLS).fill().map((r, val) =>{
          const y = Math.floor(val / COLS)
          const x = val % COLS
          const color = display[y][x]
          return <Square val={color} key={val} id={`${x},${y}`}/>
        })
      }
    </div>
  )
}
const DropButtons = () => {

}

const Square = ({val}) => {
  const color = colors[val];
  // console.log("Rerendering square:")
  // console.log(x, y, val)

  return <div className={`square ${color}`}/>
}

const GameBoard = () => {
  const [currentPlayer, setCurrentPlayer] = useState(1)
  const [active, setActive] = useState(Array(COLS).fill(5))
  const [hover, setHover] = useState(-1)
  const [isGameOver, setIsGameOver] = useState(false)
  const [isModalOpen, setIsModalOpen] = useState(false)
  const opponent = []

  function toggleModal(){

  }

  function resetGame(){
    console.log("Resetting Game...")
    for(let y in display){
      display[y] = Array(COLS).fill(' ')
    }
    setCurrentPlayer(1)
    setActive(Array(COLS).fill(5))
  }


  function startGame() {
    console.log("Start Game...")
    const start = document.getElementById("start");
    start.innerHTML = "NEW GAME";
    setIsGameOver(false)
    resetGame()
  }




  function checkForWin([x, y], board, player){
    const chain = Player.longestChainAtLocation([x, y], board, player)
    return chain >= 3? 1 : 0
  }

  function endGame(player){
    isGameOver = true
    const dropButtons = document.querySelectorAll(".dropButton")
    const endMessage = document.getElementById("endGame")
    endMessage.innerText = player === 2 ? "You Lose!" : "You Win"
    //endMessage.setAttribute("display", "visible")
    dropButtons.forEach(child => child.style.visibility = "hidden")
  }

  const columnDrop = function(player, column){
    console.log(`Column drop.  Player: ${player}, Column: ${column}`)
    //if(currentPlayer && currentPlayer !== player) return
    const [y, x] = [active[column], column]
    console.log(`Hello Player ${player}.  You've selected ${x}, ${y}`)
    display[y][x] = player === 1 ? "B" : "R"
    setHover(-1)
    setCurrentPlayer(3 - currentPlayer)

    return[column, active[column]--]
  }

  const columnHover = function(player, column){
    if(isGameOver) return
    console.log(player, column)
    changeHover(column)
  }

  const changeHover = function(column){
    console.log(`Changing hover from column ${hover} to ${column}`)
    if(hover >= 0){
      console.log("Resetting old hover : ", active[hover], hover, column)
      display[active[hover]][hover] = ' '
    }
    setHover(column)
    if(column>=0){
      display[active[column]][column] = currentPlayer === 1 ? 'G' : 'P'
    }
  }

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
              className={`dropButton ${currentPlayer === 1? 'hoverBlack' : 'hoverRed'}`}
              onClick={e => columnDrop(currentPlayer, x)}
              onMouseOver={e => columnHover(1, x)}
              onMouseLeave={e => changeHover(-1)}
              />
            )
          })
        }
        </div>
        <Grid/>
        <div className="toolbar">
          <button id="start" className="off" onClick={() => startGame()}>NEW GAME</button>
          <button id='options' onClick={e => setIsModalOpen(true)}>Options</button>
          {/* <button id="clear">PLAY AI</button>
          <button id="next">PLAY ML</button> */}

        </div>
      </div>
      <Modal isModalOpen={isModalOpen} setIsModalOpen={setIsModalOpen}/>
    </div>
  )
}

export default GameBoard

// window.onload = initialize;
