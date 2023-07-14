import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { ModalProvider, Modal } from './context/Modal';
import App from './App';
import './css';

// React 18 Update
const domNode = document.getElementById('root');
const root = createRoot(domNode)

root.render(
	<React.StrictMode>
		<ModalProvider>
			<BrowserRouter>

				<App />
				<Modal />

			</BrowserRouter>
		</ModalProvider>
	</React.StrictMode>
);
