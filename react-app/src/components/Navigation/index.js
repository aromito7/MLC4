import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);
	const sessionTheme = useSelector(state => state.session.theme);
	
	
	if (!sessionUser) return null;
	
	return (
		<div id="navigation-container" data-theme={sessionTheme}>
				
						
		<div>
			{isLoaded && <ProfileButton user={sessionUser} />}
		</div>
					
		</div>
	);
};

export default Navigation;
