from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from config.path_config import CONFIG_YAML
from config.api_config import GROQ_API_KEY
from utils.common_function import read_yalm_file
from utils.custom_exception import CustomException
from utils.logger import get_logger

logger = get_logger(__name__)

class LLMModel:
    def __init__(self, model_param):
        self.model_param = model_param['Model_Params']
        self.model_name = self.model_param['model_name']
        self.temperature = self.model_param['temperature']
        self.max_tokens = self.model_param['max_tokens']
        self.groq_api_key = GROQ_API_KEY
        self.prompt = read_yalm_file(CONFIG_YAML)
    
    def initialization_of_model_and_prompt(self):
        try:
            logger.info("Initializing the model...")
            
            model = ChatGroq(api_key=self.groq_api_key, model=self.model_name, temperature=self.temperature, max_tokens=self.max_tokens)
            
            prompt = ChatPromptTemplate.from_messages([
                ("system", self.prompt['Itenery_prompts']['system']),
                ("human", self.prompt['Itenery_prompts']['human'])
            ])
            
            
            logger.info(f"Model initialized with prompt: {self.prompt['Itenery_prompts']}")
            
            return model, prompt
        
        except Exception as e:
            logger.error("Error occurred while getting the model.")
            raise CustomException("Custom exception in get_model", e)
    
    def get_itinary(self, city: str, interests: list[str], days: str)-> str:
        """Creating the iteneary for the given city and interests. 

        Args:
            city (str): User Given city
            interests (list[str]): User Given Interests

        Returns:
            str: Model Response
        """
        try:
            logger.info("Getting itinary...")
            
            model, prompt = self.initialization_of_model_and_prompt()
            
            itinary = model(
                    prompt.format_messages(
                            city=city, 
                            interests=interests,
                            days=days
                        )
                )
            
            logger.info(f"Itinary: {itinary}")
            
            return itinary.content
        
        except Exception as e:
            logger.error("Error occurred while getting the itinary.")
            raise CustomException("Custom exception in get_itinary", e)