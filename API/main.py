import sys
import requests 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox
from PyQt5.QtCore import Qt, QDateTime

class WeatherApp(QWidget): 
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.updated_label = QLabel("", self)
        self.unit_combo = QComboBox(self)
        self.unit_combo.addItems(["°C", "°F"])
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Weather App')
        self.setFixedSize(500, 600)  # velg størrelse du vil ha
        self.temperature_label.setWordWrap(True)

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.unit_combo)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        vbox.addWidget(self.updated_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.updated_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("cityLabel")
        self.city_input.setObjectName("cityInput")
        self.unit_combo.setObjectName("unitCombo")
        self.get_weather_button.setObjectName("getWeatherButton")
        self.temperature_label.setObjectName("temperatureLabel")
        self.emoji_label.setObjectName("emojiLabel")
        self.description_label.setObjectName("descriptionLabel")
        self.updated_label.setObjectName("updatedLabel")

        self.setStyleSheet("""
            QWidget{
                background-color: #CCF6FF;
                color: black; /* Setter all tekst til svart  TEST*/
            }
            QLabel{
                font-family: Calibri;
                font-weight: bold;
            }
            QLabel#cityLabel{
                font-size: 40px;
                font-style: italic;
            }
                           
            QLineEdit#cityInput{
                font-size: 40px;
                min-height: 60px;
                border: 2px solid black;
                border-radius: 10px;
                padding: 10px;
                background-color: #EBFCFF;
            }
                           
            QComboBox#unitCombo{
                font-size: 18px;
                height: 30px;
                border: 2px solid black;
                padding: 5px;
                background-color: #EBFCFF;
                color: black;
            }
            
            QComboBox#unitCombo QAbstractItemView {
                color: black; /* Sørger for at ALL tekst i nedtrekkslisten er svart */
                background-color: #CCF6FF;
            }
            
            QComboBox#unitCombo QAbstractItemView::item:hover {
                background-color: #EBFCFF; /* Hover-farge */
            }
                           
            QPushButton#getWeatherButton{
                background-color: #EBFCFF;
                font-size: 30px;
                font-weight: bold;
                padding: 10px;
                border: 2px solid black;
            }
            QLabel#temperatureLabel{
                font-size: 75px;
                font-weight: bold;
            }
            QLabel#emojiLabel{
                font-size: 100px;
                font-family: "Apple Color Emoji";
            }
            QLabel#descriptionLabel{
                font-size: 30px;
            }
            QLabel#updatedLabel{
                font-size: 12px;
                font-style: italic;
                color: #555555;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)
        self.city_input.returnPressed.connect(self.get_weather)
        self.get_weather_button.setDefault(True)  # Enter aktiverer knappen

    def get_weather(self):
        api_key = "5154da1038d8933d48a3f337bacce707"
        city = self.city_input.text()
        unit = "metric" if self.unit_combo.currentText() == "°C" else "imperial"

        url = (f"https://api.openweathermap.org/data/2.5/weather"f"?q={city}&appid={api_key}&units={unit}")

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data, unit)

        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error("Bad request.\nPlease check your input.")
                case 401:
                    self.display_error("Invalid API key.\nPlease check your API key.")
                case 403:
                    self.display_error("Access forbidden.\nYou might have exceeded your API request limit.")
                case 404:
                    self.display_error("City not found.\nPlease check the city name.")
                case 500:
                    self.display_error("Server error.\nPlease try again later.")
                case 502:
                    self.display_error("Bad gateway.\nPlease try again later.")
                case 503:
                    self.display_error("Service unavailable.\nPlease try again later.")
                case 504:
                    self.display_error("Gateway timeout.\nPlease try again later.")
                case _:
                    self.display_error(f"HTTP error occurred: {response.status_code}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection error:\nPlease check your internet connection.")
        except requests.exceptions.Timeout: 
            self.display_error("Timeout error:\nThe request timed out.")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL.")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error:\n{req_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("color: red; font-size: 18px;")
        self.temperature_label.setWordWrap(True)
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()
        self.updated_label.clear()
 
    def display_weather(self, data, unit):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temp = data["main"]["temp"]
        symbol = "°C" if unit == "metric" else "°F"
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        self.temperature_label.setText(f"{temp:.1f}{symbol}")
        self.description_label.setText(data["weather"][0]["description"].capitalize())
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description.capitalize())
        self.updated_label.setText("Last updated: " + QDateTime.currentDateTime().toString("dd.MM.yyyy HH:mm"))

    @staticmethod
    def get_weather_emoji(weather_id):
         match weather_id:
            case _ if 200 <= weather_id <= 232:
                return "⛈️"   
            case _ if 300 <= weather_id <= 321:
                return "🌦️"   
            case _ if 500 <= weather_id <= 531:
                return "🌧️"  
            case _ if 600 <= weather_id <= 622:
                return "❄️"   
            case _ if 701 <= weather_id <= 741:
                return "🌫️"   
            case 762:
                return "🌋"   
            case 771:
                return "💨"   
            case 781:
                return "🌪️"   
            case 800:
                return "☀️"   
            case _ if 801 <= weather_id <= 804:
                return "☁️"   
            case _:
                return ""   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
