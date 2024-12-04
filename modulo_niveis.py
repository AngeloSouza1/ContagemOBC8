def calcular_niveis_exclusivos(experiencias):
    """
    Calcula o número total de níveis alcançados com base na experiência fornecida,
    contabilizando apenas valores que sozinhos completam múltiplos de 200.

    Args:
    experiencias (list): Lista de inteiros representando a experiência ganha em cada aventura.

    Returns:
    int: Número total de níveis alcançados.
    """
    niveis = 0

    for experiencia in experiencias:
        if experiencia >= 200:
            niveis += experiencia // 200

    return niveis
