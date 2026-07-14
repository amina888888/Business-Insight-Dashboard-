import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='business_analysis.log',
    filemode='a'
)
logger = logging.getLogger("BusinessAnalytics")
