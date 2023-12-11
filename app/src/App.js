// src/App.js
import React from 'react';
import './App.css';
import PassengerForm from './components/PassengerForm';
import PassengerList from './components/PassengerList';
import SearchPassenger from './components/SearchPassenger';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';

function App() {
    return (
        <Router>
            <AppBar position="static" sx={{flexGrow: 1}}>
                <Toolbar>
                    <Typography variant="h6" sx={{flexGrow: 1}}>
                        Titanic Survival Predictor (85% accuracy)
                    </Typography>
                    <Button color="inherit" component={Link} to="/" sx={{color: 'white', textDecoration: 'none'}}>
                        Home
                    </Button>
                    <Button color="inherit" component={Link} to="/list" sx={{color: 'white', textDecoration: 'none'}}>
                        Listar Passageiros
                    </Button>
                    <Button color="inherit" component={Link} to="/search" sx={{color: 'white', textDecoration: 'none'}}>
                        Pesquisar Passageiros
                    </Button>
                </Toolbar>
            </AppBar>
            <Routes>
                <Route path="/" element={<PassengerForm />} />
                <Route path="/list" element={<PassengerList />} />
                <Route path="/search" element={<SearchPassenger />} />
            </Routes>
        </Router>
    );
}

export default App;
