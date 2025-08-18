import math
from datetime import datetime

class HumanSurvivalCalculator:
    def __init__(self):
        # Fatores críticos para a sobrevivência humana
        self.factors = {
            'climate_stability': {'weight': 0.15, 'value': None},
            'food_security': {'weight': 0.12, 'value': None},
            'water_availability': {'weight': 0.12, 'value': None},
            'air_quality': {'weight': 0.08, 'value': None},
            'biodiversity': {'weight': 0.07, 'value': None},
            'ozone_layer': {'weight': 0.05, 'value': None},
            'temperature_range': {'weight': 0.06, 'value': None},
            'radiation_levels': {'weight': 0.05, 'value': None},
            'atmospheric_composition': {'weight': 0.06, 'value': None},
            'soil_quality': {'weight': 0.05, 'value': None},
            'natural_disasters': {'weight': 0.04, 'value': None},
            'disease_prevalence': {'weight': 0.05, 'value': None},
            'technology_development': {'weight': 0.05, 'value': None},
            'social_stability': {'weight': 0.05, 'value': None}
        }
        
        # Valores ideais para cada fator (escala 0-100)
        self.ideal_values = {
            'climate_stability': 90,
            'food_security': 95,
            'water_availability': 95,
            'air_quality': 90,
            'biodiversity': 85,
            'ozone_layer': 90,
            'temperature_range': 85,
            'radiation_levels': 95,
            'atmospheric_composition': 90,
            'soil_quality': 80,
            'natural_disasters': 80,
            'disease_prevalence': 85,
            'technology_development': 70,
            'social_stability': 75
        }
    
    def get_current_year_factor(self):
        """Fator de degradação baseado no ano atual"""
        current_year = datetime.now().year
        # Quanto mais longe de 2000, pior a situação (simplificação)
        base_year = 2000
        years_diff = current_year - base_year
        degradation = min(1.0, years_diff * 0.002)  # 0.2% de degradação por ano
        return 1 - degradation
    
    def calculate_factor_score(self, factor, current_value):
        """Calcula a pontuação normalizada para um fator específico"""
        ideal = self.ideal_values[factor]
        # Penaliza valores abaixo do ideal, mas não recompensa valores acima
        score = min(100, current_value) / ideal
        return max(0, min(1, score))  # Garante que está entre 0 e 1
    
    def input_factors(self):
        """Solicita ao usuário os valores atuais para cada fator"""
        print("Por favor, insira os valores atuais para cada fator (0-100):")
        for factor in self.factors:
            while True:
                try:
                    value = float(input(f"{factor.replace('_', ' ').title()}: "))
                    if 0 <= value <= 100:
                        self.factors[factor]['value'] = value
                        break
                    else:
                        print("Por favor, insira um valor entre 0 e 100.")
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número.")
    
    def calculate_survival_probability(self):
        """Calcula a probabilidade total de sobrevivência"""
        if any(v['value'] is None for v in self.factors.values()):
            raise ValueError("Todos os fatores devem ter valores atribuídos.")
        
        total_score = 0
        total_weight = sum(f['weight'] for f in self.factors.values())
        
        for factor, data in self.factors.items():
            factor_score = self.calculate_factor_score(factor, data['value'])
            weighted_score = factor_score * data['weight']
            total_score += weighted_score
        
        # Ajusta pelo fator temporal
        year_factor = self.get_current_year_factor()
        total_score *= year_factor
        
        # Normaliza para o peso total (que pode não ser exatamente 1)
        survival_prob = (total_score / total_weight) * 100
        
        return max(0, min(100, survival_prob))  # Garante que está entre 0 e 100
    
    def get_survival_assessment(self, probability):
        """Retorna uma avaliação qualitativa baseada na probabilidade"""
        if probability >= 90:
            return "Excelente - Condições ideais para sobrevivência humana a longo prazo"
        elif probability >= 75:
            return "Boa - Condições estáveis para sobrevivência humana"
        elif probability >= 60:
            return "Moderada - Alguns riscos significativos, mas gerenciáveis"
        elif probability >= 40:
            return "Preocupante - Riscos substanciais à sobrevivência humana"
        elif probability >= 20:
            return "Crítica - Sobrevivência humana em risco a médio prazo"
        else:
            return "Extrema - Sobrevivência humana severamente comprometida"

# Exemplo de uso
if __name__ == "__main__":
    calculator = HumanSurvivalCalculator()
    
    print("=== Calculadora de Taxa de Sobrevivência Humana na Terra ===")
    print("Este programa estima a probabilidade de sobrevivência humana com base")
    print("em diversos fatores ambientais e sociais.\n")
    
    # Opção para usar valores padrão ou inserir manualmente
    use_default = input("Deseja usar valores padrão aproximados? (s/n): ").lower()
    
    if use_default == 's':
        # Valores padrão (fictícios para exemplo)
        default_values = {
            'climate_stability': 65,
            'food_security': 75,
            'water_availability': 70,
            'air_quality': 60,
            'biodiversity': 55,
            'ozone_layer': 75,
            'temperature_range': 60,
            'radiation_levels': 85,
            'atmospheric_composition': 70,
            'soil_quality': 65,
            'natural_disasters': 50,
            'disease_prevalence': 60,
            'technology_development': 80,
            'social_stability': 55
        }
        
        for factor, value in default_values.items():
            calculator.factors[factor]['value'] = value
    else:
        calculator.input_factors()
    
    # Calcula e exibe os resultados
    probability = calculator.calculate_survival_probability()
    assessment = calculator.get_survival_assessment(probability)
    
    print("\n=== Resultados ===")
    print(f"Probabilidade Estimada de Sobrevivência: {probability:.1f}%")
    print(f"Avaliação: {assessment}")
    
    # Exibe detalhes dos fatores
    print("\nDetalhes dos Fatores:")
    for factor, data in calculator.factors.items():
        factor_name = factor.replace('_', ' ').title()
        ideal = calculator.ideal_values[factor]
        score = calculator.calculate_factor_score(factor, data['value']) * 100
        print(f"{factor_name}: {data['value']:.1f} (Ideal: {ideal}, Score: {score:.1f}%)")
    
    print("\nNota: Esta é uma estimativa simplificada para fins ilustrativos.")
    print("Muitos outros fatores podem influenciar a sobrevivência humana.")