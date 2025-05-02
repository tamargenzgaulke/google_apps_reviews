import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import plotly.express as px
from datetime import datetime

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("df_sentimentos.csv", parse_dates=["at", "repliedAt"])
    df["month"] = df["at"].dt.to_period("M").astype(str)
    return df

df = load_data()

st.title("Análise de Sentimentos em Reviews de App")

# Filtros interativos
st.sidebar.header("Filtros")
sentimentos = st.sidebar.multiselect("Selecione os sentimentos:", df["sentimento"].unique(), default=df["sentimento"].unique())
score = st.sidebar.slider("Score:", int(df["score"].min()), int(df["score"].max()), (int(df["score"].min()), int(df["score"].max())))
meses = st.sidebar.multiselect("Selecione os meses:", df["month"].unique(), default=df["month"].unique())

filtro = (df["sentimento"].isin(sentimentos)) & \
         (df["score"].between(score[0], score[1])) & \
         (df["month"].isin(meses))

df_filtrado = df[filtro]

st.subheader("Distribuição dos Sentimentos")
sent_counts = df_filtrado["sentimento"].value_counts()
st.plotly_chart(px.pie(names=sent_counts.index, values=sent_counts.values, title="Sentimentos"), use_container_width=True)

st.subheader("Evolução dos Sentimentos ao Longo do Tempo")
temp = df_filtrado.groupby(["month", "sentimento"]).size().reset_index(name="count")
fig1 = px.line(temp, x="month", y="count", color="sentimento", markers=True)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Boxplot da Polaridade por Score")
fig2 = px.box(df_filtrado, x="score", y="polarity", color="sentimento")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Nuvem de Palavras por Sentimento")
sent_select = st.selectbox("Escolha um sentimento para a nuvem de palavras:", df_filtrado["sentimento"].unique())
text = " ".join(df_filtrado[df_filtrado["sentimento"] == sent_select]["content"].dropna())
wordcloud = WordCloud(background_color="white", width=800, height=400).generate(text)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

st.subheader("Polaridade vs Curtidas")
fig3 = px.scatter(df_filtrado, x="polarity", y="thumbsUpCount", color="sentimento", hover_data=["content"], size_max=60)
st.plotly_chart(fig3, use_container_width=True)

st.dataframe(df_filtrado.head(20))
