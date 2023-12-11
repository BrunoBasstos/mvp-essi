// src/components/PassengerList.js
import React, {useEffect, useState} from 'react';
import Swal from 'sweetalert2';
import {Typography, Grid, Paper} from '@mui/material';

const PassengerList = () => {
    const [passengers, setPassengers] = useState([]);

    useEffect(() => {
        const fetchPassengers = async () => {
            try {
                const response = await fetch('http://localhost:5000/passageiros');
                if (response.ok) {
                    const data = await response.json();
                    setPassengers(data);
                } else if (response.status === 404) {
                    setPassengers([]);
                }
            } catch (error) {
                Swal.fire({
                    title: 'Erro',
                    text: 'Erro ao conectar com o servidor.',
                    icon: 'error',
                    confirmButtonText: 'Ok'
                });
            }
        };
        fetchPassengers();
    }, []);

    return (
        passengers.length === 0 ? (
            <Paper style={{padding: '16px', marginTop: '16px', background: '#FFF'}}>
                <Typography variant="h4" align="center" gutterBottom>
                    Nenhum passageiro encontrado
                </Typography>
            </Paper>
        ) : (

            <Grid container spacing={2} sx={{p: 2}}>
                {passengers.map((passenger) => (
                    <Grid item xs={6} sm={2} key={passenger.id}>
                        <Paper sx={{p: 2}} elevation={3} variant="outlined"
                               style={{
                                   backgroundColor: passenger.outcome ? 'green' : 'red',
                                   color: passenger.outcome ? '#ccfd7f' : '#fcdede'
                               }}
                        >
                            <Typography variant="h6" gutterBottom>
                                {passenger.name.substring(0, 20)} {passenger.name.length > 20 ? '...' : ''}
                            </Typography>
                            <Typography variant="body1" gutterBottom>
                                {passenger.sex === 'female' ? 'Feminino' : 'Masculino'} {passenger.age} - {passenger.pclass}ª
                                Classe
                            </Typography>
                            <Typography variant="body1" gutterBottom>
                                {passenger.outcome ? 'Sobreviveu' : 'Não sobreviveu'}
                            </Typography>
                        </Paper>
                    </Grid>
                ))}
            </Grid>
        )
    );
};

export default PassengerList;
