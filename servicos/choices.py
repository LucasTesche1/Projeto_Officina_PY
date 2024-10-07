from django.db.models import TextChoices

class ChoicesCategoriaManutencao (TextChoices):
    TROCAR_VALVULA_MOTOR = "TVM", "Trocar válvula do motor"
    TROCAR_OLEO = "TO", "Trocar o óleo"
    BALANCEAMENTO = "B", "Balanceamento"
    ALINHAMENTO = "A", "Alinhamento"
    TROCAR_PNEU = "TP", "Trocar pneu"
    REVISAO_FREIOS = "RF", "Revisão dos freios"
    TROCAR_BATERIA = "TB", "Trocar bateria"
    LIMPEZA_BICO_INJETOR = "LBI", "Limpeza de bico injetor"
    TROCAR_CORREIA = "TC", "Trocar correia dentada"
    VERIFICACAO_SUSPENSAO = "VS", "Verificação de suspensão"
    TROCAR_AMORTECEDOR = "TA", "Trocar amortecedor"
    TROCAR_FILTRO_AR = "TFA", "Trocar filtro de ar"
    TROCAR_FILTRO_COMBUSTIVEL = "TFC", "Trocar filtro de combustível"
    TROCAR_PASTILHA_FREIO = "TPF", "Trocar pastilha de freio"
    REGULAGEM_EMBRIAGEM = "RE", "Regulagem de embreagem"
    ALINHAMENTO_FAROL = "AF", "Alinhamento do farol"
    REPARO_AR_CONDICIONADO = "RAC", "Reparo no ar condicionado"
    TROCA_LAMPADAS = "TL", "Troca de lâmpadas"