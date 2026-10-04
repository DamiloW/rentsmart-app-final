"""
Módulo Principal do sistema RentSmart.
Responsável pela interface com o usuário e geração do orçamento.
"""

import os
from imoveis import Casa, Apartamento, Estudio

def ler_inteiro(mensagem, minimo=None, maximo=None):
    """Solicita um número inteiro e valida seus limites"""

    while True:
        try:
            valor = int(input(mensagem).strip())

            if minimo is not None and valor < minimo:
                print(f"Erro: digite um valor maior ou igual a {minimo}.")
                continue

            if maximo is not None and valor > maximo:
                print(f"Erro: digite um valor menor ou igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Erro: digite apenas um número inteiro válido.")

def ler_sim_nao(mensagem):
    """Solicia uma resposta S/N e valida a entrada"""

    while True:
        resposta = input(mensagem).strip().upper()

        if resposta in ["S", "N"]:
            return resposta == "S"

        print("Erro: responda apenas com S para Sim ou N para Não.")

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
        quarto = ler_inteiro("Quantos quartos (1 ou 2)? ", minimo=1, maximo=2)
        garagem = ler_sim_nao("Possui garagem (S/N)? ")
        imovel_escolhido = Casa(quartos=quarto, tem_garagem=garagem)

        nome_tipo = "Casa"
        nome_arquivo_tipo= "casa"
    
    elif tipo_imovel == "2":
        quarto = ler_inteiro("Quantos quartos (1 ou 2)? ", minimo=1, maximo=2)
        garagem = ler_sim_nao("Possui garagem (S/N)? ")
        crianças = ler_sim_nao("O cliente possui crianças (S/N)? ")

        imovel_escolhido = Apartamento(quartos=quarto, tem_garagem=garagem, tem_criancas=crianças)
        nome_tipo = "Apartamento"
        nome_arquivo_tipo = "apartamento"

    elif tipo_imovel == "3":
        vagas = ler_inteiro("Quantas vagas de garagem o cliente quer? ", minimo=0)

        imovel_escolhido = Estudio(vagas_garagem=vagas)
        nome_tipo = "Estúdio"
        nome_arquivo_tipo = "estudio"

    valor_mensal = imovel_escolhido.calcular_aluguel()

# ==========================================
# DEFINIÇÃO DO PARCELAMENTO DA TAXA
# ==========================================

    print("\nComo o cliente deseja pagar a taxa contratual?")
    print("1 - 1 parcela")
    print("2 - 2 parcelas")
    print("3 - 3 parcelas")
    print("4 - 4 parcelas")
    print("5 - 5 parcelas")

    numero_parcelas = ler_inteiro("Escolha a quantidade de parcelas (1 a 5): ", minimo=1, maximo=5)
    
    valor_taxa = imovel_escolhido.taxa_contratual
    parcela_taxa = valor_taxa / numero_parcelas

# ==========================================
# ORÇAMENTO FINAL
# ==========================================

    print("\n" + "=" * 45)
    print("          ORÇAMENTO FINAL          ")
    print("=" * 45)
    
    print(f"Tipo de Imóvel...........: {nome_tipo}")
    print(f"Valor Base...............: R$ {imovel_escolhido.valor_base:.2f}")
    print(f"Adicionais...............: R$ {imovel_escolhido.valor_adicionais:.2f}")
    

    if imovel_escolhido.valor_desconto > 0:
        print(f"Desconto Aplicado........: R$ {imovel_escolhido.valor_desconto:.2f} (5% off)")

    print(f"Valor do Aluguel.........: R$ {valor_mensal:.2f} / mês")
    print("=" *45)
    print(f"Taxa Contratual..........: R$ {imovel_escolhido.taxa_contratual:.2f}")
    print(f"Parcelamento da Taxa.....: R$ {parcela_taxa:.2f} / mês")
    print("=" *45)
    print(f"Valor nos primeiros {numero_parcelas} meses..: R$ {valor_mensal + parcela_taxa:.2f} / mês")
    print(f"Valor após o término da taxa ................: R$ {valor_mensal:.2f} / mês")
    print("=" *45)


# ==========================================
# GERAÇÃO DO ARQUIVO CSV DE PROJEÇÃO
# ==========================================

    numero = 1

    while True:
        nome_arquivo = f"projecao_12_meses_{nome_arquivo_tipo}_{numero}.csv"

        if not os.path.exists(nome_arquivo):
            break

        numero += 1

    with open(nome_arquivo, mode='w', encoding='utf-8') as arquivo:
        arquivo.write("Mes,Valor_Aluguel,Parcela_Taxa_Contrato,Total_a_Pagar\n")

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