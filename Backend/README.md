# Prototipo de IA para Test de Holland con Modulación de Voz

Este sistema predice el tipo vocacional (RIASEC) de un estudiante analizando cómo responde en voz a preguntas del Test de Holland.

## Módulos
- Grabación de voz por pregunta
- Extracción de características vocales (MFCC, pitch, etc.)
- Clasificación automática con Random Forest
- Interfaz simple por consola

## Estructura
- data/: grabaciones y dataset
- features/: extracción de audio
- model/: entrenamiento y predicción
- utils/: grabación de audio