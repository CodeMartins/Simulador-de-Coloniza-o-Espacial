import matplotlib.pyplot as plt
import numpy as np
from enum import Enum
from dataclasses import dataclass
import math

@dataclass
class PlanetData:
    name: str
    distance_au: float  # Distância em Unidades Astronômicas
    travel_time_years: float  # Tempo estimado de viagem em anos
    star_distance: float  # Distância da estrela em AU
    habitable_zone: bool
    climate_stability: int
    food_security: int
    water_availability: int
    air_quality: int
    biodiversity: int
    ozone_layer: int
    temperature_range: int
    radiation_levels: int
    atmospheric_composition: int
    soil_quality: int
    natural_disasters: int
    disease_prevalence: int
    technology_development: int
    social_stability: int

class PlanetType(Enum):
    TERRA = 1
    MARTE = 2
    EUROPA = 3
    TITÃ = 4
    PROXIMA_B = 5
    TRAPPIST_1E = 6
    PERSONALIZADO = 7

class ColonizationMission:
    def __init__(self):
        self.male_count = 0
        self.female_count = 0
        self.fertilized_eggs = 0
        self.mission_duration = 0  # em anos

class PlanetComparisonTool:
    def __init__(self):
        # Fatores e pesos (como no seu código original)
        self.factors = [
            'climate_stability', 'food_security', 'water_availability',
            'air_quality', 'biodiversity', 'ozone_layer',
            'temperature_range', 'radiation_levels', 'atmospheric_composition',
            'soil_quality', 'natural_disasters', 'disease_prevalence',
            'technology_development', 'social_stability'
        ]
        
        self.weights = {
            'climate_stability': 0.15,
            'food_security': 0.12,
            'water_availability': 0.12,
            'air_quality': 0.08,
            'biodiversity': 0.07,
            'ozone_layer': 0.05,
            'temperature_range': 0.06,
            'radiation_levels': 0.05,
            'atmospheric_composition': 0.06,
            'soil_quality': 0.05,
            'natural_disasters': 0.04,
            'disease_prevalence': 0.05,
            'technology_development': 0.05,
            'social_stability': 0.05
        }

        # Dados reais da NASA e estimativas científicas
        self.real_planets = {
            PlanetType.TERRA: PlanetData(
                name="Terra",
                distance_au=1.0,
                travel_time_years=0,
                star_distance=1.0,
                habitable_zone=True,
                climate_stability=90,
                food_security=95,
                water_availability=95,
                air_quality=90,
                biodiversity=85,
                ozone_layer=90,
                temperature_range=85,
                radiation_levels=95,
                atmospheric_composition=90,
                soil_quality=80,
                natural_disasters=80,
                disease_prevalence=85,
                technology_development=70,
                social_stability=75
            ),
            PlanetType.MARTE: PlanetData(
                name="Marte",
                distance_au=1.52,
                travel_time_years=0.5,  # Com tecnologia atual
                star_distance=1.52,
                habitable_zone=False,
                climate_stability=25,
                food_security=15,
                water_availability=20,
                air_quality=10,
                biodiversity=5,
                ozone_layer=15,
                temperature_range=30,
                radiation_levels=20,
                atmospheric_composition=25,
                soil_quality=40,
                natural_disasters=60,
                disease_prevalence=30,
                technology_development=15,
                social_stability=35
            ),
            PlanetType.EUROPA: PlanetData(
                name="Europa (Júpiter)",
                distance_au=5.2,
                travel_time_years=6,
                star_distance=5.2,
                habitable_zone=False,
                climate_stability=40,
                food_security=20,
                water_availability=90,  # Subsuperfície
                air_quality=5,
                biodiversity=10,
                ozone_layer=0,
                temperature_range=10,
                radiation_levels=10,
                atmospheric_composition=5,
                soil_quality=5,
                natural_disasters=70,
                disease_prevalence=20,
                technology_development=10,
                social_stability=25
            ),
            PlanetType.TITÃ: PlanetData(
                name="Titã (Saturno)",
                distance_au=9.5,
                travel_time_years=7,
                star_distance=9.5,
                habitable_zone=False,
                climate_stability=30,
                food_security=10,
                water_availability=5,  # Metano líquido
                air_quality=15,
                biodiversity=0,
                ozone_layer=0,
                temperature_range=5,
                radiation_levels=50,
                atmospheric_composition=40,
                soil_quality=30,
                natural_disasters=50,
                disease_prevalence=10,
                technology_development=15,
                social_stability=20
            ),
            PlanetType.PROXIMA_B: PlanetData(
                name="Proxima Centauri b",
                distance_au=268770,  # ~4.24 anos-luz
                travel_time_years=6300,  # Com tecnologia atual
                star_distance=0.0485,
                habitable_zone=True,
                climate_stability=60,
                food_security=40,
                water_availability=70,
                air_quality=50,
                biodiversity=30,
                ozone_layer=40,
                temperature_range=60,
                radiation_levels=40,
                atmospheric_composition=50,
                soil_quality=50,
                natural_disasters=60,
                disease_prevalence=50,
                technology_development=5,
                social_stability=40
            ),
            PlanetType.TRAPPIST_1E: PlanetData(
                name="TRAPPIST-1e",
                distance_au=395369,  # ~6 anos-luz
                travel_time_years=9000,  # Com tecnologia atual
                star_distance=0.029,
                habitable_zone=True,
                climate_stability=55,
                food_security=45,
                water_availability=80,
                air_quality=60,
                biodiversity=35,
                ozone_layer=50,
                temperature_range=55,
                radiation_levels=45,
                atmospheric_composition=55,
                soil_quality=45,
                natural_disasters=55,
                disease_prevalence=45,
                technology_development=5,
                social_stability=45
            )
        }
        
        self.current_mission = None
        self.custom_planet = None

    def input_mission_parameters(self):
        """Coleta dados sobre a missão de colonização"""
        print("\n" + "="*50)
        print("PARÂMETROS DA MISSÃO DE COLONIZAÇÃO")
        print("="*50 + "\n")
        
        mission = ColonizationMission()
        
        while True:
            try:
                mission.male_count = int(input("Número de colonos masculinos: "))
                mission.female_count = int(input("Número de colonos femininos: "))
                mission.fertilized_eggs = int(input("Número de óvulos fecundados congelados: "))
                mission.mission_duration = float(input("Duração planejada da missão (anos): "))
                
                if mission.male_count >= 0 and mission.female_count >= 0 and mission.fertilized_eggs >= 0 and mission.mission_duration > 0:
                    break
                else:
                    print("Todos os valores devem ser positivos!")
            except ValueError:
                print("Por favor, insira números válidos.")
        
        self.current_mission = mission

    def calculate_population_growth(self, planet_score):
        """Calcula o crescimento populacional baseado na viabilidade do planeta"""
        if not self.current_mission:
            return 0, 0
        
        # Fator de viabilidade reprodutiva (0-1)
        reproductive_factor = planet_score / 100 * 0.8  # Máximo de 80% de eficiência
        
        # Cálculos básicos de crescimento populacional
        fertile_couples = min(self.current_mission.male_count, self.current_mission.female_count)
        potential_births = fertile_couples * (self.current_mission.mission_duration / 1.5)  # Considerando 1.5 anos entre gestações
        
        # Efeito dos óvulos fecundados
        egg_contribution = self.current_mission.fertilized_eggs * 0.9  # 90% de sucesso
        
        total_children = (potential_births + egg_contribution) * reproductive_factor
        
        # Mortalidade infantil estimada
        survival_rate = 0.7 + (planet_score / 100 * 0.3)  # Entre 70% e 100%
        surviving_children = total_children * survival_rate
        
        return int(total_children), int(surviving_children)

    def input_custom_planet(self):
        """Permite ao usuário criar um planeta personalizado"""
        print("\n" + "="*50)
        print("CRIAR PLANETA PERSONALIZADO")
        print("="*50 + "\n")
        
        name = input("Nome do planeta: ")
        
        # Coletar dados astronômicos
        print("\nDados Astronômicos:")
        distance_au = float(input("Distância da Terra (UA): "))
        travel_time = float(input("Tempo estimado de viagem (anos): "))
        star_distance = float(input("Distância da estrela (UA): "))
        habitable = input("Está na zona habitável? (s/n): ").lower() == 's'
        
        # Coletar dados de sobrevivência
        print("\nFatores de Sobrevivência (0-100):")
        factors = {}
        for factor in self.factors:
            while True:
                try:
                    value = int(input(f"{factor.replace('_', ' ').title()}: "))
                    if 0 <= value <= 100:
                        factors[factor] = value
                        break
                    else:
                        print("Valor deve estar entre 0 e 100")
                except ValueError:
                    print("Por favor, insira um número válido")
        
        # Criar objeto PlanetData
        self.custom_planet = PlanetData(
            name=name,
            distance_au=distance_au,
            travel_time_years=travel_time,
            star_distance=star_distance,
            habitable_zone=habitable,
            climate_stability=factors['climate_stability'],
            food_security=factors['food_security'],
            water_availability=factors['water_availability'],
            air_quality=factors['air_quality'],
            biodiversity=factors['biodiversity'],
            ozone_layer=factors['ozone_layer'],
            temperature_range=factors['temperature_range'],
            radiation_levels=factors['radiation_levels'],
            atmospheric_composition=factors['atmospheric_composition'],
            soil_quality=factors['soil_quality'],
            natural_disasters=factors['natural_disasters'],
            disease_prevalence=factors['disease_prevalence'],
            technology_development=factors['technology_development'],
            social_stability=factors['social_stability']
        )

    def calculate_survival_score(self, planet_data):
        """Calcula a pontuação de sobrevivência (0-100)"""
        total_score = 0
        for factor in self.factors:
            value = getattr(planet_data, factor)
            weighted = (value / 100) * self.weights[factor]
            total_score += weighted
        
        # Ajuste para planetas na zona habitável
        if planet_data.habitable_zone:
            total_score = min(100, total_score * 1.1)  # Bônus de 10%
        
        return total_score * 100

    def show_comparison(self):
        """Mostra a comparação detalhada"""
        if not self.custom_planet and not hasattr(self, 'selected_planet'):
            print("\nPor favor, selecione ou crie um planeta primeiro.")
            return
        
        planet = self.custom_planet if self.custom_planet else self.selected_planet
        earth = self.real_planets[PlanetType.TERRA]
        
        earth_score = self.calculate_survival_score(earth)
        planet_score = self.calculate_survival_score(planet)
        
        # Cálculo de crescimento populacional
        if self.current_mission:
            potential, surviving = self.calculate_population_growth(planet_score)
        
        print("\n" + "="*50)
        print("ANÁLISE COMPARATIVA DE HABITABILIDADE")
        print("="*50 + "\n")
        
        print(f"=== DADOS ASTRONÔMICOS ===")
        print(f"{'Nome':<25}: {planet.name}")
        print(f"{'Distância da Terra (UA)':<25}: {planet.distance_au:.2f}")
        print(f"{'Tempo de viagem (anos)':<25}: {planet.travel_time_years:.1f}")
        print(f"{'Distância da estrela (UA)':<25}: {planet.star_distance:.3f}")
        print(f"{'Zona habitável':<25}: {'Sim' if planet.habitable_zone else 'Não'}")
        
        print("\n=== TAXAS DE SOBREVIVÊNCIA ===")
        print(f"{'Terra':<25}: {earth_score:.1f}%")
        print(f"{planet.name:<25}: {planet_score:.1f}%")
        print(f"{'Diferença':<25}: {abs(earth_score - planet_score):.1f} pontos")
        
        if planet_score >= 60:
            veredict = "HABITÁVEL (Satisfaz requisitos mínimos)"
        elif planet_score >= 30:
            veredict = "MARGINALMENTE HABITÁVEL (Requer tecnologia adicional)"
        else:
            veredict = "INABITÁVEL (Condições extremamente hostis)"
        
        print(f"\nVEREDITO PARA {planet.name.upper()}: {veredict}")
        
        if self.current_mission:
            print("\n=== PROJEÇÃO DE COLONIZAÇÃO ===")
            print(f"Colonos iniciais: {self.current_mission.male_count} homens + {self.current_mission.female_count} mulheres")
            print(f"Óvulos fecundados: {self.current_mission.fertilized_eggs}")
            print(f"Duração da missão: {self.current_mission.mission_duration} anos")
            print(f"\nProjeção de crescimento populacional:")
            print(f"- Nascimentos potenciais: {potential}")
            print(f"- Crianças sobreviventes: {surviving} (taxa de {surviving/potential*100:.1f}%)")
            print(f"- População final estimada: {self.current_mission.male_count + self.current_mission.female_count + surviving}")
        
        # Gráficos
        self.plot_comparison(earth_score, planet_score, earth, planet)

    def plot_comparison(self, earth_score, planet_score, earth, planet):
        """Cria gráficos comparativos"""
        # Gráfico de barras comparativo
        plt.figure(figsize=(12, 6))
        bars = plt.bar(['Terra', planet.name], [earth_score, planet_score], 
                      color=['blue', 'orange'])
        plt.title('Comparação de Habitabilidade')
        plt.ylabel('Índice de Sobrevivência (%)')
        plt.ylim(0, 100)
        
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}%', ha='center', va='bottom')
        
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
        
        # Gráfico de radar
        labels = [f.replace('_', ' ').title() for f in self.factors]
        earth_values = [getattr(earth, f) for f in self.factors]
        planet_values = [getattr(planet, f) for f in self.factors]
        
        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
        angles += angles[:1]
        earth_values += earth_values[:1]
        planet_values += planet_values[:1]
        
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
        ax.plot(angles, earth_values, 'b', label='Terra')
        ax.fill(angles, earth_values, 'b', alpha=0.1)
        ax.plot(angles, planet_values, 'r', label=planet.name)
        ax.fill(angles, planet_values, 'r', alpha=0.1)
        
        ax.set_thetagrids(np.degrees(angles[:-1]), labels)
        ax.set_ylim(0, 100)
        ax.set_title('Comparação por Fator', y=1.1)
        ax.legend(loc='upper right')
        plt.tight_layout()
        plt.show()

    def run(self):
        """Loop principal do programa"""
        while True:
            print("\n" + "="*50)
            print("ANÁLISE DE HABITABILIDADE PLANETÁRIA")
            print("="*50 + "\n")
            print("1. Selecionar planeta conhecido")
            print("2. Criar planeta personalizado")
            print("3. Definir parâmetros de colonização")
            print("4. Mostrar análise comparativa")
            print("5. Sair")
            
            choice = input("\nEscolha uma opção (1-5): ")
            
            if choice == '1':
                print("\nPlanetas disponíveis:")
                for pt in PlanetType:
                    if pt != PlanetType.PERSONALIZADO:
                        print(f"{pt.value}. {pt.name.replace('_', ' ').title()}")
                
                try:
                    selection = int(input("\nSelecione um planeta: "))
                    if PlanetType(selection):
                        self.selected_planet = self.real_planets[PlanetType(selection)]
                        self.custom_planet = None
                        print(f"\nPlaneta {self.selected_planet.name} selecionado!")
                except:
                    print("Seleção inválida!")
            
            elif choice == '2':
                self.input_custom_planet()
                self.selected_planet = None
            
            elif choice == '3':
                self.input_mission_parameters()
            
            elif choice == '4':
                self.show_comparison()
            
            elif choice == '5':
                print("Encerrando o programa...")
                break
            
            else:
                print("Opção inválida. Por favor, tente novamente.")

# Executar o programa
if __name__ == "__main__":
    tool = PlanetComparisonTool()
    tool.run()