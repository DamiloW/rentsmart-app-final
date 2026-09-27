"""
Módulo contendo as classes dos imóveis da R.M Imóveis
Desenvolvido para o sistema RentSmart.
"""

class Imovel:
    """Classe base que representa as regras gerais da imobiliária"""

    def __init__(self):
        """
        Método construtor: inicializa os atributos comuns a todos os imóveis.
        """
        self.taxa_contratual = 2000.00
        self.valor_base = 0.0
        self.valor_adicionais = 0.0
        self.valor_desconto = 0.0

class Casa(Imovel):
    """
    Representa uma Casa, herdando as regras gerais de Imovel.
    """

    def __init__(self, quartos, tem_garagem):
        """
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos específicos de uma casa.
        """
        super().__init__()
        self.quartos = quartos
        self.tem_garagem = tem_garagem
        self.valor_base = 900.000

    def calcular_aluguel(self):
        """
        Aplica as regras matemáticas para calcular o aluguel da Casa.
        """
        self.valor_adicionais = 0.0

        if self.quartos == 2:
            self.valor_adicionais += 250.00

        if self.tem_garagem == True:
            self.valor_adicionais += 300.00

        return self.valor_base + self.valor_adicionais

class Apartamento(Imovel):
    """
    Representa um Apartamento, herdando de Imovel, com regra especial de desconto.
    """

    def __init__(self, quartos, tem_garagem, tem_criancas):
        """
        Inicializa os atributos, incluindo a verificação de crianças para o desconto.
        """
        super().__init__()

        self.quartos = quartos
        self.tem_garagem = tem_garagem
        self.tem_criancas = tem_criancas
        self.valor_base = 700.00

    def calcular_aluguel(self):
        """
        Calcular o aluguel aplicando adicionais e o desconto de 5% se aplicável.
        """
        self.valor_adicionais = 0.0
        self.valor_desconto = 0.0

        if self.quartos == 2:
            self.valor_adicionais += 200.00

        if self.tem_garagem == True:
            self.valor_adicionais += 300.00

        subtotal = self.valor_base + self.valor_adicionais

        if self.tem_criancas == False:
            self.valor_desconto = subtotal * 0.05

        return subtotal - self.valor_desconto

class Estudio(Imovel):
    """
    Representa um Estúdio, herdadando de Imovel, com regra especial para garagem.
    """

    def __init__(self, vagas_garagem):
        """
        Inicializa os atributos, recebendo a quantidade exata de vagas de garagem.
        """
        super().__init__()

        self.vagas_garagem = vagas_garagem
        self.valor_base = 1200.00

    def calcular_aluguel(self):
        """
        Calcula o aluguel aplicando a regra de pacotes de garagem.
        """
        self.valor_adicionais = 0.0

        if self.vagas_garagem > 0:
            if self.vagas_garagem <= 2:
                self.valor_adicionais += 250.00
            else:
                vagas_extras = self.vagas_garagem - 2
                self.valor_adicionais += 250.00 + (vagas_extras * 60.00)

        return self.valor_base + self.valor_adicionais

# ==========================================
# ÁREA DE TESTES (Desenvolvimento Incremental)
# ==========================================

if __name__ == "__main__":
    meu_apto_teste = Apartamento(quartos=2, tem_garagem=True, tem_criancas=False)

    print("\n--- Teste da Classe Estudio ---")
    # Vamos testar um estúdio com 3 vagas. 
    # Conta esperada: 1200 (base) + 250 (pelas 2 primeiras vagas) + 60 (pela 3ª vaga) = R$ 1510.00
    meu_estudio_teste = Estudio(vagas_garagem=3)
    valor_final_estudio = meu_estudio_teste.calcular_aluguel()
    
    print(f"Taxa de contrato herdada: R$ {meu_estudio_teste.taxa_contratual:.2f}")
    print(f"Aluguel mensal calculado: R$ {valor_final_estudio:.2f}")
