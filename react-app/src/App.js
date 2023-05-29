import { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Redirect, Route, Switch} from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import GameBoard from "./components/GamePage";

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

          <Route path="/signup">
            <SignupFormPage />
          </Route>

          <Route path="/login" >
            <LoginFormPage />
          </Route>



          <Route path="/">
            <GameBoard/>
          </Route>

        </Switch>
      )}
    </>
  );
}

export default App;
