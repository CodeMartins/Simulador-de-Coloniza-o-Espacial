def main():
    print("=== Simulador de Decolagem de Foguete Espacial ===")

    # Tamanho do foguete
    area_foguete = float(input("Tamanho do foguete (m²): "))
    altura_foguete = float(input("Altura do foguete (m): "))
    volume_foguete = area_foguete * altura_foguete  # m³

    # Recursos (todos em kg/m²)
    sementes = float(input("Quantidade de sementes (kg/m²): "))
    racao_humana = float(input("Quantidade de ração humana (kg/m²): "))
    medicamentos = float(input("Quantidade de medicamentos (kg/m²): "))
    ferramentas = float(input("Quantidade de ferramentas (kg/m²): "))

   # Água (antes do combustível)
    agua = float(input("Quantidade de água (litros/m³): "))


    # Humanos e óvulos
    homens = int(input("Quantidade de homens: "))
    mulheres = int(input("Quantidade de mulheres: "))
    ovulos = int(input("Óvulos fecundados congelados: "))

    # ======= Cálculo do espaço e peso =======
    # Cada humano ocupa 1 m²
    espaco_humanos = homens + mulheres  # m²

    # Recursos ocupam m² conforme seus valores
    espaco_sementes = sementes
    espaco_racao = racao_humana
    espaco_medicamentos = medicamentos
    espaco_ferramentas = ferramentas

    # Cálculo parcial do peso total para estimar combustível mínimo
    peso_parcial = (
        sementes + racao_humana + medicamentos + ferramentas
    ) * area_foguete + (homens + mulheres) * 70 + agua * 1  # sem o combustível ainda

    combustivel_minimo = (peso_parcial / 100) * 30  # estimativa mínima

    print(f"⚠️ Para a carga atual, o combustível mínimo necessário para decolagem será cerca de {combustivel_minimo:.2f} litros.")

    # Agora pergunta ao usuário quanto de combustível deseja adicionar
    combustivel_disponivel = float(input("Informe a quantidade de combustível (litros/m³): "))

    # Água e combustível ocupam m³ diretamente
    volume_agua = agua
    volume_combustivel = combustivel_disponivel

    # Espaço total ocupado (m² convertido para m³ assumindo altura = 1m)
    volume_total_ocupado = (
        espaco_humanos +
        espaco_sementes +
        espaco_racao +
        espaco_medicamentos +
        espaco_ferramentas
    ) + volume_agua + volume_combustivel  # m³

    # Peso total aproximado (em kg)
    peso_total = (
        sementes + racao_humana + medicamentos + ferramentas
    ) * area_foguete + (homens + mulheres) * 70 + agua * 1 + combustivel_disponivel * 0.8

    # ======= Cálculo da quantidade mínima de combustível =======
    # Estimativa com base na Lei de Hess (energia necessária proporcional ao peso)
    # Aproximação: 30 litros de combustível por 100 kg de massa
    combustivel_minimo = (peso_total / 100) * 30  # litros

    print("\n=== RELATÓRIO ===")
    print(f"Volume total do foguete (m³): {volume_foguete:.2f}")
    print(f"Volume ocupado (m³): {volume_total_ocupado:.2f}")
    print(f"Peso total da carga (kg): {peso_total:.2f}")
    print(f"Combustível disponível (litros): {combustivel_disponivel:.2f}")
    print(f"Combustível mínimo necessário (litros): {combustivel_minimo:.2f}")

    # ======= Verificações =======
    if volume_total_ocupado > volume_foguete:
        print("❌ O foguete está com excesso de volume. Não pode decolar.")
    elif combustivel_disponivel < combustivel_minimo:
        print("❌ Combustível insuficiente para decolagem.")
    else:
        print("✅ Foguete pronto para decolar!")

if __name__ == "__main__":
    main()
