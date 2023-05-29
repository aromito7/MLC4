import { useState } from "react";
import { login } from "../../store/session";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import './LoginForm.css';

function LoginFormPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector(state => state.session.user);
  const sessionTheme = useSelector(state => state.session.theme);
  
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  const history = useHistory();

  if (sessionUser) return null;
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const data = await dispatch(login(email, password));
    if (data) {
      if (!data.id) {
        return setErrors(data);
      }
    }
    
    setEmail("");
    setPassword("");
    return history.push('/');
  };
  
  // const handleDemoLogin = async (e) => {
  //   e.preventDefault();
    
  //   await dispatch(login('demo@aa.io', 'password'));
  //   setEmail("");
  //   setPassword("");
  //   return history.push('/');
  // }
  
  
  // const tabSubmitLogin = (e) => {
  //   if (e.key === "Tab") {
  //     e.preventDefault();
  //     if (buttonDisabled) return;
  //     handleSubmit(e);
  //   } 
  // }
  
  // const buttonDisabled = email.length < 1 || password.length < 1;

  return (
    <div>
      <div id="login-container">
        
        <form onSubmit={handleSubmit}>
          
        </form>
        
      </div>
    </div>
  );
}

export default LoginFormPage;
