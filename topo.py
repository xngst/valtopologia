from pathlib import Path
import json
import folium

in_dir = Path(r"C:\Downloads")

with open(in_dir/"topologia.json", "r") as f:
    d = json.load(f)
    
mmap = folium.Map(location=[47.497912,19.040235], zoom_start=12)

for row in range(0,len(d['Tables'][0]['Rows'])):
    
    shapes = d['Tables'][0]['Rows'][row][8]
    shape_list = []
    
    for i in shapes.split(","):
        shape_list.append([float(coord) for coord in i.split(" ")])
        
    folium.Polygon(
        locations=shape_list,
        color="blue",
        weight=1,
        fill_color="yellow",
        fill_opacity=0.5,
        fill=True,
        popup= "",
        tooltip= d['Tables'][0]['Rows'][row][1],
    ).add_to(mmap)
    
mmap.save(in_dir/"valasztasikorzetek.html")
