import { useState } from "react"

const Modal = ({isModalOpen, setIsModalOpen, gameType, setGameType}) => {
    return(
        <div className={`dropdown-modal ${isModalOpen ? "active" : "inactive"}`}>
            <div id='dropdown-modal-container'>
                <div id='modal-close-container' className='flex center'>
                    <p className='flex-end cursor-pointer' onClick={e => setIsModalOpen(false)}>
                        Close
                    </p>
                </div>
                <div id='modal-options-container'>
                    <div className="center">
                        <p>Game Types:</p>
                    </div>
                    <div className="center">
                        <ul id="option-list" className="no-bullets">
                            <li className="red-background-hover cursor-pointer center">
                                Player Vs Player
                            </li>
                            <li className="center">
                                Player Vs AI Bot
                            </li>
                            <li className="center">
                                Player Vs ML Bot
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Modal
