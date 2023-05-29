import React from 'react';
import { createRoot } from 'react-dom/client';
import { Provider } from "react-redux";
import { BrowserRouter } from 'react-router-dom';
import { ModalProvider, Modal } from './context/Modal';
import store from './store';
import App from './App';
import './css';

// React 18 Update
const domNode = document.getElementById('root');
const root = createRoot(domNode)

root.render(
	<React.StrictMode>
		<ModalProvider>
			<Provider store={store}>
				<BrowserRouter>
				
					<App />
					<Modal />
					
				</BrowserRouter>
			</Provider>
		</ModalProvider>
	</React.StrictMode>
);
