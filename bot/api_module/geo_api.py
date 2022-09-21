from ymaps import SearchAsync, GeocodeAsync, StaticAsync


async def get_api_search_org(key, query, **kwargs):
    response = await SearchAsync(key).search(query, **kwargs)
    return response['features']


async def get_api_image(query, **kwargs):
    return await StaticAsync().getimage(query, **kwargs)
