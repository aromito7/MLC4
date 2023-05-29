import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { signUp } from "../../store/session";
import { useHistory } from "react-router-dom";
import './SignupForm.css';

function SignupFormPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector(state => state.session.user);
  const sessionTheme = useSelector(state => state.session.theme);
  
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [hasSubmitted, setHasSubmitted] = useState(false);
  const [errors, setErrors] = useState({});
  const history = useHistory();

  
  useEffect(() => {
    if (hasSubmitted) setErrors(validateFormErrors())
  }, [hasSubmitted, email, username, password, confirmPassword])
  
  if (sessionUser) return <Redirect to="/" />;
  
  const validateFormErrors = () => {
    const newErrors = {};
    
    if (!email || (email.length < 4 || email.length > 30)) newErrors.email = 'Email (4-30) characters';
    if (!username || (username.length < 2 || username.length > 20)) newErrors.username = 'Username (2-20) characters';
    if (!password || (password.length < 6 || password.length > 30)) newErrors.password = 'password (2-30) characters';
    if (confirmPassword && confirmPassword !== password) newErrors.confirmPassword = 'Password fields must match';
    
    return newErrors;
  }
  
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const newErrors = validateFormErrors();
    if (Object.values(newErrors).length > 0) {
      setHasSubmitted(true);
      return setErrors(newErrors);
    }
    
    const user = {
      email,
      username,
      password,
      confirmPassword
    }
    
    const data = await dispatch(signUp(user));
    if (data.errors) {
      return setErrors(data.errors);
    }
    
    return history.push('/');
  };
  
  // const diableSignupButton = () => !email || !username ||
  //             !password || !confirmPassword || errors.length > 0;
              
  // const tabSubmitSignup = (e) => {
  //   if (e.key === "Tab") {
  //     e.preventDefault();
  //     if (diableSignupButton) return;
  //     handleSubmit(e);
  //   } 
  // }
  
  return (
    <>
      <div id="signup-container">
				
				<form onSubmit={handleSubmit}>
					<ul className="signup-errors-ul">
						{Object.values(errors).map((error, idx) => (
							<li key={idx}>{error}</li>
						))}
					</ul>
				
        
            
					
				</form>
			</div>
    </>
  );
}

export default SignupFormPage;
