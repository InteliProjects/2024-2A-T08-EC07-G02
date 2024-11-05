'use client';
import React, { useState, useEffect } from 'react';
import { DefaultService } from '@client';
import {
  Box,
  Button,
  Typography,
  Card,
  CardContent,
  CardActions,
  Container,
  Paper,
  Alert,
  CircularProgress,
  TextField,
  Autocomplete,
  Chip,
} from '@mui/material';
import Grid from '@mui/material/Grid2';
import { saveAs } from 'file-saver';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import RadioButtonUncheckedIcon from '@mui/icons-material/RadioButtonUnchecked';
import DeleteIcon from '@mui/icons-material/Delete';
import DownloadIcon from '@mui/icons-material/Download';
import VisibilityIcon from '@mui/icons-material/Visibility';
import SelectAllIcon from '@mui/icons-material/SelectAll';

export default function Dashboard() {
  const [failuresFile, setFailuresFile] = useState<File | null>(null);
  const [resultsFile, setResultsFile] = useState<File | null>(null);
  const [statusFile, setStatusFile] = useState<File | null>(null);
  const [tags, setTags] = useState<string[]>([]);
  const [models, setModels] = useState<
    { model_name: string; tags: String[]}[]
  >([]);
  const [selectedModel, setSelectedModel] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);
  const [modelsLoading, setModelsLoading] = useState<boolean>(true);
  const [error, setError] = useState<string>('');
  const [successMessage, setSuccessMessage] = useState<string>('');

  useEffect(() => {
    setModelsLoading(true);
    DefaultService.listModelsApiModelGet()
      .then((response: any) => {
        if (response && response.models) {
          setModels(response.models);
        }
        // Fetch the selected model
        return DefaultService.selectedModelApiModelSelectedGet();
      })
      .then((response: any) => {
        if (response && response.model) {
          setSelectedModel(response.model);
        }
        setModelsLoading(false);
      })
      .catch((error) => {
        console.error('Error fetching models:', error);
        setError('Falha ao buscar os modelos.');
        setModelsLoading(false);
      });
  }, []);

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!failuresFile || !resultsFile || !statusFile) {
      setError(
        'Por favor, selecione os arquivos necessários para o treinamento.'
      );
      return;
    }

    setLoading(true);
    setError('');
    setSuccessMessage('');

    DefaultService.requestApiModelTrainPost({
      formData: {
		failures: failuresFile,
		results: resultsFile,
		status: statusFile,
		tags,
		},
    })
      .then((response) => {
        console.log('Model training started:', response);
        setSuccessMessage('Treinamento realizado com sucesso.');
        return DefaultService.listModelsApiModelGet();
      })
      .then((response: any) => {
        if (response && response.models) {
          setModels(response.models);
        }
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error training model:', error);
        setError('Falha ao treinar o modelo.');
        setLoading(false);
      });
  };

  const handleDownload = (modelId: string) => {
    setLoading(true);
    setError('');
    DefaultService.downloadModelApiModelDownloadModelIdGet({ modelId })
      .then((response: any) => {
        console.log('Model downloaded:', response);
        const blob = new Blob([response], { type: 'application/octet-stream' });
        saveAs(blob, modelId);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error downloading model:', error);
        setError('Falha ao baixar o modelo.');
        setLoading(false);
      });
  };

  const handleNetron = (modelId: string) => {
    setLoading(true);
    setError('');
    DefaultService.downloadModelApiModelDownloadModelIdGet({ modelId })
      .then((response: any) => {
        const netronUrl = `https://netron.app/?url=${encodeURIComponent(response.url)}`;
        window.open(netronUrl, '_blank');
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error downloading model:', error);
        setError('Falha ao visualizar o modelo.');
        setLoading(false);
      });
  };

  const handleDelete = (modelId: string) => {
    setLoading(true);
    setError('');
    DefaultService.deleteModelApiModelModelIdDelete({ modelId })
      .then((response: any) => {
        console.log('Model deleted:', response);
        setSuccessMessage(`Modelo '${modelId}' excluído com sucesso.`);
        // Atualizar a lista de modelos
        return DefaultService.listModelsApiModelGet();
      })
      .then((response: any) => {
        if (response && response.models) {
          setModels(response.models);
        }
        // Se o modelo excluído for o selecionado, limpar a seleção
        if (modelId === selectedModel) {
          setSelectedModel('');
        }
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error deleting model:', error);
        setError('Falha ao excluir o modelo.');
        setLoading(false);
      });
  };

  const handleSelect = (modelId: string) => {
    setLoading(true);
    setError('');
    DefaultService.selectModelApiModelSelectModelIdPost({ modelId })
      .then((response: any) => {
        console.log('Model selected:', response);
        setSuccessMessage(`Modelo '${modelId}' selecionado com sucesso.`);
        setSelectedModel(modelId);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error selecting model:', error);
        setError('Falha ao selecionar o modelo.');
        setLoading(false);
      });
  };

  return (
    <Container maxWidth="md">
      <Paper sx={{ padding: 4, marginBottom: 4, marginTop: 4 }} elevation={3}>
        <Typography variant="h4" gutterBottom>
          Treinamento de modelos
        </Typography>
        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}
        {successMessage && (
          <Alert severity="success" sx={{ mb: 2 }}>
            {successMessage}
          </Alert>
        )}
        <form onSubmit={handleSubmit}>
          <Grid container spacing={2}>
            <Grid size={{ xs: 12, sm: 4 }}>
              <Button variant="contained" component="label" fullWidth>
                Enviar Falhas
                <input
                  type="file"
                  hidden
                  onChange={(e) =>
                    setFailuresFile(e.target.files ? e.target.files[0] : null)
                  }
                />
              </Button>
              {failuresFile && (
                <Typography variant="body2" sx={{ mt: 1 }}>
                  Arquivo selecionado: {failuresFile.name}
                </Typography>
              )}
            </Grid>
            <Grid size={{ xs: 12, sm: 4 }}>
              <Button variant="contained" component="label" fullWidth>
                Enviar Resultados
                <input
                  type="file"
                  hidden
                  onChange={(e) =>
                    setResultsFile(e.target.files ? e.target.files[0] : null)
                  }
                />
              </Button>
              {resultsFile && (
                <Typography variant="body2" sx={{ mt: 1 }}>
                  Arquivo selecionado: {resultsFile.name}
                </Typography>
              )}
            </Grid>
            <Grid size={{ xs: 12, sm: 4 }}>
              <Button variant="contained" component="label" fullWidth>
                Enviar Status
                <input
                  type="file"
                  hidden
                  onChange={(e) =>
                    setStatusFile(e.target.files ? e.target.files[0] : null)
                  }
                />
              </Button>
              {statusFile && (
                <Typography variant="body2" sx={{ mt: 1 }}>
                  Arquivo selecionado: {statusFile.name}
                </Typography>
              )}
            </Grid>
            <Grid size={{ xs: 12 }}>
              <Autocomplete
                multiple
                freeSolo
                options={[]}
                value={tags}
                onChange={(event, newValue) => {
                  setTags(newValue as string[]);
                }}
                renderTags={(value: string[], getTagProps) =>
                  value.map((option: string, index: number) => (
                    <Chip
                      variant="outlined"
                      label={option}
                      {...getTagProps({ index })}
                    />
                  ))
                }
                renderInput={(params) => (
                  <TextField
                    {...params}
                    variant="outlined"
                    label="Tags"
                    placeholder="Pressione Enter para adicionar uma tag"
                  />
                )}
              />
            </Grid>
            <Grid size={{ xs: 12 }}>
              <Button
                type="submit"
                variant="contained"
                color="primary"
                fullWidth
                disabled={loading}
                startIcon={loading && <CircularProgress size={20} />}
              >
                {loading ? 'Treinando...' : 'Iniciar treinamento'}
              </Button>
            </Grid>
          </Grid>
        </form>
      </Paper>

      <Paper sx={{ padding: 4, marginBottom: 4 }} elevation={3}>
        <Typography variant="h4" gutterBottom>
          Modelos disponíveis
        </Typography>
        {selectedModel && (
          <Typography variant="subtitle1" sx={{ mb: 2 }}>
            Modelo selecionado: <strong>{selectedModel}</strong>
          </Typography>
        )}
        {modelsLoading ? (
          <Box display="flex" justifyContent="center" sx={{ mt: 2 }}>
            <CircularProgress />
          </Box>
        ) : models.length === 0 ? (
          <Typography>Sem modelos disponíveis.</Typography>
        ) : (
          <Grid container spacing={2}>
            {models.map((modelObj, index) => {
              const { model_name, tags } = modelObj;
              return (
                <Grid size={{ xs: 12, sm: 6, md: 4 }} key={index}>
                  <Card
                    sx={{
                      height: '100%',
                      display: 'flex',
                      flexDirection: 'column',
                      border:
                        model_name === selectedModel ? '2px solid' : undefined,
                      borderColor:
                        model_name === selectedModel
                          ? 'primary.main'
                          : undefined,
                      boxShadow: model_name === selectedModel ? 4 : undefined,
                    }}
                  >
                    <CardContent sx={{ flexGrow: 1 }}>
                      <Box display="flex" alignItems="center" sx={{ mb: 1 }}>
                        {model_name === selectedModel ? (
                          <CheckCircleIcon color="primary" sx={{ mr: 1 }} />
                        ) : (
                          <RadioButtonUncheckedIcon
                            color="action"
                            sx={{ mr: 1 }}
                          />
                        )}
                        <Typography variant="h6" noWrap>
                          <b>{model_name.split('_')[0]}</b>
                        </Typography>
                      </Box>
                      <Typography
                        variant="body2"
                        color="textSecondary"
                        sx={{ wordBreak: 'break-all' }}
                      >
                        {model_name}
                      </Typography>
                      {tags.length > 0 && (
                        <Box sx={{ mt: 1 }}>
                          {tags.map((tag, index) => (
							<Chip
							  key={index}
							  label={tag}
							  size="small"
							  sx={{ mr: 1, mb: 1 }}
							/>
						  ))}
                        </Box>
                      )}
                    </CardContent>
                    <CardActions sx={{ flexWrap: 'wrap' }}>
                      <Button
                        size="small"
                        startIcon={<DownloadIcon />}
                        onClick={() => handleDownload(model_name)}
                        disabled={loading}
                      >
                        Download
                      </Button>
                      <Button
                        size="small"
                        startIcon={<VisibilityIcon />}
                        onClick={() => handleNetron(model_name)}
                        disabled={loading}
                      >
                        Visualizar
                      </Button>
                      <Button
                        size="small"
                        startIcon={<SelectAllIcon />}
                        onClick={() => handleSelect(model_name)}
                        disabled={loading || model_name === selectedModel}
                      >
                        {model_name === selectedModel
                          ? 'Selecionado'
                          : 'Selecionar'}
                      </Button>
                      <Button
                        size="small"
                        startIcon={<DeleteIcon />}
                        onClick={() => handleDelete(model_name)}
                        disabled={loading}
                        color="secondary"
                      >
                        Excluir
                      </Button>
                    </CardActions>
                  </Card>
                </Grid>
              );
            })}
          </Grid>
        )}
      </Paper>
    </Container>
  );
}
