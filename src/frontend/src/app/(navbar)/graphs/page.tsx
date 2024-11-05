'use client';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
  Container,
  Typography,
  Box,
  CircularProgress,
  Alert,
} from '@mui/material';

const ChartComponent = ({ endpoint, title }) => {
  const [chartData, setChartData] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    axios
      .get(`http://0.0.0.0:3333/api/charts/${endpoint}`)
      .then((response) => {
        if (response.data.chart) {
          setChartData(response.data.chart);
        } else if (response.data.error) {
          setError(response.data.error);
        }
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error fetching chart data:', error);
        setError('Erro ao carregar o gráfico.');
        setLoading(false);
      });
  }, [endpoint]);

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" sx={{ mt: 4 }}>
        <CircularProgress />
      </Box>
    );
  }

  if (error) {
    return (
      <Alert severity="error" sx={{ mt: 2 }}>
        {error}
      </Alert>
    );
  }

  return (
    <Box sx={{ my: 4 }}>
      <Typography variant="h5" sx={{ mb: 2, textAlign: 'center' }}>
        {title}
      </Typography>
      {chartData ? (
        <Box display="flex" justifyContent="center">
          <img
            src={`data:image/png;base64,${chartData}`}
            alt={title}
            style={{ maxWidth: '100%', height: 'auto', borderRadius: 8 }}
          />
        </Box>
      ) : (
        <Typography variant="body1" sx={{ textAlign: 'center' }}>
          Gráfico não disponível.
        </Typography>
      )}
    </Box>
  );
};

export default function Graficos() {
  return (
    <Container maxWidth="md">
      <Typography
        variant="h4"
        sx={{ mt: 4, mb: 4, textAlign: 'center', fontWeight: 'bold' }}
      >
        Gráficos de Análise
      </Typography>
      <ChartComponent endpoint="checkup_time" title="Tempo Total de Check-up" />
      <ChartComponent endpoint="freq_erros" title="Frequência de Erros" />
    </Container>
  );
}
