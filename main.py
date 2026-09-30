"""
Módulo Principal do sistema RentSmart.
Responsável pela interface com o usuário e geração do orçamento.
"""

import os
from imoveis import Casa, Apartamento, Estudio

def iniciar_atendimento():
    """Função principal que gerencia a interação com o usuário."""
    print("=" * 45)
    print("     BEM-VINDO AO RENTSMART - R.M IMÓVEIS     ")
    print("=" * 45)

    tipo_imovel = ""

    while tipo_imovel not in ["1", "2", "3"]:
        print("\nQual tipo de imóvel o cliente deseja orçar?")
        print("1 - Casa")
        print("2 - Apartamento")
        print("3 - Estúdio")
        tipo_imovel = input("Digite a opção (1 , 2 ou 3): ").strip()

        if tipo_imovel not in ["1", "2", "3"]:
            print("Erro: Opção inválida! Por favor, digite 1, 2 ou 3.")

    print("\nÓtimo! Vamos preencher os detalhes do imóvel...")

    if tipo_imovel == "1":
        quarto = int(input("Quantos quartos (1 ou 2)? "))
        garagem = (input)("Possui garagem (S/N)? ").strip().upper() == "S"

        imovel_escolhido = Casa(quartos=quarto, tem_garagem=garagem)
        nome_tipo = "Casa"
    
    elif tipo_imovel == "2":
        quarto = int(input("Quantos quartos (1 ou 2)? "))
        garagem = input("Possui garagem (S/N)? ").strip().upper() == "S"
        crianças = input("O cliente possui crianças (S/N)? ").strip().upper() == "S"

        imovel_escolhido = Apartamento(quartos=quarto, tem_garagem=garagem, tem_criancas=crianças)
        nome_tipo = "Apartamento"

    elif tipo_imovel == "3":
        vagas = int(input("Quantas vagas de garagem o cliente quer? "))

        imovel_escolhido = Estudio(vagas_garagem=vagas)
        nome_tipo = "Estúdio"

    valor_mensal = imovel_escolhido.calcular_aluguel()

    print("\n" + "=" * 45)
    print("          ORÇAMENTO FINAL          ")
    print("=" * 45)
    print(f"Tipo de Imóvel..........: {nome_tipo}")
    print(f"Taxa Contratual.........: R$ {imovel_escolhido.taxa_contratual:.2f} (Pode ser parcelada em 5x)")

    if imovel_escolhido.valor_desconto > 0:
        print(f"Desconto Aplicado........: R$ {imovel_escolhido.valor_desconto:.2f} (5% off)")

    print(f"Valor do Aluguel........: R$ {valor_mensal:.2f} / mês")
    print("=" *45)

# ==========================================
# GERAÇÃO DO ARQUIVO CSV DE PROJEÇÃO
# ==========================================

    numero = 1

    while True:
        nome_arquivo = f"projecao_12_meses_{nome_tipo.lower()}_{numero}.csv"

        if not os.path.exists(nome_arquivo):
            break

        numero += 1

    with open(nome_arquivo, mode='w', encoding='utf-8') as arquivo:
        arquivo.write("Mes,Valor_Aluguel,Parcela_Taxa_Contrato,Total_a_Pagar\n")

        parcela_taxa = imovel_escolhido.taxa_contratual / 5

        for mes in range(1, 13):
            if mes <= 5:
                taxa_mes = parcela_taxa
            else:
                taxa_mes = 0.0

            total_mes = valor_mensal + taxa_mes

            arquivo.write(f"{mes},{valor_mensal:.2f},{taxa_mes:.2f},{total_mes:.2f}\n")

    print(f"\n[SUCESSO] O arquivo '{nome_arquivo}' foi gerado na sua pasta com a prosposta de 1 ano!")

if __name__ == "__main__":
    iniciar_atendimento()