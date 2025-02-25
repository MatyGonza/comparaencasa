import React from 'react';
import { createRoot } from 'react-dom/client'; // Importa createRoot
import App from './App';


// Selecciona el contenedor raíz
const container = document.getElementById('root');

// Crea una raíz
const root = createRoot(container);

// Renderiza la aplicación
root.render(<App />);