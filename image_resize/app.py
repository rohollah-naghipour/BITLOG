
from PIL import Image

def validate_cover_article(value):
   from django.core.exceptions import ValidationError
   from io import BytesIO
   img = Image.open(value)
   width, height = img.size
   if width != 768 or height != 512:
        new_width, new_height = 768, 512
        resized_image = img.resize((new_width, new_height))
        thumb_io = BytesIO()
        resized_image.save(thumb_io, format=['.jpg', '.png'])  
        thumb_io.seek(0)
        value.file = thumb_io
        value.name = value.name  
        
   return value     