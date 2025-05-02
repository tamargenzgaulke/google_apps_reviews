<<<<<<< HEAD
# google_apps_reviews
=======
# google_apps_reviewsa# google_apps_reviews
>>>>>>> 774d459 (first commit)

# Análise de Sentimentos em Avaliações de Aplicativo 📱🧠

Este projeto utiliza técnicas de **Processamento de Linguagem Natural (PLN)** para realizar análise de sentimentos em avaliações de usuários extraídas de um aplicativo. O objetivo é extrair, limpar, visualizar e interpretar sentimentos (positivos, negativos e neutros), além de criar visualizações e um app interativo com **Streamlit**.

## 🔍 Funcionalidades

- Pré-processamento de texto com `nltk`, `spaCy` e `TextBlob`
- Tokenização, remoção de stopwords, stemming e lematização
- Geração de nuvens de palavras
- Análise de polaridade com VADER
- Classificação dos sentimentos (positivo, negativo, neutro)
- Visualizações interativas com `plotly`
- Interface interativa com **Streamlit**

## 📂 Estrutura do Projeto

├── reviews.csv # Base de dados com as avaliações
├── text_mining_1_colab.ipynb # Notebook com toda a análise
├── df_sentimentos.csv # Base com sentimentos rotulados
├── app.py # Aplicativo em Streamlit
└── README.md # Este arquivo

bash
Copiar
Editar

## 🛠️ Instalação e Execução

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute o app Streamlit:

bash
Copiar
Editar
streamlit run app.py
📊 Tecnologias Utilizadas
Python

NLTK

spaCy

TextBlob

WordCloud

Plotly

Pandas

Matplotlib

Seaborn

Streamlit

📈 Principais Visualizações
Nuvens de palavras por sentimento

Distribuição de sentimentos

Evolução temporal dos sentimentos

Boxplot de polaridade vs. score

Correlação entre likes e polaridade

💡 Resultado Esperado
Um sistema que ajuda a compreender o sentimento geral dos usuários em relação ao aplicativo, com insights visuais e interativos que facilitam a tomada de decisão para melhorias.

👩‍💻 Autora
Desenvolvido por Tamar ✨
Contato: [Seu LinkedIn ou e-mail aqui]

