import os
import logging
from main import create_app

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info("🔄 Starting via WSGI...")

app = create_app()  # ✅ Assign the result to `app`

logger.info("✅ WSGI app created")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Railway will set this
    app.run(host="0.0.0.0", port=port)
