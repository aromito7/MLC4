import { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Redirect, Route, Switch} from "react-router-dom";
import GameBoard from "./components/GamePage";
import './style.css'

function App() {


  return (
    <>
      <Switch>

        <Route path="/">
          <GameBoard/>
        </Route>

      </Switch>
    </>
  );
}

export default App;
