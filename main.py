import kivy
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

from plyer import notification


event = None
threshold = 57
time_interval = 5


def got_json(req, result):
	pass


def get_current_inr_value():
    rates_url = f'https://api.currencyapi.com/v3/latest?apikey=nHZBwPeOVvhvVhP2nuF7byWNGiqUHtJA9Inku0F4&currencies=AUD,INR&base_currency=AUD'
    req = UrlRequest(rates_url)
    req.wait()
    response = req.result
    current_value = response['data']['INR']['value']
    return current_value


def get_messages(current_value):
    title = "Currency Convertion Alert!"
    message = f"Current Rate: {current_value}"
    return title, message


class MyGrid(GridLayout):
    notification_flag = False

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Currency Threshold: "))
        self.threshold = TextInput(multiline=False)
        self.inside.add_widget(self.threshold)

        self.inside.add_widget(Label(text="Time Interval in minutes: "))
        self.time_interval = TextInput(multiline=False)
        self.inside.add_widget(self.time_interval)

        self.start = Button(text="Start", font_size=40)
        self.start.bind(on_press=self.start_notifications)
        self.inside.add_widget(self.start)

        self.stop = Button(text="Stop", font_size=40)
        self.stop.bind(on_press=self.stop_notifications)
        self.inside.add_widget(self.stop)

        self.add_widget(self.inside)

        self.label_info = Label(
            text="Minimum time interval is 5 min!", font_size=50)
        self.add_widget(self.label_info)

    def start_notifications(self, obj):
        global event
        global threshold
        global time_interval

        if self.threshold.text:
            threshold = float(self.threshold.text)
        else:
            threshold = 57
        if self.time_interval.text:
            time_interval = float(self.time_interval.text)
        else:
            time_interval = 5

        if time_interval < 5:
            self.label_info.text = "Incorrect time interval Minimum is 5 min!"
            self.label_info.font_size = 30
            self.threshold.text = ""
            self.time_interval.text = ""
            return

        notify_secs = time_interval * 60

        event = Clock.schedule_interval(
            self.send_notificatons, notify_secs / 1.)

        self.label_info.text = f"Success! Alert for every {time_interval} min with threshold {threshold}"
        self.label_info.font_size = 30

    def send_notificatons(self, obj):
        current_value = get_current_inr_value()
        if current_value > threshold:
            title, message = get_messages(current_value)
            notification.notify(title=title, message=message,
                                app_icon=None, timeout=10, toast=False)

    def stop_notifications(self, obj):
        global event
        event.cancel()
        self.label_info.text = f"Stopped! No more Alerts"
        self.label_info.font_size = 40


class MyApp(App):

    def build(self):
        return MyGrid()


MyApp().run()
