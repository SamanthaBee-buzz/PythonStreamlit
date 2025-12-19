import argparse
import json
import os
from datetime import datetime, timezone
from typing import Any, Dict, Iterable, List, Sequence

from dotenv import load_dotenv
from newsapi import NewsApiClient

from storage import insert_articles, log_ingestion
from tavily_ingest import normalize_articles

top 5/10 destinations for each country?