import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError

def main():

    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
    email = st.text_input("Campo de texto para inserção do email do vendedor.")
    data = st.date_input("Data da Compra", datetime.now())
    hora = st.time_input("Hora da Compra", value=time(9, 0)) #Valor padrão: 09:00
    valor = st.number_input("Valor da Venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de Produto(s)", min_value=1, step=1)
    produto = st.selectbox("Produto", options=["ZapFlow com Gemini", "ZapFlow com chatGPT", "ZapFlow com Llama3.0"])

    if st.button("Salvar"):

        try:
            data_hora = datetime.combine(data, hora)
            
            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )

            st.write(venda)
        except ValidationError as e:
            st.error(f"Deu Erro {e}")

if __name__=="__main__":
    main()

