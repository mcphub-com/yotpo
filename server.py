import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/omrico1/api/yotpo'

mcp = FastMCP('yotpo')

@mcp.tool()
def get_product_reviews(count: Annotated[str, Field(description='specify how many reviews you want to pull')],
                        page: Annotated[str, Field(description='specify the page number you want to pull')]) -> dict: 
    '''get all reviews for a specific product that belongs to a specific app_key'''
    url = 'https://yotpo.p.rapidapi.com/products/B02uug6tF2uEA0Denhj0c9PV73y5PEOuKFmTCGb1/92431514/reviews'
    headers = {'x-rapidapi-host': 'yotpo.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'count': count,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_product_bottom_line_score(app_key: Annotated[str, Field(description='your application key that is assigned to you after signing up to Yotpo (www.yotpo.com)')],
                                  domain_key: Annotated[str, Field(description='unique identifier of the product as stored when creating the review')]) -> dict: 
    '''get bottom line score for a specific product that belongs to a specific app_key'''
    url = 'https://yotpo.p.rapidapi.com/products/B02uug6tF2uEA0Denhj0c9PV73y5PEOuKFmTCGb1/92431514/bottomline'
    headers = {'x-rapidapi-host': 'yotpo.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'app_key': app_key,
        'domain_key': domain_key,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_products(count: Annotated[Union[str, None], Field(description='specify how many products you want to pull')] = None,
                 page: Annotated[Union[str, None], Field(description='specify the page number you want to pull')] = None) -> dict: 
    '''getting all products stored for a specific app_key'''
    url = 'https://yotpo.p.rapidapi.com/apps/B02uug6tF2uEA0Denhj0c9PV73y5PEOuKFmTCGb1/products'
    headers = {'x-rapidapi-host': 'yotpo.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'count': count,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
