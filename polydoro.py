import tkinter as tk

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 200

BUTTON_WIDTH = 10
BUTTON_HEIGHT = 5

currentType = "n"  # n = none, p = pomodoro, b = break

master = tk.Tk("Polydoro")
master.title("Polydoro")
master.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
master.configure(bg="red3")
master.resizable(False, False)

timeText = tk.StringVar()
timeText.set("00:00")
timeLabel = tk.Label(master, textvariable=timeText, font=("Arial", 32, "bold"))
timeLabel.pack(padx=20, pady=20, side=tk.TOP, fill=tk.BOTH)


def resetPomodoro():
    global currentType
    currentType = "n"
    timeText.set("00:00")


def startTimer(totalTime, type):
    global currentType

    if type != currentType:
        return

    if totalTime > 0:
        minutes, seconds = divmod(totalTime, 60)
        timeText.set(f"{minutes:02}" + ":" + f"{seconds:02}")
        totalTime -= 1
        master.after(1000, startTimer, totalTime, type)
    else:
        resetPomodoro()


def startSession():
    global currentType
    currentType = "p"
    startTimer(1500, "p")


def startBreak():
    global currentType
    currentType = "b"
    startTimer(300, "b")


buttonFrame = tk.Frame(master)
buttonFrame.pack(padx=20, pady=20, side=tk.BOTTOM)

startButton = tk.Button(
    buttonFrame, text="Start Session", command=startSession)
startButton.pack(side=tk.LEFT)
startButton.configure(height=BUTTON_HEIGHT,
                      width=BUTTON_WIDTH, font=("Arial", 12, "bold"))

breakButton = tk.Button(buttonFrame, text="Start Break", command=startBreak)
breakButton.pack(side=tk.LEFT)
breakButton.configure(height=BUTTON_HEIGHT,
                      width=BUTTON_WIDTH, font=("Arial", 12, "bold"))

resetButton = tk.Button(buttonFrame, text="Reset", command=resetPomodoro)
resetButton.pack(side=tk.LEFT)
resetButton.configure(height=BUTTON_HEIGHT,
                      width=BUTTON_WIDTH, font=("Arial", 12, "bold"))

tk.mainloop()
