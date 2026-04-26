import streamlit as st

# Configuração da página
st.set_page_config(page_title="Sidney Tech - TMO", page_icon="🏗️")

# Estilo personalizado (Cores Sidney Tech)
st.markdown("""
    <style>
    .main { background-color: #0f172a; color: white; }
    .stButton>button { background-color: #1e293b; color: white; border-radius: 10px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏗️ Sidney Tech - Sistema TMO")
st.subheader("Cálculos de Medição e Orçamentação")

# Entradas de dados
with st.sidebar:
    st.header("Configurações de Traço")
    qc = st.number_input("Cimento (Qc)", value=1.0)
    qan = st.number_input("Areia (Qan)", value=4.0)
    st.info(f"Traço total: {qc + qan}")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Área da parede (m²)", min_value=0.0, step=1.0)
    espessura = st.number_input("Espessura (cm)", value=2.0)

with col2:
    preco_cimento = st.number_input("Preço do Saco (KZ)", value=5000)
    litros_saco = st.number_input("Litros por saco", value=35.64)

if st.button("CALCULAR ORÇAMENTO"):
    # Lógica de cálculo (A mesma que validamos)
    volume_total = area * (espessura / 100)
    traco_total = qc + qan
    volume_cimento = (volume_total / traco_total) * qc
    
    qtd_sacos = (volume_cimento * 1000) / litros_saco
    custo_total = qtd_sacos * preco_cimento
    
    # Exibição dos resultados
    st.success(f"### Resultado para {area}m²")
    st.metric("Sacos de Cimento", f"{qtd_sacos:.2f}")
    st.metric("Custo Estimado", f"{custo_total:,.2f} KZ")
    
    st.write(f"**Detalhes Técnicos:**")
    st.write(f"- Volume de argamassa: {volume_total:.3f} m³")
    st.write(f"- Cimento necessário: {volume_cimento:.3f} m³")