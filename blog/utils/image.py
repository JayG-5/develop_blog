import hashlib,re,base64,random,string

from django.core.files.base import ContentFile
from ..models import Image

def upload_image(image):
    hash_value = hashlib.sha1(image.read()).hexdigest()
    image_extension = image.name.split('.')[-1].lower()
    file_id = f"{hash_value}.{image_extension}"
    
    try:
        image_model = Image.objects.get(file_id=file_id)
        return image_model
    except Image.DoesNotExist:
        image.name = file_id
        image_model = Image.objects.create(file_id=file_id, image=image)
        return image_model

def random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def handle_markdown_images(markdown_string):
    uploaded_images = []    
    def base64_to_imgurl(match):
        base64_img = match.group(2)
        image_data = base64_img.encode()
        image = ContentFile(base64.b64decode(image_data), name=f"{random_string(10)}.png")
        uploaded_image = upload_image(image)
        uploaded_images.append(uploaded_image)
        return f"![]({uploaded_image.image.url})"

    regex = r'!\[.*?\]\((data:image\/.*?;base64,([a-zA-Z0-9+/=]+))\)'
    result_string = re.sub(regex, base64_to_imgurl, markdown_string)

    return result_string,uploaded_images