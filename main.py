from authentication import get_authenticated_service
from urls_handlers import ChannelUrlHandler, UserUrlHandler, PlaylistUrlHandler
from api_requests import ApiV3RequestsHandler
from database_handler import close_connection

try:
    service_client = get_authenticated_service()

except Exception as e:
    print('\nThe following error occurred while tring to initialize the google client:')
    print(e)
    close_connection()
    exit()

api_requests_handler = ApiV3RequestsHandler(service_client=service_client)

channel_url_handler = ChannelUrlHandler(
    api_requests_handler=api_requests_handler)

user_url_handler = UserUrlHandler(api_requests_handler=api_requests_handler)

playlist_url_handler = PlaylistUrlHandler(
    api_requests_handler=api_requests_handler)

url_handlers = [channel_url_handler, user_url_handler, playlist_url_handler]

url = raw_input('\nPlease enter a valid youtube channel/account/playlist url:\n')

playlist_id, error = None, False

for i in url_handlers:
    
    try:
        
        playlist_id = i.get_playlist_id(url)

        if playlist_id is not None:

            print('\nValid url detected\nStart downloading videos info\nPlease wait...')

            try:
                i.save_videos_info(playlist_id=playlist_id)
            except Exception as e:
                error = True
                print('Error: ', e)
                break
    
    except:
        continue

if playlist_id is None:
    print('Url not valid')
elif not error:
    print('The download completed successfully')

close_connection()
