//const Player = require("./player");
import Player from './player.js'
import Modal from './modal.js'
import './style.css'
import { useState, useEffect } from "react";


const ROWS = 6;
const COLS = 7;
const display = Array(ROWS).fill().map(col => Array(COLS).fill(' '))
const board = Array(ROWS).fill().map(col => Array(COLS).fill(0))
const colors = {
  'B': 'black',
  'R': 'red',
  'G': 'grey',
  'P': 'pink',
  ' ': 'empty'
}

const updateDisplayBoard = (y, x, color) => {
  display[y][x] = color

  if(color === 'B' || color === 'R'){
    board[y][x] = color === 'B' ? 1 : 2
  }
}

const Grid = () => {
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
  const [gameType, setGameType] = useState("pvai")


  function resetGame(){
    console.log("Resetting Game...")
    for(let y in display){
      display[y] = Array(COLS).fill(' ')
      board[y] = Array(COLS).fill(0)
    }
    setCurrentPlayer(1)
    setIsModalOpen(false)
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


  const botDecide = async(type) => {
    const response = await fetch(`/api/bot/ai/decide`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        board,
        active
      })
    });
    const data = await response.json()
    console.log(data)
    return data.move - 1
  }

  const pressButton = async function(player, column){
    if(currentPlayer === 1 || gameType === 'pvp'){
      columnDrop(player, column)
      if(gameType !== 'pvp'){
        const column = await botDecide(gameType)
        columnDrop(3 - player, column)
      }
    }
  }

  const columnDrop = function(player, column){
    if(active[column] < 0){
      console.log(`Error: Cannot drop a piece in column ${column} as it's active position is ${active[column]}`)
    }
    const [y, x] = [active[column], column]


    updateDisplayBoard(y, x, player === 1 ? "B" : "R")

    setHover(-1)
    setCurrentPlayer(3 - player)

    return[column, active[column]--]
  }

  const columnHover = function(player, column){
    if(isGameOver) return
    changeHover(column)
  }

  const changeHover = function(column){
    if(hover >= 0){
      updateDisplayBoard(active[hover], hover, ' ')

    }
    setHover(column)
    if(column>=0){

      updateDisplayBoard(active[column], column, currentPlayer === 1 ? 'G' : 'P')
    }
  }

  const changeGameType = function(type){
    setGameType(type)
    resetGame()
  }

  return (
    <div id="container">
      <h1>Connect 4</h1>
      <div id="app">
        <p id="endGame"></p>
        <div id="dropButtons">
        {
          Array(COLS).fill().map((i, x) => {

            return (active[x] >= 0)
              ? <button
              key={x}
              className={`dropButton ${currentPlayer === 1? 'hoverBlack' : 'hoverRed'}`}
              onClick={e => pressButton(currentPlayer, x)}
              onMouseOver={e => columnHover(1, x)}
              onMouseLeave={e => changeHover(-1)}
              />
              :
              <div className='disabledButton'>
              </div>
          })
        }
        </div>
        <Grid/>
        <div className="toolbar">
          <button id="start" className="off cursor-pointer" onClick={() => startGame()}>NEW GAME</button>
          <button id='pvp' className={`cursor-pointer ${gameType === 'pvp' ? 'on' : 'off'}`} onClick={e => changeGameType('pvp')}>PvP</button>
          <button id='pvai' className={`cursor-pointer ${gameType === 'pvai' ? 'on' : 'off'}`} onClick={e => changeGameType('pvai')}>PvAI</button>
          <button id='pvml' className={`cursor-pointer ${gameType === 'pvml' ? 'on' : 'off'}`} onClick={e => changeGameType('pvml')}>PvML</button>
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
