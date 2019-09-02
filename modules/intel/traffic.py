"""
Traffic

This module will list known country and state traffic camera resources
"""

cams = {
    "Alabama": 	"http://alitsweb2.dot.state.al.us/its/",
    "Alaska": 	"http://www.dot.state.ak.us/iways/roadweather/forms/AreaSelectForm.html",
    "Arizona": 	"http://www.az511.gov/adot/files/cameras/",
    "Arkansas": 	"http://www.fhwa.dot.gov/Trafficinfo/ar.htm",
    "California": 	"http://www.dot.ca.gov/dist6/cctv/",
    "Colorado": 	"http://www.cotrip.org/home.htm",
    "Connecticut": 	"http://www.ct.gov/dot/cwp/view.asp?a=1993&Q=290242&dotNav=|",
    "Delaware": 	"http://www.deldot.gov/information/travel_advisory/",
    "Florida": 	"http://www.fl511.com/Cameras.aspx",
    "Georgia": 	"http://www.georgia-navigator.com/cameras",
    "Hawaii": 	"http://www.fhwa.dot.gov/Trafficinfo/hi.htm",
    "Idaho": 	"http://511.idaho.gov/staticMap.asp?display=cams",
    "Illinois": 	"http://www.webcamlocator.com/traffic/illinois_traffic_webcam_locator.htm",
    "Indiana": 	"http://www.fhwa.dot.gov/Trafficinfo/in.htm",
    "Iowa": 	"http://www.webcamlocator.com/traffic/iowa_traffic_webcam_locator.htm",
    "Kansas": 	"http://511.ksdot.org/KanRoadPublic_VE/Default.aspx",
    "Kentucky": 	"http://www.webcamlocator.com/traffic/kentucky_traffic_webcam_locator.htm",
    "Louisiana": 	"http://hb.511la.org/",
    "Maine": 	"http://www.webcamlocator.com/traffic/maine_traffic_webcam_locator.htm",
    "Maryland": 	"http://www.chart.state.md.us/TravInfo/trafficcams.php",
    "Massachusetts": "http://www1.eot.state.ma.us/",
    "Michigan": 	"http://www.webcamlocator.com/traffic/michigan_traffic_webcam_locator.htm",
    "Minnesota": 	"http://www.dot.state.mn.us/tmc/trafficinfo/metrocams/mapindex.html",
    "Mississippi": 	"http://www.mdottraffic.com/default.aspx?showMain=true",
    "Missouri": 	"http://www.webcamlocator.com/traffic/missouri_traffic_webcam_locator.htm",
    "Montana": 	"http://www.mdt.mt.gov/travinfo/weather/rwis.shtml",
    "Nebraska": 	"http://www.webcamlocator.com/traffic/nebraska_traffic_webcam_locator.htm",
    "Nevada": 	"http://www.nvfast.org/trafficcameras.html",
    "New Hampshire": "http://67.62.24.187/reportservice/(S(p4omokq3rplgpufohciafkv3))/public.aspx",
    "New Jersey": 	"http://www.webcamlocator.com/traffic/newjersey_traffic_webcam_locator.htm",
    "New Mexico": 	"http://nmroads.com/",
    "New York": 	"http://www.webcamlocator.com/traffic/newyork_traffic_webcam_locator.htm",
    "North Carolina": "https://apps.dot.state.nc.us/TIMS/RegionSummary.aspx?re=",
    "North Dakota": "http://www.dot.nd.gov/travel-info/",
    "Ohio": 	"http://www.webcamlocator.com/traffic/ohio_traffic_webcam_locator.htm",
    "Oklahoma": 	"http://www.oktraffic.org/index.php",
    "Oregon": 	"http://www.webcamlocator.com/traffic/oregon_traffic_webcam_locator.htm",
    "Pennsylvania": "http://www.webcamlocator.com/traffic/pennsylvania_traffic_webcam_locator.htm",
    "Rhode Island": "http://www.tmc.state.ri.us/",
    "South Carolina": "http://www.511sc.org",
    "South Dakota": "http://www.safetravelusa.com/sd/cameras/",
    "Tennessee": 	"http://www.webcamlocator.com/traffic/tennessee_traffic_webcam_locator.htm",
    "Texas": 	"http://www.webcamlocator.com/traffic/texas_traffic_webcam_locator.htm",
    "Utah": 	"http://commuterlink.utah.gov/",
    "Vermont": 	"http://www.511vt.com/",
    "Virginia": 	"http://511virginia.org/Cameras.aspx?r=1",
    "Washington": 	"http://www.webcamlocator.com/traffic/washington_traffic_webcam_locator.htm",
    "Washington DC":"http://www.webcamlocator.com/traffic/district_traffic_webcam_locator.htm",
    "West Virginia":"http://www.webcamlocator.com/traffic/westvirginia_traffic_webcam_locator.htm",
    "Wisconsin": 	"http://www.webcamlocator.com/traffic/wisconsin_traffic_webcam_locator.htm",
    "Wyoming": 	"http://www.webcamlocator.com/traffic/wyoming_traffic_webcam_locator.htm"
}

class Module:
    """
    Module Class
    """
    __title__ = 'intel/traffic'
    __date__ = '2017-11-12'
    __rank__ = 'normal'
    __description__ = 'List known traffic camera resources'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def run(self):
        """
        run(self)
        
        :return: 
        """
        col_width = max(len(c) for c in cams) + 2  # padding
        print("\n")
        for c in cams:
            print ("{} : {}".format(c.ljust(col_width), cams[c].ljust(col_width)))
        print("\n")
