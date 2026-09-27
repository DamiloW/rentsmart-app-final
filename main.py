"""
Módulo Principal do sistema RentSmart.
Responsável pela interface com o usuário e geração do orçamento.
"""

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

    Valor_mensal = imovel_escolhido.calcular_aluguel()

    print("\n" + "=" * 45)
    print("          ORÇAMENTO FINAL          ")
    print("=" * 45)
    print(f"Tipo de Imóvel..........: {nome_tipo}")
    print(f"Taxa Contratual.........: R$ {imovel_escolhido.taxa_contratual:.2f} (Pode ser parcelada em 5x)")

    if imovel_escolhido.valor_desconto > 0:
        print(f"Desconto Aplicado........: R$ {imovel_escolhido.valor_desconto:.2f} (5% off)")

    print(f"Valor do Aluguel........: R$ {Valor_mensal:.2f} / mês")
    print("=" *45)

if __name__ == "__main__":
    iniciar_atendimento()