import os
import shutil
from textnode import TextNode
from md_to_textnode import *

def main():
   create_public()
   move_directories(path= "static", path2= "public")
   generate_page_recursively("content","template.html","public")

def create_public():
   if os.path.exists("public"):
      shutil.rmtree("public",ignore_errors=True)
   os.mkdir("public")

def move_directories(path = "",path2 = ""):
   dir = os.listdir(path)
   if len(dir) == 0:
      return
   for i in range(0,len(dir)):
      newpath = os.path.join(path,dir[i])
      newpath2 = os.path.join(path2,dir[i])
      if os.path.isfile(newpath):
         shutil.copy(newpath,f"{path2}")
      else:
         os.mkdir(f"{path2}/{dir[i]}")
         move_directories(path=newpath,path2=newpath2)
   return

def extract_title(markdown):
   lines = open(markdown,"r")
   for line in lines:
      line = line.strip()
      cut = line.split("# ")
      if len(cut) == 2 and len(cut[0]) == 0:
         return cut[1]
   raise Exception("No title available")

def replace_template(template,title,content):
   read = open(template,"r")
   html = read.read()
   titled = html.replace("{{ Title }}", title)
   return titled.replace("{{ Content }}",content)
   

def generate_page(from_path, template_path, dest_path):
   print(f"Generating page from {from_path} to {dest_path} using {template_path}")
   html_node = markdown_to_html_node(from_path)
   html = html_node.to_html()
   title = extract_title(from_path)
   page = replace_template(template_path,title,html)
   with open(dest_path,"w") as end:
      print(page,file=end)
   return

def generate_page_recursively(dir_path_content, template_path, dir_dest_path):
   print(f"Generating page recursively from {dir_path_content} to {dir_dest_path} using {template_path}")
   dirs = os.listdir(dir_path_content)
   if len(dirs) == 0:
      return
   for i in range(0,len(dirs)):
      if dirs[i][-2:] == "md":
         generate_page(os.path.join(dir_path_content,dirs[i]),template_path,os.path.join(dir_dest_path,dirs[i].replace("md","html")))
      elif not os.path.isfile(os.path.join(dir_dest_path,dirs[i])):
         os.mkdir(os.path.join(dir_dest_path,dirs[i]))
         generate_page_recursively(dir_path_content= os.path.join(dir_path_content,dirs[i]),template_path = template_path,dir_dest_path= os.path.join(dir_dest_path,dirs[i]))
   return



if __name__ == "__main__":
   main()
   