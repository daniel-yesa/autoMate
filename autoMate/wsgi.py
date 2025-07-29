import logging
from main import create_app

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info("🔄 Starting via WSGI...")

app = create_app()  # ✅ Assign the result to `app`

logger.info("✅ WSGI app created")
