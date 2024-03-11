import streamlit as st

def main():
    st.title('Apresentação de SSMA')
    st.write('Bem-vindo à apresentação sobre Saúde, Segurança e Meio Ambiente (SSMA).')

    st.header('O que é SSMA?')
    st.write('SSMA é uma abordagem integrada para garantir a saúde e a segurança dos funcionários, bem como a proteção do meio ambiente em um local de trabalho.')

    st.header('Objetivos de SSMA')
    st.write('Os principais objetivos de SSMA incluem:')
    st.markdown("""
    - **Proteger a saúde e a segurança dos funcionários**: Isso é alcançado através da identificação e eliminação de riscos ocupacionais, fornecendo treinamento adequado e implementando medidas preventivas.
    - **Preservar o meio ambiente**: Minimizando a poluição, reduzindo o desperdício e adotando práticas sustentáveis.
    - **Cumprir regulamentações e normas**: Assegurando que todas as atividades da empresa estejam em conformidade com as leis e regulamentos ambientais e de segurança.
    - **Promover uma cultura de segurança**: Incentivando a conscientização, responsabilidade e participação de todos os funcionários na promoção da segurança no local de trabalho.
    """)

    st.header('Componentes de SSMA')
    st.write('SSMA geralmente engloba os seguintes componentes:')
    st.markdown("""
    - **Saúde Ocupacional**: Prevenção de lesões e doenças relacionadas ao trabalho, exames médicos regulares, promoção de estilos de vida saudáveis.
    - **Segurança do Trabalho**: Identificação e mitigação de riscos, implementação de medidas de segurança, treinamento em segurança.
    - **Proteção Ambiental**: Gestão de resíduos, conservação de recursos naturais, prevenção da poluição.
    """)

    st.header('Benefícios de SSMA')
    st.write('A implementação eficaz de SSMA pode trazer vários benefícios para uma organização, incluindo:')
    st.markdown("""
    - Redução de acidentes e lesões
    - Melhoria da produtividade
    - Redução de custos relacionados a acidentes de trabalho e danos ambientais
    - Melhoria da reputação da empresa
    - Cumprimento de regulamentações legais
    """)

    st.header('Conclusão')
    st.write('SSMA é uma parte essencial de qualquer operação empresarial responsável. Ao priorizar a saúde, segurança e o meio ambiente, as organizações podem garantir um ambiente de trabalho mais seguro, saudável e sustentável para todos os envolvidos.')

if __name__ == "__main__":
    main()
