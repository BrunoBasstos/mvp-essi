// src/components/PassengerForm.js
import React, {useState} from 'react';
import Swal from 'sweetalert2';
import {
    Box,
    Button,
    TextField,
    Typography,
    FormControl,
    InputLabel,
    Select,
    MenuItem,
    Grid,
    Paper
} from '@mui/material';


export default function PassengerForm() {
    const onsubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData(event.target);
        const passengerData = Object.fromEntries(formData.entries());

        try {
            const response = await fetch('http://localhost:5000/passageiros', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(passengerData),
            });

            if (response.ok) {
                const result = await response.json();
                const outcomeMessage = result.outcome ? 'SOBREVIVEU :-)' : 'NÃO SOBREVIVEU :-(';
                Swal.fire({
                    title: 'PASSAGEIRO CADSTRADO',
                    html: `<div style="margin-bottom: 15px;">Veja abaixo a previsão</div>
                                <div style="display: grid; columns: 3; grid-template-columns: repeat(3, 1fr); grid-auto-rows: 50px; gap: 16px">                                
                                <div>
                                    <div style="font-weight: bold;">Nome:</div><div>${result.name}</div>
                                </div>
                                <div>
                                    <div style="font-weight: bold;">Idade:</div><div>${result.age}</div>
                                </div>
                                <div>
                                    <div style="font-weight: bold;">Classe:</div><div>${result.pclass}</div>
                                </div>
                            </div>
                            <div style="padding: 15px; background-color: ${result.outcome ? 'green' : 'red'}; color: #FFF; border-radius: 5px; margin-top: 16px;">
                                <div style="font-weight: bold;">Previsão:</div>
                                <div>${outcomeMessage}</div>
                            </div>`,
                    icon: result.outcome ? 'success' : 'error',
                    confirmButtonText: 'Ok'
                });
            } else {
                let errorMsg = 'Erro ao enviar dados para o servidor.';
                if (response.status === 400) {
                    errorMsg = 'Passageiro já cadastrado.';
                }
                Swal.fire({
                    title: 'Erro',
                    text: errorMsg,
                    icon: 'error',
                    confirmButtonText: 'Ok'
                });
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

    const [passenger, setPassenger] = useState({
        pclass: '',
        name: '',
        sex: '',
        age: '',
        sibsp: '',
        parch: '',
        ticket: '',
        fare: '',
        cabin: '',
        embarked: ''
    });

    const [isValid, setIsValid] = useState({
        name: false,
        age: false,
        pclass: false,
        sex: false,
        embarked: false,
        sibsp: false,
        parch: false,
        ticket: true,
        fare: false,
        cabin: true
    });

    const checkValidity = (name, value) => {
        switch (name) {
            case 'name':
                return value.trim() !== '';
            case 'age':
                return value > 0;
            case 'pclass':
                return value !== '';
            case 'sex':
                return value !== '';
            case 'embarked':
                return value !== '';
            case 'sibsp':
                return value >= 0;
            case 'parch':
                return value >= 0;
            case 'fare':
                return value >= 0;
            default:
                return true;
        }
    };

    const handleChange = (event) => {
        const {name, value} = event.target;

        const fieldIsValid = checkValidity(name, value);
        setPassenger({...passenger, [name]: value});
        setIsValid({...isValid, [name]: fieldIsValid});
    };

    const isFormValid = () => {
        return Object.values(isValid).every(Boolean);
    };

    return (
        <Paper style={{padding: '16px', marginTop: '16px', background: '#FFF'}}>
            <Typography variant="h4" align="center" gutterBottom>
                Cadastrar Passageiro
            </Typography>
            <Typography variant="body1" align="center" gutterBottom>
                Preencha os campos abaixo para cadastrar um novo passageiro e prever se ele sobreviveria ao naufrágio do
                Titanic.
            </Typography>
            <Typography variant="body1" align="center" gutterBottom>
                Os campos marcados com * são obrigatórios.
            </Typography>

            <Box component="form" onSubmit={onsubmit} sx={{mt: 1}}>
                <Grid container spacing={2}>
                    <Grid item xs={12} sm={8}>
                        <TextField
                            margin="normal"
                            required
                            fullWidth
                            label="Nome"
                            name="name"
                            value={passenger.name}
                            onChange={handleChange}
                        />
                    </Grid>

                    <Grid item xs={12} sm={4}>
                        <TextField
                            type={'number'}
                            margin="normal"
                            required
                            fullWidth
                            label="Idade"
                            name="age"
                            value={passenger.age}
                            onChange={handleChange}
                        />
                    </Grid>

                    <Grid item xs={12} sm={4}>
                        <FormControl fullWidth>
                            <InputLabel id="demo-simple-select-label">Classe *</InputLabel>
                            <Select
                                required
                                labelId="pclass-select"
                                id="pclass-select"
                                value={passenger.pclass}
                                label="Classe"
                                name="pclass"
                                onChange={handleChange}
                            >
                                <MenuItem value={'1'}>Primeira Classe</MenuItem>
                                <MenuItem value={'2'}>Segunda Classe</MenuItem>
                                <MenuItem value={'3'}>Terceira Classe</MenuItem>
                            </Select>
                        </FormControl>
                    </Grid>

                    <Grid item xs={12} sm={4}>
                        <FormControl fullWidth>
                            <InputLabel id="demo-simple-select-label">Sexo *</InputLabel>
                            <Select
                                required
                                labelId="demo-simple-select-label"
                                id="demo-simple-select"
                                value={passenger.sex}
                                label="Sexo"
                                placeholder="Sexo"
                                name="sex"
                                onChange={handleChange}
                            >
                                <MenuItem value={'male'}>Masculino</MenuItem>
                                <MenuItem value={'female'}>Feminino</MenuItem>
                            </Select>
                        </FormControl>
                    </Grid>

                    <Grid item xs={12} sm={4}>
                        <FormControl fullWidth>
                            <InputLabel id="demo-simple-select-label">Porto de Embarque</InputLabel>
                            <Select
                                required
                                labelId="pclass-select"
                                id="pclass-select"
                                value={passenger.embarked}
                                label="Porto de Embarque"
                                name="embarked"
                                onChange={handleChange}
                            >
                                <MenuItem value={'C'}>Cherbourg</MenuItem>
                                <MenuItem value={'Q'}>Queenstown</MenuItem>
                                <MenuItem value={'S'}>Southampton</MenuItem>
                            </Select>
                        </FormControl>
                    </Grid>


                    <Grid item xs={12} sm={6}>
                        <TextField
                            type={'number'}
                            margin="normal"
                            required
                            fullWidth
                            label="Qtd Irmãos e Cônjuge a bordo"
                            name="sibsp"
                            value={passenger.sibsp}
                            onChange={handleChange}
                        />
                    </Grid>
                    <Grid item xs={12} sm={6}>
                        <TextField
                            type={'number'}
                            margin="normal"
                            required
                            fullWidth
                            label="Qtd parentes (pai/mãe) e filhos a bordo"
                            name="parch"
                            value={passenger.parch}
                            onChange={handleChange}
                        />
                    </Grid>

                    <Grid item xs={12} sm={4}>
                        <FormControl fullWidth>
                            <TextField
                                margin="normal"
                                fullWidth
                                label="Número do Ticket de embarque (opcional)"
                                name="ticket"
                                value={passenger.ticket}
                                onChange={handleChange}
                            />
                        </FormControl>
                    </Grid>
                    <Grid item xs={12} sm={4}>
                        <FormControl fullWidth>
                            <TextField
                                type={'number'}
                                margin="normal"
                                required
                                fullWidth
                                label="Valor da Passagem"
                                name="fare"
                                value={passenger.fare}
                                onChange={handleChange}
                            />
                        </FormControl>
                    </Grid>
                    <Grid item xs={12} sm={4}>
                        <FormControl fullWidth>
                            <TextField
                                margin="normal"
                                fullWidth
                                label="Cabine"
                                name="cabin"
                                value={passenger.cabin}
                                onChange={handleChange}
                            />
                        </FormControl>
                    </Grid>
                    <Button type="submit" fullWidth variant="contained" sx={{mt: 3, mb: 2}} disabled={!isFormValid()}>
                        {!isFormValid() ? 'Preencha os campos obrigatórios' : 'Cadastrar e Prever Sobrevivência'}
                    </Button>
                </Grid>
            </Box>
        </Paper>
    );
}
