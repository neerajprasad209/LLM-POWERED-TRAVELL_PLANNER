from utils.custom_exception import CustomException
from utils.logger import get_logger
from utils.common_function import read_yalm_file
from config.path_config import CONFIG_YAML
from langchain_core.messages import HumanMessage, AIMessage
from chains.itinerary_chain import LLMModel

logger = get_logger(__name__)


class TravelPlanner:
    def __init__(self):
        self.messages = []
        self.city = ""
        self.interests = []
        self.days = ""
        self.model_config = read_yalm_file(CONFIG_YAML)
        self.llm_model = LLMModel(self.model_config)
        self.itenary = ""
        
        logger.info("Travel planner initialized.")
        
    def set_city(self, city:str):
        """Setting the city

        Args:
            city (str): User Interested city
        """
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city))
            logger.info("City set successfully.")
        except Exception as e:
            logger.error(f"Error occurred while setting the city: {e}")
            raise CustomException("Custom exception in set_city", e)
        
    def set_days(self, days:str):
        """Setting the number of days

        Args:
            days (int): Number of days
        """
        try:
            self.days = days
            self.messages.append(HumanMessage(content=days))
            logger.info("Days set successfully.")
        except Exception as e:
            logger.error(f"Error occurred while setting the days: {e}")
            raise CustomException("Custom exception in set_days", e)
    
    def set_interests(self, interests_str:str):
        """Setting the interests

        Args:
            interests_str (str):Places of interest in the city
        """
        try:
            self.interests = [i.strip() for i in interests_str.split(",")]
            self.messages.append(HumanMessage(content=interests_str))
            logger.info("Interests set successfully.")
        except Exception as e:
            logger.error(f"Error occurred while setting the interests: {e}")
            raise CustomException("Custom exception in set_interests", e)
        
    def create_itinary(self):
        """Creating the itinary for the given city and 
        """
        try:
            logger.info(f"Creating itinary for {self.city} with interests {self.interests}")
            response = self.llm_model.get_itinary(self.city, self.interests, self.days)
            
            self.messages.append(AIMessage(content=response))
            self.itenary = response
            logger.info(f"LLM response: {response}")
            logger.info("Itinary created successfully.")

            return self.itenary
        except Exception as e:
            logger.error(f"Error occurred while creating the itinary: {e}")
            raise CustomException("Custom exception in create_itinary", e)
