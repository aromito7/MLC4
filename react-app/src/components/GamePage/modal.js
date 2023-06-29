import { useState } from "react"

const Modal = ({isModalOpen, setIsModalOpen}) => {
    return(
        <div className={`dropdown-modal ${isModalOpen ? "active" : "inactive"}`}>
            <div id="deposit-container">
                <div className="flex-vertical ">
                    <div className="flex">
                        <div id="x-close" className="cursor-pointer light-background-hover font36" onClick={e => setIsModalOpen(false)}>X</div>
                    </div>
                </div>
                <div id="deposit-container-padding">
                    <div className="flex">
                        <p className="flex-left bold font20">Transfer Money</p>
                    </div>
                    <div id="transfer-modal-grid">
                        <p>Amount</p>
                        <input className="grey-border flex-end"></input>
                        <p>From</p>
                        <select className="grey-border">
                            <option>Interest Checking</option>
                            <option>LittleJohn</option>
                        </select>
                        <p>To</p>
                        <select className="grey-border">
                            <option>LittleJohn</option>
                            <option>Interest Checking</option>
                        </select>
                    </div>
                    <div className="flex-vertical">
                    <p className="pad10 font20">Current buying power: ${0.00}</p>
                        {true ?
                            <>
                                <p className="pad10 red-font font20">Hello</p>
                                <button className="standard-button green-background center" >Dismiss</button>
                            </>
                            : <button className="standard-button green-background center" >Confirm Transfer</button>
                        }
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Modal
