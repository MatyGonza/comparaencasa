import React, { useState, useEffect } from 'react';

import { Container, TextField, Button, Box, createTheme,Typography, ThemeProvider, CssBaseline } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';

import { fetchResults } from './services/api';
import './App.css';

const theme = createTheme({
  palette: {
    mode: 'dark',
    background: {
      default: '#121212',
      paper: '#121212',
    },
    text: {
      primary: '#ffffff',
    },
    primary: {
      main: '#90caf9',
    },
    secondary: {
      main: '#f48fb1',
    },
  },
});

const App = () => {
  
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    try {
      const data = await fetchResults(query);
      console.log('Results before setResults:', data); // Verifica la estructura de los datos
      setResults(data || []);
      console.log('Results after setResults:', data); // Verifica la estructura de los datos
    } catch (error) {
      console.error('Error fetching data:', error);
      setResults([]);
    }
  };

  useEffect(() => {
    console.log('Results state updated:', results);
  }, [results]);

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container>
        <Box
          display="flex"
          justifyContent="center"
          alignItems="center"
          minHeight="100vh"
          flexDirection="column"
        >
          
          <Typography variant="h4" component="h1" gutterBottom sx={{ color: 'white' }}>
            Bienvenido a la Búsqueda de Películas
          </Typography>
          <Typography variant="body1" gutterBottom sx={{ color: 'white', mb: 2 }}>
            Ingresa el título de una película para buscar en nuestra base de datos.
          </Typography>
          <TextField
            variant="outlined"
            placeholder="Buscar..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            InputProps={{
              endAdornment: (
                <Button variant="contained" color="primary" startIcon={<SearchIcon />} onClick={handleSearch}>
                  Buscar
                </Button>
              ),
            }}
            sx={{ mb: 2, width: '100%', maxWidth: '500px', input: { color: 'white' } }}
          />
          <Box>
            <ul style={{ color: 'white', listStyleType: 'none', padding: 0 }}>
              {results.map((result, index) => (
                <li key={index} style={{ marginBottom: '8px' }}>
                  {result.primaryTitle || result.name}
                </li>
              ))}
            </ul>
          </Box>
        </Box>
      </Container>
    </ThemeProvider>
  );
};

export default App;