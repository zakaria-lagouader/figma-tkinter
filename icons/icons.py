import customtkinter
from PIL import Image
import os

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
search_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "search.png")), size=(24, 24))
plus_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "plus.png")), size=(24, 24))
chart_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "chart.png")), size=(24, 24))
drop_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "drop.png")), size=(24, 24))
home_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(24, 24))
edit_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "edit.png")), size=(24, 24))
delete_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "delete.png")), size=(24, 24))
cancel_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "cancel.png")), size=(24, 24))
play_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "play.png")), size=(24, 24))
ok_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "ok.png")), size=(24, 24))
close_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "close.png")), size=(24, 24))
bell_icon = customtkinter.CTkImage(Image.open(os.path.join(image_path, "bell.png")), size=(24, 24))
