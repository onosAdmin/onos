#!/usr/bin/env python

import codecs
#from get_top_menu import *   #works because there is sys.path.append(lib_dir2)  in globalVar.py
try:
  obj_name_list=zoneDict[zone]["objects"]   
except:
  print "Content-type: text/html\n"
  obj_name_list=["a","b"]
  print(str(list(obj_name_list)))

#with codecs.open("css/play-zone.css",'r',encoding='utf8') as g:
#    css_file = g.read()
#    css_play_zone=css_file
#g.close()  

print("ssfref")
part_to_insert_in_head='''<!--onos_automatic_page--><!--onos_automatic_javascript--><link rel="stylesheet" href="/css/display_zone_objects.css"><style type="text/css"><!--onos_automatic_body_style--></style>
   	<title>Object list</title>

'''
#html=getTopMenu(part_to_insert_in_head)

play_zone_html=html+'''
<body>

<div id="ReloadThis" >


 '''


web_page=play_zone_html+ '''<title>'''+zone.upper()+'''</title>'''



web_page_old=web_page




for a in obj_name_list :      # for every web_obj in the zone make a row...


  web_page=web_page+'''




		<div class="riga" <!--onos_automatic_local_style--> >
            <!--onos_automatic_object_a-->  
			  <div id="<!--onos_automatic_object_id-->"   class="imagebutton col1" onclick="buttonfunction(this.id,'click1');"></div>
			  <div class="specs col2"><!--onos_automatic_object_html--></div>
			  <div class="impostazioni-link col3"><i class="icon-wrench"></i>
            </div>



		</div>






'''

if len(obj_name_list)<1:
  web_page=web_page_old+"No objects present in this zone" 
        


web_page=web_page+'''<div id="footer"></div></div><!--end reload--></body></html>''' #the closing div is for the reload_page_indicator div


print(web_page)
print("ddd")

