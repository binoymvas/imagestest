# @author: Binoy
# @create_date: 23-Jan-2015
# @modified by: Binoy M V    
# @modified_date: 23-Jan-2015
# @linking to other page: /__init__.py
# @description: Methods for the context processor

#Importing the configurations
from django.conf import settings 
print "in the base url v v v v "
def baseUrl(request):
 
    print "[[[[[[[[[[[[[["
    """To clean the site url
    Args:
        {
            self - request from the page          
        }
            
    Returns:
        Returns response to the html page
            
    Raises:
        Exceptions                
    """
    return {'base_url': settings.BASE_URL}

def mediaRoot(request):
    """To find the media root
    Args:
        {
            self - request from the page          
        }
            
    Returns:
        Returns response to the html page
            
    Raises:
        Exceptions                
    """
    return {'media_root': settings.MEDIA_ROOT}
