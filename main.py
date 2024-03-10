import streamlit as st
import pandas as pd
from datetime import datetime

# Carregar dados do Excel
excel_file = 'SSMA.xlsx'
selected_sheet_name = 'Sheet1'

# Carregar dados
def load_data():
    try:
        df = pd.read_excel(excel_file, sheet_name=selected_sheet_name)
    except FileNotFoundError:
        st.error(f"Arquivo {excel_file} não encontrado. Um novo arquivo será criado.")
        df = pd.DataFrame(columns=["DATA", "HORA", "CLASS. EVENTO", "DESC. EVENTO", "UNIDADE", "TP.OCORRENCIA", "EMBARCADOR", "OCORRENCIA", "OPERAÇÃO", "VOL.", "CAVALO", "CARRETA", "MOTORISTA", "TRANSPORTADORA", "NF", "CLIENTE", "MÊS DO EVENTO", "ANO DO EVENTO"])
    return df

df = load_data()

# Título da aplicação
st.title("Cadastro de Ocorrência 📝")

# Opção de seleção no sidebar para alternar entre formulário e tabela
opcao = st.sidebar.selectbox("Selecione uma opção:", ["Mostrar Formulário", "Mostrar Tabela"])

# Opções pré-definidas
unidade_options = ["CUBATÃO", "BARUERI", "UBERLÂNDIA", "PAULINIA"]
tipo_ocorrencia_options = ["MÉDIA", "EMERGÊNCIA"]
embarcador_options = ["IPIRANGA", "TOTAL"]
ocorrencia_options = ["AVA", "CONTAMINAÇÃO", "DERRAME", "INCIDENTE"]
operacao_options = ["DISTRIBUIÇÃO", "ENTREGA"]

# Verificar se a opção "Mostrar Formulário" foi selecionada
if opcao == "Mostrar Formulário":
    # Coletar dados da ocorrência através de um formulário
    data = st.date_input("Data da ocorrência:", value=datetime.today())
    hora = st.time_input("Hora da ocorrência:")
    class_evento_options = ["INCIDENTE", "ACIDENTE NÍVEL 1", "ACIDENTE NÍVEL 2", "ACIDENTE NÍVEL 3"]
    class_evento = st.selectbox("Classificação do evento:", class_evento_options)
    desc_evento = st.text_input("Descrição do evento:")
    unidade = st.selectbox("Unidade:", unidade_options)
    tp_ocorrencia = st.selectbox("Tipo de ocorrência:", tipo_ocorrencia_options)
    embarcador = st.selectbox("Embarcador:", embarcador_options)
    ocorrencia = st.selectbox("Ocorrência:", ocorrencia_options)
    operacao = st.selectbox("Operação:", operacao_options)
    vol = st.number_input("Volume:", min_value=0)
    cavalo = st.text_input("Cavalo:")
    carreta = st.text_input("Carreta:")
    motorista = st.text_input("Motorista:")
    transportadora = st.text_input("Transportadora:")
    nf = st.text_input("Nota Fiscal:")
    cliente = st.text_input("Cliente:")


    # Botão para cadastrar a ocorrência
    if st.button("Cadastrar Ocorrência"):
        # Criar um novo registro de ocorrência
        novo_registro = pd.DataFrame({
            "DATA": [datetime.combine(data, hora)],  # Combinar data e hora
            "CLASS. EVENTO": [class_evento],
            "DESC. EVENTO": [desc_evento],
            "UNIDADE": [unidade],
            "TP.OCORRENCIA": [tp_ocorrencia],
            "EMBARCADOR": [embarcador],
            "OCORRENCIA": [ocorrencia],
            "OPERAÇÃO": [operacao],
            "VOL.": [vol],
            "CAVALO": [cavalo],
            "CARRETA": [carreta],
            "MOTORISTA": [motorista],
            "TRANSPORTADORA": [transportadora],
            "NF": [nf],
            "CLIENTE": [cliente],

        })
        # Adicionar o novo registro ao DataFrame
        df = pd.concat([df, novo_registro], ignore_index=True)
        # Salvar os dados atualizados no arquivo Excel
        df.to_excel(excel_file, index=False)
        st.success("Ocorrência cadastrada com sucesso!")

# Verificar se a opção "Mostrar Tabela" foi selecionada
if opcao == "Mostrar Tabela":
    # Exibir a tabela de ocorrências
    st.header("Ocorrências Cadastradas")
    st.write(df)
