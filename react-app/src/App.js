import { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Redirect, Route, Switch} from "react-router-dom";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import GameBoard from "./components/GamePage";
import './style.css'

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);




  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>

          <Route path="/">
            <GameBoard/>
          </Route>

        </Switch>
      )}
    </>
  );
}

export default App;
