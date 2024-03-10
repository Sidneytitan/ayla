import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import tempfile
import pandas as pd
import os
from reportlab.lib.utils import ImageReader


# Função para gerar PDF
def generate_pdf(driver_list, monitor_name, font_size, file_name, column_positions, distance=5):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as buffer:
        cnv = canvas.Canvas(buffer.name, pagesize=A4)
        cnv.setFontSize(font_size)

        # Desenha o cabeçalho
        x_start = 50
        y = 730  # Posição vertical inicial do cabeçalho
        for header, x_position in column_positions.items():
            cnv.drawString(x_position, y, header)

        # Desenha os detalhes de cada motorista
        for driver_data in driver_list:
            y -= 20  # Move para a próxima linha
            for header, x_position in column_positions.items():
                cnv.drawString(x_position, y, str(driver_data.get(header, '')))

        # Adiciona a imagem PNG (logo)
        logo_path = "logo.png"  # Caminho para a imagem
        logo_size = (80, 30)  # Tamanho da imagem (largura, altura)
        logo_position = (10, A4[1] - logo_size[1] - 10)  # Posição da imagem (horizontal, vertical)
        image = ImageReader(logo_path)
        cnv.drawImage(image, logo_position[0], logo_position[1], width=logo_size[0], height=logo_size[1])

        # Adiciona o nome do motorista monitor no final
        if monitor_name:
            text_width = cnv.stringWidth(f"Motorista Monitor: {monitor_name}")
            x_position = (A4[0] - text_width) / 2  # Centraliza horizontalmente
            y -= 600
            cnv.drawString(x_position, y, f"{monitor_name}")
            cnv.drawString(x_position, y - 15, f"Motorista Monitor")

            # Adiciona um risco com a distância especificada
            risco_x = x_position - 5
            risco_y = y + distance
            cnv.line(risco_x, risco_y, risco_x + text_width + 3, risco_y)

        cnv.save()

        buffer.seek(0)
        pdf = buffer.read()

    return pdf

def main():
    st.title('Gerador de PDF e Excel')

    if 'driver_list' not in st.session_state:
        st.session_state.driver_list = []

    # Adiciona um motorista
    st.markdown('---')
    st.subheader("Cadastro de Motorista")
    with st.expander("Preencha os dados do motorista"):
        col1, col2 = st.columns(2)  # Divide em duas colunas

        with col1:
            id_motorista = st.text_input('ID do Motorista')
            nome_motorista = st.text_input('Nome do Motorista')
            cpf = st.text_input('CPF')

        with col2:
            infracao = st.text_input('Infração')
            data = st.date_input('Data')
            horario = st.time_input('Horário')
            tipo_contato = st.selectbox('Tipo de Contato', ['Telefone', 'E-mail', 'WhatsApp'])

        if st.button('Adicionar Motorista'):
            data_dict = {
                'ID': id_motorista,
                'Nome do Motorista': nome_motorista,
                'CPF': cpf,
                'Infração': infracao,
                'Data': data,
                'Horário': horario,
                'Tipo de Contato': tipo_contato
            }

            st.session_state.driver_list.append(data_dict)
            st.success("Motorista adicionado com sucesso!")

    # Adiciona o nome do motorista monitor
    st.markdown('---')
    st.subheader("Cadastro do Motorista Monitor")
    with st.expander("Preencha o nome do motorista monitor"):
        monitor_name = st.text_input('Nome do Motorista Monitor')

    # Defina a distância entre o texto e o risco
    distance = 10  # Defina a distância desejada aqui

    # Mostra os detalhes do motorista monitor
    if monitor_name:
        st.subheader("Detalhes do Motorista Monitor")
        st.write(f"Nome do Motorista Monitor: {monitor_name}")



    # Defina as posições iniciais das colunas do cabeçalho
    column_positions = {
        'ID': 50,
        'Nome do Motorista': 100,
        'CPF': 250,
        'Infração': 320,
        'Data': 365,
        'Horário': 415,
        'Tipo de Contato': 460
    }

    # Mostra os motoristas cadastrados
    if st.session_state.driver_list:
        st.markdown('---')
        st.subheader("Motoristas Cadastrados")
        for i, driver_data in enumerate(st.session_state.driver_list):
            st.markdown('---')
            st.subheader(f"Motorista {i+1}")
            st.write(f"ID: {driver_data['ID']}")
            st.write(f"Nome: {driver_data['Nome do Motorista']}")
            st.write(f"CPF: {driver_data['CPF']}")
            st.write(f"Infração: {driver_data['Infração']}")
            st.write(f"Data: {driver_data['Data']}")
            st.write(f"Horário: {driver_data['Horário']}")
            st.write(f"Tipo de Contato: {driver_data['Tipo de Contato']}")

    # Botão para gerar PDF e salvar Excel
    if st.button('Gerar PDF e Salvar Excel'):
        if st.session_state.driver_list:
            # Gerar PDF
            pdf = generate_pdf(st.session_state.driver_list, monitor_name, 8, "Meu_pdf.pdf", column_positions, distance=distance)
            st.download_button(label="Baixar PDF", data=pdf, file_name="SSMA_pdf.pdf", mime="application/pdf")

            # Salvar Excel
            excel_file = "motoristas.xlsx"
            if os.path.isfile(excel_file):
                existing_df = pd.read_excel(excel_file)
                new_df = pd.DataFrame(st.session_state.driver_list)
                updated_df = pd.concat([existing_df, new_df], ignore_index=True)
                updated_df.to_excel(excel_file, index=False)
            else:
                df = pd.DataFrame(st.session_state.driver_list)
                df.to_excel(excel_file, index=False)
            st.success(f"Dados dos motoristas salvos nos registros.")

if __name__ == '__main__':
    main()