'use client';
import React, { useState, useEffect } from 'react';
import { DefaultService } from '@client';
import {
  Box,
  Typography,
  Container,
  Paper,
  CircularProgress,
  Alert,
  Grid,
  Stepper,
  Step,
  StepLabel,
  StepContent,
  TextField,
  Autocomplete,
  Button,
} from '@mui/material';
import { format } from 'date-fns';
import { ptBR } from 'date-fns/locale';
import { CheckCircle, Error, ArrowBack, ArrowForward } from '@mui/icons-material';

export default function LastProcessedKNR() {
  const [knrData, setKnrData] = useState<any>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string>('');
  const [knrsList, setKnrsList] = useState<string[]>([]);
  const [selectedKnr, setSelectedKnr] = useState<string | null>(null);

  useEffect(() => {
    // Buscar a lista de KNRs
    DefaultService.listKnrsApiKnrGet()
      .then((response: any) => {
        setKnrsList(response.knrs || []);
      })
      .catch((error) => {
        console.error('Erro ao buscar a lista de KNRs:', error);
        setError('Falha ao buscar a lista de KNRs.');
      });

    // Buscar o último KNR processado
    DefaultService.getLastKnrApiKnrLastProcessedGet()
      .then((response: any) => {
        setKnrData(response.knr);
        setSelectedKnr(response.knr?.id || null);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Erro ao buscar o último KNR processado:', error);
        setError('Falha ao buscar o último KNR processado.');
        setLoading(false);
      });
  }, []);

  const handleKnrChange = (event: any, value: string | null) => {
    setSelectedKnr(value);
    if (value) {
      setLoading(true);
      DefaultService.getKnrApiKnrKnrGet({ knr: value })
        .then((response: any) => {
          if (response.knr && !response.knr.error) {
            setKnrData(response.knr);
            setError('');
          } else {
            setKnrData(null);
            setError('KNR não encontrado.');
          }
          setLoading(false);
        })
        .catch((error) => {
          console.error('Erro ao buscar o KNR:', error);
          setError('Falha ao buscar o KNR.');
          setLoading(false);
        });
    } else {
      setKnrData(null);
    }
  };

  if (loading) {
    return (
      <Container maxWidth="md">
        <Box display="flex" justifyContent="center" sx={{ mt: 4 }}>
          <CircularProgress />
        </Box>
      </Container>
    );
  }

  return (
    <Container maxWidth="md">
      <Paper sx={{ padding: 4, marginTop: 4 }} elevation={3}>
        <Typography
          variant="h4"
          component="div"
          gutterBottom
          sx={{ textAlign: 'center', fontWeight: 'bold' }}
        >
          Análise do Veículo Processado
        </Typography>

        {/* Campo de busca */}
        <Box sx={{ mt: 2, mb: 2 }}>
          <Autocomplete
            options={knrsList}
            value={selectedKnr + " | Último Processado"}
            onChange={handleKnrChange}
            renderInput={(params) => (
              <TextField {...params} label="Buscar KNR" variant="outlined" fullWidth />
            )}
          />
        </Box>

        {/* Botões de Anterior e Próximo */}
        <Box display="flex" justifyContent="space-between" sx={{ mb: 2 }}>
          <Button variant="contained" startIcon={<ArrowBack />} >
            Anterior
          </Button>
          <Button variant="contained" endIcon={<ArrowForward />} >
            Próximo
          </Button>
        </Box>

        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}

        {knrData ? (
          <Grid container spacing={4} sx={{ mt: 2 }}>
            <Grid item xs={12} md={6}>
              <Box
                sx={{
                  border: 1,
                  borderColor: 'grey.300',
                  borderRadius: 2,
                  padding: 2,
                  backgroundColor: '#f9f9f9',
                }}
              >
                <Typography variant="h6" sx={{ fontWeight: 'bold', mb: 2 }}>
                  Detalhes do Veículo
                </Typography>
                <Typography variant="body1">
                  <strong>ID do Veículo:</strong> {knrData.id}
                </Typography>
                <Typography variant="body1" sx={{ mt: 1 }}>
                  <strong>Status da Análise:</strong>{' '}
                  <Box
                    component="span"
                    sx={{
                      display: 'inline-flex',
                      alignItems: 'center',
                      color: `${
                        knrData.prediction === 'FAILURE' ? 'error.main' : 'success.main'
                      }`,
                      fontWeight: 'bold',
                    }}
                  >
                    {knrData.prediction === 'FAILURE' ? (
                      <Error color="error" sx={{ mr: 1 }} />
                    ) : (
                      <CheckCircle color="success" sx={{ mr: 1 }} />
                    )}
                    {knrData.prediction === 'FAILURE' ? 'FALHA' : 'NORMAL'}
                  </Box>
                </Typography>
                <Typography variant="body1" sx={{ mt: 1 }}>
                  <strong>Data da Atualização:</strong>{' '}
                  {format(
                    new Date(knrData.updated_at),
                    "dd 'de' MMMM 'de' yyyy 'às' HH:mm",
                    {
                      locale: ptBR,
                    }
                  )}
                </Typography>
              </Box>
            </Grid>
            <Grid item xs={12} md={6}>
              <Stepper
                activeStep={
                  knrData.prediction === 'FAILURE' ? 3 : 4
                }
                orientation="vertical"
              >
                <Step completed>
                  <StepLabel>Recebimento do veículo</StepLabel>
                  <StepContent>
                    <Typography variant="body2">
                      Veículo recebido para análise.
                    </Typography>
                  </StepContent>
                </Step>
                <Step completed>
                  <StepLabel>Inspeção inicial</StepLabel>
                  <StepContent>
                    <Typography variant="body2">
                      Realização de inspeção visual e funcional.
                    </Typography>
                  </StepContent>
                </Step>
                <Step completed>
                  <StepLabel>Análise de dados</StepLabel>
                  <StepContent>
                    <Typography variant="body2">
                      Processamento e análise dos dados coletados.
                    </Typography>
                  </StepContent>
                </Step>
                <Step completed={knrData.prediction !== 'FAILURE'}>
                  <StepLabel>Conclusão</StepLabel>
                  <StepContent>
                    {knrData.prediction === 'FAILURE' ? (
                      <Alert severity="error">
                        Possível falha detectada na análise.
                      </Alert>
                    ) : (
                      <Typography variant="body2">
                        Nenhuma falha detectada.
                      </Typography>
                    )}
                  </StepContent>
                </Step>
              </Stepper>
            </Grid>
          </Grid>
        ) : (
          !error && (
            <Alert severity="info" sx={{ mt: 4 }}>
              Nenhum dado de KNR disponível no momento.
            </Alert>
          )
        )}
      </Paper>
    </Container>
  );
}
