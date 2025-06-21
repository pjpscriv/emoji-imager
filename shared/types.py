import io
import base64
from PIL import Image
from shared.helpers import get_row_filename


class Emoji2:
    emoji: str = ''
    name: str = ''
    codepoints: str = ''
    filename: str = ''
    ignore: bool = False

    def __init__(self, row: dict) -> None:
        self.emoji = row['emoji']
        self.name = row['name']
        self.codepoints = row['codepoints']
        self.ignore = row.get('ignore', '0') == '1'
        self.filename = get_row_filename(row)
    
    def get_image(self, vendor: str, size: int) -> Image:
        image = self.get_company_image(vendor)
        # Resize image to 160 x 160 pixels
        image = image.resize((size, size))
        return image

    def get_company_image(self, company: str) -> Image:
        try:
            return Image.open(f'./backend/imgs/{company}/{self.filename}')
        except FileNotFoundError:
            raise Exception(f'ERROR: Could not load image for this emoji: "{self.name}" (Emoji: {self.emoji}, Company: {company})')


class Emoji:
    id = 0
    emoji = ''
    unicode = ''
    name = ''
    apple = ''
    google = ''
    facebook = ''
    windows = ''
    twitter = ''
    joypixels = ''
    samsung = ''
    gmail = ''
    softbank = ''
    docomo = ''
    kddi = ''
    _print_limit = 35


    def __init__(self, line) -> None:
        self.id = line[0]
        self.emoji = line[1]
        self.unicode = line[2]
        self.name = line[3].replace(':', ',').replace('*', 'star')
        self.apple = line[4]
        self.google = line[5]
        self.facebook = line[6]
        self.windows = line[7]
        self.twitter = line[8]
        self.joypixels = line[9]
        self.samsung = line[10]
        self.gmail = line[11]
        self.softbank = line[12]
        self.docomo = line[13]
        self.kddi = line[14]

    def get_image(self) -> Image:
        try:
            return self.get_company_image(self.apple)
        except:
            pass
        try:
            return self.get_company_image(self.facebook)
        except:
            pass
        try:
            return self.get_company_image(self.google)
        except:
            pass
        try:
            return self.get_company_image(self.twitter)
        except:
            pass
        try:
            return self.get_company_image(self.windows)
        except:
            pass
        try:
            return self.get_company_image(self.joypixels)
        except:
            pass
        try:
            return self.get_company_image(self.samsung)
        except:
            pass
        try:
            return self.get_company_image(self.gmail)
        except:
            pass
        try:
            return self.get_company_image(self.softbank)
        except:
            pass
        try:
            return self.get_company_image(self.docomo)
        except:
            pass
        try:
            return self.get_company_image(self.kddi)
        except:
            raise Exception(f'ERROR: Could not load image for this emoji: "{self.name}" (ID: {self.id})')

    def get_company_image(self, company_string) -> Image:
        bytes_string = company_string.split(',')[1]
        actual_bytes = base64.b64decode(bytes_string)
        image = Image.open(io.BytesIO(actual_bytes))
        return image

    def __repr__(self) -> str:
        return self.print_partial()

    def print_partial(self) -> str:
        res = f'''Emoji: {self.emoji} (ID: {self.id}, {self.unicode}, "{self.name}") Apple: "{self.apple[:self._print_limit]}..."'''
        return res

    def print_full(self) -> str:
        res = f'''Emoji: {{
    ID: {self.id},
    emoji: {self.emoji},
    unicode: {self.unicode},
    name: {self.name},
    Apple: {self.apple[:self._print_limit]}...,
    Google: {self.google[:self._print_limit]}...,
    Facebook: {self.facebook[:self._print_limit]}...,
    Windows: {self.windows[:self._print_limit]}...,
    Twitter: {self.twitter[:self._print_limit]}...,
    JoyPixels: {self.joypixels[:self._print_limit]}...,
    Samsung: {self.samsung[:self._print_limit]}...,
    Gmail: {self.gmail[:self._print_limit]}...,
    SoftBank: {self.softbank[:self._print_limit]}...,
    DoCoMo: {self.docomo[:self._print_limit]}...,
    KDDI: {self.kddi[:self._print_limit]}...\n
}}'''
        return res
