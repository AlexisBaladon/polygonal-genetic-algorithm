from Statistics import Statistics
from DeapConfig import DeapConfig
from AltSolver import AltSolver
from EAController import EAController
from ImageProcessor import ImageProcessor
from EA import EA

"""
     dc = DeapConfig(NGEN=NGEN)
     ip = ImageProcessor(IMAGE_NAME, vertex_count=VERTEX_COUNT)
     ea = EA(ip)
     eac = EAController(ea, dc)
     eac.build_ea_module()
     eac.build_deap_module()
     alts = AltSolver(eac.evolutionary_algorithm)

     stats = Statistics(eac, alts)
     stats.parametric_evaluation()
     stats.parametric_evaluation()
     stats.greedy_evaluation()

     #una vez se tenga la configuracion optima
     stats.informal_evaluation()
     stats.efficiency_evaluation()   
"""

DeapConfig.register_fitness() # register fitness outside main

if __name__  == "__main__":        
    IMAGE_RESULT_PATH = "img/"
    stateless_stats = Statistics(None, None)

    #PARAMETRIC
    FORMAL_SEED_NUMBER = 30
    FORMAL_SEEDS = list(range(500, 500 + FORMAL_SEED_NUMBER))
    FORMAL_IMAGES = ["ultima_cena.jpg"]
    FORMAL_VERTEX_COUNT = 5000
    FORMAL_ATTRIBUTES = {"CXPB": [0.8, 0.9], "MUTPB": [0.01, 0.05, 0.1]}
    stateless_stats.parametric_evaluation2(FORMAL_VERTEX_COUNT, FORMAL_ATTRIBUTES, IMAGE_RESULT_PATH, FORMAL_IMAGES, seeds=FORMAL_SEEDS)

    #INFORMAL
    best_config = {"CXPB":0.8, "MUTPB":0.01} #TODO: obtenerla de la evaluación formal
    INFORMAL_ATTRIBUTES = {"MU": [50, 100], "selection": ["best", "tournament", "roulette"]}
    INFORMAL_VERTEX_COUNT = 100
    #stateless_stats.informal_evaluation_2(best_config, INFORMAL_VERTEX_COUNT, INFORMAL_ATTRIBUTES, IMAGE_RESULT_PATH, IMAGE_NAME, seeds=SEEDS)
    
    #GREEDY
    GREEDY_CONFIG = {
        "local_search": {"max_iter": 5, "threshold": 3},
        "gaussian": {"max_iter": 5, "threshold": 50}
    }
    stateless_stats.greedy_evaluation_2(best_config, GREEDY_CONFIG, FORMAL_VERTEX_COUNT, IMAGE_RESULT_PATH, seeds=SEEDS)
