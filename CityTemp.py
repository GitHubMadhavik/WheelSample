import urlopen
import webbrowser

city = input("Enter City: ")
apikey = "5779e9b71429b01f7e37254bdba15a6a"
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + apikey + "&units=imperial&mode=html"

webbrowser.open(url)