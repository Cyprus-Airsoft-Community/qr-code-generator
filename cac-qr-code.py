import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

data = "https://discord.io/CyprusAirsoftCommunity"
border_color = "#4e5b31"  # Set your border color here
text_color = "#4e5b31"  # Set your text color here

# Generate a high resolution QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=60,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Create the QR code with the specified fill color
img = qr.make_image(fill_color="#d57800", back_color="white").convert("RGBA")

# Load the logo
logo = Image.open("server_avatar.png")

# Calculate dimensions to position the logo at the center
logo_width, logo_height = logo.size
qr_width, qr_height = img.size
logo_size = (
    min(qr_width, qr_height) // 3
)  # Size of the logo - you can adjust this value
logo_x = (qr_width - logo_size) // 2  # x position of the logo
logo_y = (qr_height - logo_size) // 2  # y position of the logo

# Resize the logo as per the calculated dimensions
logo = logo.resize((logo_size, logo_size))

# Paste the logo at the center
img.paste(logo, (logo_x, logo_y), logo)

# Add a border around the QR code
border_width = 60  # Adjust as needed
border_img = Image.new(
    "RGBA", (qr_width + border_width, qr_height + border_width), "white"
)  # Add extra height for the text
border_img.paste(img, (border_width // 2, border_width // 2))

# Create an ImageDraw object
draw = ImageDraw.Draw(border_img)

# Draw a border around the QR code
draw.rectangle(
    [
        (border_width // 2, border_width // 2),
        (qr_width + border_width // 2, qr_height + border_width // 2),
    ],
    outline=border_color,
    width=border_width,
)

# Load the font (ensure the .ttf file is in the correct path location)
font = ImageFont.truetype("azonix.ttf", 100)  # Adjust size as needed

# Add the text under the QR code
text = "discord.io/CyprusAirsoftCommunity"
text_width, text_height = draw.textsize(text, font=font)
text_x = (border_img.width - text_width) // 2
text_y = border_img.height - text_height - 120  # Adjust as needed
draw.text((text_x, text_y), text, fill=text_color, font=font)

# check if file "discord_link_qr_code.png" exists, if it does, delete it and save it again
if os.path.exists("discord_link_qr_code.png"):
    os.remove("discord_link_qr_code.png")

border_img.save("discord_invite_qr_code.png")
