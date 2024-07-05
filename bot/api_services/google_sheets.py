import gspread
from settings import GOOGLE_CREDS_FILENAME, GOOGLE_SCOPES


GS_CLIENT = gspread.service_account(GOOGLE_CREDS_FILENAME)
