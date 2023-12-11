// src/components/SearchPassenger.js
import React, {useState} from 'react';
import Swal from 'sweetalert2';
import {
    Box, Button, TextField, Typography, Grid, Paper
} from '@mui/material';

const SearchPassenger = () => {
    const [hasSearched, setHasSearched] = useState(false);
    const [searchTerm, setSearchTerm] = useState('');
    const [searchResults, setSearchResults] = useState([]);

    const handleSearch = async (event) => {
        event.preventDefault();
        try {
            const response = await fetch(`http://localhost:5000/passageiros?name=${searchTerm}`);
            if (response.ok) {
                const data = await response.json();
                setSearchResults(data);
            } else if (response.status === 404) {
                setSearchResults([]);
            } else if (response.status === 400) {
                setHasSearched(false);
                Swal.fire({
                    title: 'Erro',
                    text: 'Informe um termo para a busca.',
                    icon: 'error',
                    confirmButtonText: 'Ok'
                });
            }

            setHasSearched(true);
        } catch (error) {
            setHasSearched(false);
            Swal.fire({
                title: 'Erro',
                text: 'Erro ao conectar com o servidor.',
                icon: 'error',
                confirmButtonText: 'Ok'
            });
        }
    };

    return (
        <Grid container spacing={2} sx={{p: 2}}>
            <Grid item xs={12}>
                <Box sx={{display: 'flex', alignItems: 'flex-end'}}>
                    <TextField
                        fullWidth
                        label="Nome do Passageiro"
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                    />
                    <Button
                        variant="contained"
                        onClick={handleSearch}
                        sx={{height: '100%'}}
                    >
                        Pesquisar
                    </Button>
                </Box>
            </Grid>

            {!hasSearched ? (
                <Typography variant="h4" align="center" textAlign="center" style={{width: '100%', padding: '15px'}}
                            gutterBottom>
                    Informe um nome para pesquisar
                </Typography>
            ) : (
                searchResults.length === 0 ? (
                    <Typography variant="h4" align="center" textAlign="center" style={{width: '100%', padding: '15px'}}
                                gutterBottom>
                        Nenhum passageiro encontrado
                    </Typography>
                ) : (
                    <Grid item xs={12}>
                        <Grid container spacing={2}>
                            {searchResults.map((passenger) => (
                                <Grid item xs={6} sm={2} key={passenger.id}>
                                    <Paper sx={{p: 2}} elevation={3} variant="outlined"
                                           style={{backgroundColor: passenger.outcome ? 'green' : 'red'}}>
                                        <Typography variant="h6" gutterBottom>
                                            {passenger.name} ({passenger.sex === 'female' ? 'M' : 'H'} {passenger.age})
                                        </Typography>
                                        <Typography variant="body1" gutterBottom>
                                            {passenger.outcome ? 'Sobreviveu' : 'Não sobreviveu'}
                                        </Typography>
                                    </Paper>
                                </Grid>
                            ))}
                        </Grid>
                    </Grid>
                )
            )}
        </Grid>
    );
}

export default SearchPassenger;
