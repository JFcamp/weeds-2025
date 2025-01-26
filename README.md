# Classificação de Ervas Daninhas

Este repositório contém o código e a documentação do trabalho desenvolvido por Pedro Henrique Campos Moreira, Elisa e Bernardo, para a classificação de ervas daninhas utilizando técnicas de visão computacional e aprendizado de máquina.

## Objetivo
O objetivo deste projeto é criar um modelo capaz de classificar imagens de diferentes tipos de ervas daninhas, facilitando sua identificação em cenários agrícolas. Essa classificação pode ser usada para automatizar processos de controle e manejo de ervas daninhas, promovendo maior eficiência na agricultura.

## Etapas do Projeto
1. **Coleta e Preparação dos Dados**:
   - Imagens de diferentes tipos de ervas daninhas foram coletadas.
   - As imagens foram segmentadas e organizadas em pastas conforme suas classes.
   - Foi realizado o pré-processamento, como redimensionamento e normalização.

2. **Exploração de Dados**:
   - Visualização de amostras das imagens.
   - Análise do balanceamento das classes.

3. **Modelagem**:
   - Foram testados diferentes modelos de aprendizado de máquina, como KNN, Random Forest e Redes Neurais Convolucionais (CNN).
   - Realização de tuning de hiperparâmetros.

4. **Treinamento e Avaliação**:
   - O conjunto de dados foi dividido em treinamento e teste.
   - Métricas como acurácia, precisão, recall e F1-score foram utilizadas para avaliar o desempenho.

5. **Resultados**:
   - O modelo final apresentou uma acurácia de 97.03%, usando a EfficientNet-V2.
   - EfficientNet V2 demonstrou o melhor desempenho geral com e sem DA, mostrando maior robustez e precisão.
   - O aumento de dados(data augmentation) foi crucial para melhorar o desempenho do modelo, particularmente em precisão e F1-Score.
6. **Contribuições deste estudo:**:
   -  Este trabalho fornece insights valiosos para a construção de modelos eficientes e precisos, com aplicações potenciais no gerenciamento de culturas do mundo real.
   -  Permite uma classificação rápida e precisa de ervas daninhas, além de respostas rápidas, minimizando riscos sem a necessidade de um especialista.

## Como Utilizar
1. Clone este repositório:
   ```bash
   git clone https://github.com/usuario/projeto-classificacao-ervas.git
