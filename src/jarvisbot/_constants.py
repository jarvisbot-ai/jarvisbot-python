import httpx

RAW_RESPONSE_HEADER = "X-Raw-Response"
OVERRIDE_CAST_TO_HEADER = "___override_cast_to"

# default timeout is 10 minutes
DEFAULT_TIMEOUT = httpx.Timeout(timeout=600.0, connect=5.0)
DEFAULT_MAX_RETRIES = 2
DEFAULT_LIMITS = httpx.Limits(max_connections=100, max_keepalive_connections=20)

INITIAL_RETRY_DELAY = 0.5
MAX_RETRY_DELAY = 8.0

DEFAULT_BASE_URL = "http://jarvisbot.emchub.ai:10013"
TOKEN_CHECK_PATH = "/jarvis/v1/token/api/check/"
