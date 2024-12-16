from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCAR_OLEO_MOTOR = "TO", "Trocar óleo do motor" 
    TROCAR_PECA_MOTOR = "TPM", "Trocar peça do motor"
    TROCAR_PECA_SUSPENSAO = "TPS", "Trocar peça da suspensão"
    TROCAR_PECA_INJECAO = "TPI", "Trocar peça da injecao"
    BALACEAMENTO = "BA", "Balancelamento"
    ALINHAMENTO = "AL", "Alinhamento"