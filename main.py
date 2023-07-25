import pywhatkit
import Ai_Functions as Func
import datetime

# main function to run AI
if __name__ == "__main__":
    while True:
        try:
            if 'jarvis' in Func.awake().lower():
                Func.wishme("Chirag")
                query = Func.take_command().lower()
                try:
                    if 'search' in query:
                        Func.speak("here what i found")
                        pywhatkit.search(query)
                    elif 'open' in query:
                        Func.open_browser(query)

                    elif 'play' in query:
                        Func.searchyt(query)

                    elif 'song' in query:
                        Func.searchyt(query)

                    elif 'on youtube' in query:
                        Func.searchyt(query)

                    elif 'the time' in query:
                        strTime = datetime.datetime.now().strftime("%H %M")
                        Func.speak(f"the time is {strTime}")
                    else:
                        Func.search_wikipedia(query)

                except Exception as e:
                    pass

            else:
                pass

        except Exception as e:
            pass