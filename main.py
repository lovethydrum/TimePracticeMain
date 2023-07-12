import pygame
import sys
import os
import random
import ctypes


# This is needed for converting to an exe
def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Constants
LIGHT_GREEN = (208, 240, 192)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_RED = (255, 127, 127)
CREAM = (255, 255, 237)
GREEN = (44, 180, 44)
RETRO_GREEN = (137, 162, 91)
PINK = (255, 182, 193)
SKY_BLUE = (0, 181, 226)
# Variables
score = 0
high_score = 0
# Center the screen
ctypes.windll.user32.SetProcessDPIAware()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Initialize PYGAME
pygame.init()
pygame.mixer.init()

# Window setup
screen_width, screen_height = 1180, 710
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Numbers")
game_surface = pygame.Surface((1200, 750))
game_surface.fill(LIGHT_GREEN)
game_window.blit(game_surface, (0, 0))

# What Time Pictures
cross = pygame.image.load(resource_path("cross.png"))
check = pygame.image.load(resource_path("check.png"))
bath = pygame.image.load(resource_path("bath.png"))
bed = pygame.image.load(resource_path("bed.png"))
breakfast = pygame.image.load(resource_path("breakfast.png"))
dinner = pygame.image.load(resource_path("dinner.png"))
dream = pygame.image.load(resource_path("dream.png"))
homework = pygame.image.load(resource_path("homework.png"))
lunch = pygame.image.load(resource_path("lunch.png"))
snack = pygame.image.load(resource_path("snack.png"))
study = pygame.image.load(resource_path("study.png"))
wake_up = pygame.image.load(resource_path("wake_up.png"))
stopwatch_raw = pygame.image.load(resource_path("stopwatch.png"))
stopwatch = pygame.transform.scale(stopwatch_raw, (100, 100))
end_banner_raw = pygame.image.load(resource_path("end_banner.png"))
end_banner = pygame.transform.scale(end_banner_raw, (1100, 400))

pic_list = [bath, bed, breakfast, dinner, dream, homework, lunch, snack, study, wake_up]
random.shuffle(pic_list)

# What Time Audio
countdown_sound = pygame.mixer.Sound(resource_path("audio/countdown.ogg"))

bath_audio = pygame.mixer.Sound(resource_path("audio/bath.ogg"))
bed_audio = pygame.mixer.Sound(resource_path("audio/bed.ogg"))
breakfast_audio = pygame.mixer.Sound(resource_path("audio/breakfast.ogg"))
dinner_audio = pygame.mixer.Sound(resource_path("audio/dinner.ogg"))
dream_audio = pygame.mixer.Sound(resource_path("audio/dream.ogg"))
homework_audio = pygame.mixer.Sound(resource_path("audio/homework.ogg"))
lunch_audio = pygame.mixer.Sound(resource_path("audio/lunch.ogg"))
snack_audio = pygame.mixer.Sound(resource_path("audio/snack.ogg"))
study_audio = pygame.mixer.Sound(resource_path("audio/study.ogg"))
wake_up_audio = pygame.mixer.Sound(resource_path("audio/wake_up.ogg"))
what_time_audio_dictionary = {
    "bath": bath_audio,
    "bed": bed_audio,
    "breakfast": breakfast_audio,
    "dinner": dinner_audio,
    "dream": dream_audio,
    "homework": homework_audio,
    "lunch": lunch_audio,
    "snack": snack_audio,
    "study": study_audio,
    "wake_up": wake_up_audio,
    "": wake_up_audio
}

audio_list = ["bath", "bed", "breakfast", "dinner", "dream", "homework", "lunch", "snack", "study", "wake_up"]

# Pictures
end_banner_raw = pygame.image.load(resource_path("end_banner.png"))
end_banner = pygame.transform.scale(end_banner_raw, (1100, 400))
stopwatch_raw = pygame.image.load(resource_path("stopwatch.png"))
stopwatch = pygame.transform.scale(stopwatch_raw, (100, 100))
modoru_raw = pygame.image.load(resource_path("modoru.png"))
modoru = pygame.transform.scale(modoru_raw, (100, 100))
eraser_raw = pygame.image.load(resource_path("eraser.png"))
eraser = pygame.transform.scale(eraser_raw, (250, 250))
repeat_raw = pygame.image.load(resource_path("repeat.png"))
repeat = pygame.transform.scale(repeat_raw, (100, 100))
repeat_small = pygame.transform.scale(repeat_raw, (50, 50))
game_clock_image_raw = pygame.image.load(resource_path("clock.png"))
game_clock_image = pygame.transform.scale(game_clock_image_raw, (710, 710))
fight_image_raw = pygame.image.load(resource_path("fight.png"))
fight_image = pygame.transform.scale(fight_image_raw, (395, 245))
# Audio
correct_audio = pygame.mixer.Sound(resource_path("audio/correct.ogg"))
wrong_audio = pygame.mixer.Sound(resource_path("audio/wrong.ogg"))
oh_audio = pygame.mixer.Sound(resource_path("audio/oh.ogg"))
oh_clock_audio = pygame.mixer.Sound(resource_path("audio/ohclock.ogg"))
one_audio = pygame.mixer.Sound(resource_path("audio/one.ogg"))
two_audio = pygame.mixer.Sound(resource_path("audio/two.ogg"))
three_audio = pygame.mixer.Sound(resource_path("audio/three.ogg"))
four_audio = pygame.mixer.Sound(resource_path("audio/four.ogg"))
five_audio = pygame.mixer.Sound(resource_path("audio/five.ogg"))
six_audio = pygame.mixer.Sound(resource_path("audio/six.ogg"))
seven_audio = pygame.mixer.Sound(resource_path("audio/seven.ogg"))
eight_audio = pygame.mixer.Sound(resource_path("audio/eight.ogg"))
nine_audio = pygame.mixer.Sound(resource_path("audio/nine.ogg"))
ten_audio = pygame.mixer.Sound(resource_path("audio/ten.ogg"))
eleven_audio = pygame.mixer.Sound(resource_path("audio/eleven.ogg"))
twelve_audio = pygame.mixer.Sound(resource_path("audio/twelve.ogg"))
thirteen_audio = pygame.mixer.Sound(resource_path("audio/thirteen.ogg"))
fourteen_audio = pygame.mixer.Sound(resource_path("audio/fourteen.ogg"))
fifteen_audio = pygame.mixer.Sound(resource_path("audio/fifteen.ogg"))
sixteen_audio = pygame.mixer.Sound(resource_path("audio/sixteen.ogg"))
seventeen_audio = pygame.mixer.Sound(resource_path("audio/seventeen.ogg"))
eighteen_audio = pygame.mixer.Sound(resource_path("audio/eighteen.ogg"))
nineteen_audio = pygame.mixer.Sound(resource_path("audio/nineteen.ogg"))
twenty_audio = pygame.mixer.Sound(resource_path("audio/twenty.ogg"))
thirty_audio = pygame.mixer.Sound(resource_path("audio/thirty.ogg"))
forty_audio = pygame.mixer.Sound(resource_path("audio/forty.ogg"))
fifty_audio = pygame.mixer.Sound(resource_path("audio/fifty.ogg"))

audio_dictionary = {
    "1": [one_audio],
    "2": [two_audio],
    "3": [three_audio],
    "4": [four_audio],
    "5": [five_audio],
    "6": [six_audio],
    "7": [seven_audio],
    "8": [eight_audio],
    "9": [nine_audio],
    "10": [ten_audio],
    "11": [eleven_audio],
    "12": [twelve_audio],
    "13": [thirteen_audio],
    "14": [fourteen_audio],
    "15": [fifteen_audio],
    "16": [sixteen_audio],
    "17": [seventeen_audio],
    "18": [eighteen_audio],
    "19": [nineteen_audio],
    "20": [twenty_audio],
    "21": [twenty_audio, one_audio],
    "22": [twenty_audio, two_audio],
    "23": [twenty_audio, three_audio],
    "24": [twenty_audio, four_audio],
    "25": [twenty_audio, five_audio],
    "26": [twenty_audio, six_audio],
    "27": [twenty_audio, seven_audio],
    "28": [twenty_audio, eight_audio],
    "29": [twenty_audio, nine_audio],
    "30": [thirty_audio],
    "31": [thirty_audio, one_audio],
    "32": [thirty_audio, two_audio],
    "33": [thirty_audio, three_audio],
    "34": [thirty_audio, four_audio],
    "35": [thirty_audio, five_audio],
    "36": [thirty_audio, six_audio],
    "37": [thirty_audio, seven_audio],
    "38": [thirty_audio, eight_audio],
    "39": [thirty_audio, nine_audio],
    "40": [forty_audio],
    "41": [forty_audio, one_audio],
    "42": [forty_audio, two_audio],
    "43": [forty_audio, three_audio],
    "44": [forty_audio, four_audio],
    "45": [forty_audio, five_audio],
    "46": [forty_audio, six_audio],
    "47": [forty_audio, seven_audio],
    "48": [forty_audio, eight_audio],
    "49": [forty_audio, nine_audio],
    "50": [fifty_audio],
    "51": [fifty_audio, one_audio],
    "52": [fifty_audio, two_audio],
    "53": [fifty_audio, three_audio],
    "54": [fifty_audio, four_audio],
    "55": [fifty_audio, five_audio],
    "56": [fifty_audio, six_audio],
    "57": [fifty_audio, seven_audio],
    "58": [fifty_audio, eight_audio],
    "59": [fifty_audio, nine_audio],
}

oh_audio_length = int(1000*oh_audio.get_length())
oh_clock_audio_length = int(1000*oh_clock_audio.get_length())


class WhatTimeButton:
    def __init__(self, x, y, pic):
        self.pic = pic
        if self.pic == bath:
            self.name = "bath"
        elif self.pic == bed:
            self.name = "bed"
        elif self.pic == breakfast:
            self.name = "breakfast"
        elif self.pic == dinner:
            self.name = "dinner"
        elif self.pic == dream:
            self.name = "dream"
        elif self.pic == homework:
            self.name = "homework"
        elif self.pic == lunch:
            self.name = "lunch"
        elif self.pic == snack:
            self.name = "snack"
        elif self.pic == study:
            self.name = "study"
        elif self.pic == wake_up:
            self.name = "wake_up"
        self.width = self.pic.get_width()
        self.height = self.pic.get_height()
        self.x = x + ((255 - self.width)/2)
        self.y = y + ((165 - self.height)/2)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_button(self):
        game_window.blit(self.pic, (self.x, self.y), )
        pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), 4)


class QuestionGenerator:
    def __init__(self):
        self.answer = 0
        self.low_range = 1
        self.high_range = 59
        self.answer_hour = ""
        self.answer_minute = ""
        self.text_answer = str(self.answer)
        self.length = len(self.text_answer)

    def randomizer(self):
        self.answer = random.randint(self.low_range, self.high_range)
        self.text_answer = str(self.answer)
        self.length = len(self.text_answer)

    def clock_randomizer(self):
        self.answer_hour = str(random.randint(1, 12))
        self.answer_minute = str(random.randint(0, 59))

    def play_sound(self):
        # minute_length_1 = int(1000*audio_dictionary[self.answer_minute][0].get_length())

        if game_state == "number game" or game_state == "number prep":
            try:
                pygame.mixer.Sound.play(audio_dictionary[self.text_answer][0])
                pygame.time.delay(610)
            except:
                pass
            try:
                pygame.mixer.Sound.play(audio_dictionary[self.text_answer][1])
            except:
                pass
        elif game_state == "clock practice" or game_state == "clock prep" or game_state == "clock reference" \
                or game_state == "clock transition" or game_state == "clock duel":
            hour_length = int(1000 * audio_dictionary[self.answer_hour][0].get_length()) + 100
            pygame.mixer.Sound.play(audio_dictionary[self.answer_hour][0])
            pygame.time.delay(hour_length)
            if 0 < int(self.answer_minute) <= 9:
                pygame.mixer.Sound.play(oh_audio)
                pygame.time.delay(oh_audio_length)
                pygame.mixer.Sound.play(audio_dictionary[self.answer_minute][0])
            elif int(self.answer_minute) == 0:
                pygame.mixer.Sound.play(oh_clock_audio)
            else:
                minute_length = int(1000 * audio_dictionary[self.answer_minute][0].get_length())
                pygame.mixer.Sound.play(audio_dictionary[self.answer_minute][0])
                pygame.time.delay(minute_length)
                try:
                    pygame.mixer.Sound.play(audio_dictionary[self.answer_minute][1])
                except:
                    # print("fukken shaved by the audio exception")
                    pass

    def stop_sound(self):
        pygame.mixer.Sound.stop(audio_dictionary[self.text_answer][0])
        try:
            pygame.mixer.Sound.stop(audio_dictionary[self.text_answer][1])
        except:
            pass


# Font
calculator_font = pygame.font.Font(resource_path("calculator_font.ttf"), 55)
calculator_button_font = pygame.font.Font(None, 45)
timer_font = pygame.font.Font(None, 70)
clock_menu_font = pygame.font.Font(None, 100)
menu_font = pygame.font.Font(None, 150)
transition_font = pygame.font.Font(None, 500)
end_score_font = pygame.font.Font(None, 125)

# Timer
clock = pygame.time.Clock()
counter, text = 60, "60".rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
clock_text = str(counter).rjust(3)

pygame.time.set_timer(pygame.USEREVENT+1, 150)


class Button:
    def __init__(self, x, y, number):

        self.width = 80
        self.height = 80
        self.x = x
        self.y = y
        self.number = number
        self.color = BLACK
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_button(self):
        pygame.draw.rect(game_window, self.color, (self.x, self.y, self.width, self.height), )
        if self.number == "C":
            game_window.blit(calculator_button_font.render(self.number, True, (255, 255, 255)),
                             (self.x + 30, self.y + 30))
        elif self.number == "R":
            pass
        else:
            game_window.blit(calculator_button_font.render(self.number, True, (255, 255, 255)),
                             (self.x + 33, self.y + 30))
        pygame.draw.rect(game_window, self.color, (self.x, self.y, self.width, self.height), 4)


number_pad_1 = Button(450, 300, "1")
number_pad_2 = Button(550, 300, "2")
number_pad_3 = Button(650, 300, "3")
number_pad_4 = Button(450, 400, "4")
number_pad_5 = Button(550, 400, "5")
number_pad_6 = Button(650, 400, "6")
number_pad_7 = Button(450, 500, "7")
number_pad_8 = Button(550, 500, "8")
number_pad_9 = Button(650, 500, "9")
number_pad_0 = Button(450, 600, "0")
number_pad_c = Button(650, 600, "C")
number_pad_c.color = RED
number_pad_repeat = Button(550, 600, "R")
number_pad_repeat.color = WHITE

# number_pad_c.width = 180
# number_pad_c.rect = pygame.Rect(number_pad_c.x, number_pad_c.y, number_pad_c.width, number_pad_c.height)

number_pad_list = [number_pad_1, number_pad_2, number_pad_3, number_pad_4, number_pad_5, number_pad_6, number_pad_7,
                   number_pad_8, number_pad_9, number_pad_0]


class MenuButton:
    def __init__(self, x, y, color):
        self.width = 400
        self.height = 250
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_button(self):
        pygame.draw.rect(game_window, self.color, (self.x, self.y, self.width, self.height), )
        pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), 4)


menu_button_1 = MenuButton(40, 230, GREEN)
menu_button_1.width = 300
menu_button_1.height = 150
menu_button_1.rect = pygame.Rect(menu_button_1.x, menu_button_1.y, menu_button_1.width, menu_button_1.height)
menu_button_2 = MenuButton(40, 430, GREEN)
menu_button_2.width = 300
menu_button_2.height = 150
menu_button_2.rect = pygame.Rect(menu_button_2.x, menu_button_2.y, menu_button_2.width, menu_button_2.height)
menu_button_3 = MenuButton(850, 550, RED)
menu_button_3.width = 300
menu_button_3.height = 150
menu_button_3.rect = pygame.Rect(menu_button_3.x, menu_button_3.y, menu_button_3.width, menu_button_3.height)
main_menu_practice_button = MenuButton(826, 234, PINK)
main_menu_practice_button.width, main_menu_practice_button.height = 345, 130
main_menu_what_time_is_it_button = MenuButton(330, 130, WHITE)
main_menu_what_time_is_it_button.width, main_menu_what_time_is_it_button.height = 520, 150
main_menu_what_time_is_it_button.rect = pygame.Rect(main_menu_what_time_is_it_button.x, main_menu_what_time_is_it_button.y, main_menu_what_time_is_it_button.width, main_menu_what_time_is_it_button.height)
main_menu_numbers_button = MenuButton(390, 330, WHITE)
main_menu_numbers_button.width, main_menu_numbers_button.height = 400, 150
main_menu_numbers_button.rect = pygame.Rect(main_menu_numbers_button.x, main_menu_numbers_button.y, main_menu_numbers_button.width, main_menu_numbers_button.height)
main_menu_time_button = MenuButton(390, 530, WHITE)
main_menu_time_button.width, main_menu_time_button.height = 400, 150
main_menu_time_button.rect = pygame.Rect(main_menu_time_button.x, main_menu_time_button.y, main_menu_time_button.width, main_menu_time_button.height)
return_button = MenuButton(20, 640, WHITE)
return_button.width, return_button.height = 100, 50
return_button.rect = pygame.Rect(return_button.x, return_button.y, return_button.width, return_button.height)
clock_menu_return_button = MenuButton(1050, 640, WHITE)
clock_menu_return_button.width, clock_menu_return_button.height = 100, 50
clock_menu_return_button.rect = pygame.Rect(clock_menu_return_button.x, clock_menu_return_button.y, clock_menu_return_button.width, clock_menu_return_button.height)
clock_menu_reference_button = MenuButton(20, 100, RETRO_GREEN)
clock_menu_reference_button.width, clock_menu_reference_button.height = 350, 200
clock_menu_reference_button.rect = pygame.Rect(clock_menu_reference_button.x, clock_menu_reference_button.y, clock_menu_reference_button.width, clock_menu_reference_button.height)
clock_menu_practice_button = MenuButton(20, 400, PINK)
clock_menu_practice_button.width, clock_menu_practice_button.height = 350, 200
clock_menu_practice_button.rect = pygame.Rect(clock_menu_practice_button.x, clock_menu_practice_button.y, clock_menu_practice_button.width, clock_menu_practice_button.height)
clock_menu_duel_button = MenuButton(750, 17, RED)
clock_menu_duel_button_60 = MenuButton(780, 300, WHITE)
clock_menu_duel_button_60.width, clock_menu_duel_button_60.height = 120, 120
clock_menu_duel_button_60.rect = pygame.Rect(clock_menu_duel_button_60.x, clock_menu_duel_button_60.y, clock_menu_duel_button_60.width, clock_menu_duel_button_60.height)
clock_menu_duel_button_90 = MenuButton(1000, 300, WHITE)
clock_menu_duel_button_90.width, clock_menu_duel_button_90.height = 120, 120
clock_menu_duel_button_90.rect = pygame.Rect(clock_menu_duel_button_90.x, clock_menu_duel_button_90.y, clock_menu_duel_button_90.width, clock_menu_duel_button_90.height)
clock_menu_duel_button_120 = MenuButton(780, 470, WHITE)
clock_menu_duel_button_120.width, clock_menu_duel_button_120.height = 120, 120
clock_menu_duel_button_120.rect = pygame.Rect(clock_menu_duel_button_120.x, clock_menu_duel_button_120.y, clock_menu_duel_button_120.width, clock_menu_duel_button_120.height)
clock_menu_duel_button_150 = MenuButton(1000, 470, WHITE)
clock_menu_duel_button_150.width, clock_menu_duel_button_150.height = 120, 120
clock_menu_duel_button_150.rect = pygame.Rect(clock_menu_duel_button_150.x, clock_menu_duel_button_150.y, clock_menu_duel_button_150.width, clock_menu_duel_button_150.height)

clock_clear_button = MenuButton(800, 100, (255, 127, 0))
clock_clear_button.width, clock_clear_button.height = 300, 150
clock_clear_button.rect = pygame.Rect(clock_clear_button.x, clock_clear_button.y, clock_clear_button.width, clock_clear_button.height)
clock_repeat_button = MenuButton(800, 500, (255, 127, 0))
clock_repeat_button.width, clock_repeat_button.height = 300, 150
clock_repeat_button.rect = pygame.Rect(clock_repeat_button.x, clock_repeat_button.y, clock_repeat_button.width, clock_repeat_button.height)
ending_button = MenuButton(440, 520, GREEN)
ending_button.width, ending_button.height = 300, 150
# What Time Buttons
what_time_menu_button_1 = MenuButton(390, 300, GREEN)
what_time_menu_button_1.width, what_time_menu_button_1.height = 400, 180
what_time_menu_button_1.rect = pygame.Rect(what_time_menu_button_1.x, what_time_menu_button_1.y, what_time_menu_button_1.width, what_time_menu_button_1.height)
what_time_ending_button_1 = MenuButton(240, 520, RED)
what_time_ending_button_2 = MenuButton(640, 520, GREEN)
what_time_ending_button_1.width, what_time_ending_button_1.height = 300, 150
what_time_ending_button_2.width, what_time_ending_button_2.height = 300, 150
what_time_return_button = MenuButton(540, 400, WHITE)
what_time_return_button.width, what_time_return_button.height = 100, 50
what_time_return_button.rect = pygame.Rect(what_time_return_button.x, what_time_return_button.y,
                                           what_time_return_button.width, what_time_return_button.height)


def draw_return_button():
    return_button.draw_button()
    game_window.blit(modoru, (19, 620))
    game_window.blit(modoru, (20, 620))
    game_window.blit(modoru, (21, 620))


def draw_clock_return_button():
    clock_menu_return_button.draw_button()
    game_window.blit(modoru, (1049, 620))
    game_window.blit(modoru, (1050, 620))
    game_window.blit(modoru, (1051, 620))


class ClockButton:
    def __init__(self, x, y, width, height, hour, minute):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hour = hour
        self.minute = minute
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_clock_button(self):
        # pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), )
        pygame.draw.rect(game_window, BLACK, (self.x, self.y, self.width, self.height), 4)


class ClockPolygon:
    def __init__(self, point1, point2, point3, point4, hour, minute, flip):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4
        self.hour = hour
        self.minute = minute
        self.flip = flip
        if self.flip:
            self.drawpoints = [point4, point3, point2, point1]
        else:
            self.drawpoints = [point1, point2, point3, point4]

    def draw_polygon(self):
        pygame.draw.polygon(game_window, RED, (self.point1, self.point2, self.point3, self.point4), 4)

    def pointtest(self, point):
        # drawpoints is a list containing points defining your polygon
        # point is the mouse position
        # if it doesn't work, list them in opposite order.
        # works for arbitrary convex geometry
        x = point[0]

        y = point[1]
        Lines = []
        index = 0
        for index in range(len(self.drawpoints)):
            p0 = self.drawpoints[index]
            try:
                p1 = self.drawpoints[index + 1]
            except:
                p1 = self.drawpoints[0]
            Lines.append([p0, p1])
        for l in Lines:
            p0 = l[0]
            p1 = l[1]
            x0 = p0[0];
            y0 = p0[1]
            x1 = p1[0];
            y1 = p1[1]
            test = (y - y0) * (x1 - x0) - (x - x0) * (y1 - y0)
            if test < 0 : return False
        return True
    #
    # def draw_minute_hand(self):
    #     global minute_clicked
    #     pygame.draw.line(game_window, RED, (353, 353),
    #                      ((self.point3[0] + self.point4[0]) / 2, (self.point3[1] + self.point4[1]) / 2), width=10)
    #     pygame.display.update()
    #     minute_clicked = True

    def assign_minute_coordinates(self):
        if self.minute == "30":
            return (self.point1[0] + self.point2[0]) / 2, (self.point1[1] + self.point2[1]) / 2
        else:
            return (self.point3[0] + self.point4[0]) / 2, (self.point3[1] + self.point4[1]) / 2

    def assign_hour_coordinates(self):
        if self.hour == "1":
            return 455, 180
        elif self.hour == "2":
            return 530, 250
        elif self.hour == "3":
            return 573, 353
        elif self.hour == "4":
            return 530, 456
        elif self.hour == "5":
            return 447, 515
        elif self.hour == "6":
            return 353, 550
        elif self.hour == "7":
            return 260, 510
        elif self.hour == "8":
            return 175, 455
        elif self.hour == "9":
            return 150, 353
        elif self.hour == "10":
            return 190, 260
        elif self.hour == "11":
            return 263, 200
        elif self.hour == "12":
            return 353, 160


CENTER = 353

# center_check = ClockPolygon((353, 353), (354, 353), (354, 354), (353, 354), "center", "center")
one_button = ClockPolygon((375, 5), (405, 7), (395, 50), (375, 50), "no", "1", False)
two_button = ClockPolygon((415, 8), (442, 15), (427, 50), (405, 50), "no", "2", False)
three_button = ClockPolygon((452, 17), (475, 29), (460, 60), (436, 52), "no", "3", False)
four_button = ClockPolygon((485, 31), (508, 42), (485, 75), (468, 65), "no", "4", False)
five_button = ClockPolygon((515, 46), (540, 59), (510, 110), (485, 100), "1", "5", False)
six_button = ClockPolygon((545, 64), (568, 80), (540, 110), (525, 95), "no", "6", False)
seven_button = ClockPolygon((575, 84), (593, 105), (570, 130), (550, 115), "no", "7", False)
eight_button = ClockPolygon((600, 110), (618, 130), (585, 155), (575, 140), "no", "8", False)
nine_button = ClockPolygon((625, 135), (643, 159), (608, 178), (595, 164), "no", "9", False)
ten_button = ClockPolygon((648, 167), (663, 194), (613, 213), (600, 199), "2", "10", False)
eleven_button = ClockPolygon((664, 200), (675, 228), (635, 233), (620, 225), "no", "11", False)
twelve_button = ClockPolygon((680, 233), (685, 258), (645, 268), (635, 245), "no", "12", False)
thirteen_button = ClockPolygon((690, 268), (695, 293), (655, 298), (650, 280), "no", "13", False)
fourteen_button = ClockPolygon((698, 303), (700, 330), (655, 328), (650, 310), "no", "14", False)
fifteen_button = ClockPolygon((700, 340), (700, 367), (645, 367), (645, 340), "3", "15", False)
sixteen_button = ClockPolygon((698, 303 + 2 * (CENTER - 303)), (700, 330 + 2 * (CENTER - 330)),
                              (655, 328 + 2 * (CENTER - 328)), (650, 310 + 2 * (CENTER - 310)), "no", "16", True)
seventeen_button = ClockPolygon((690, 268 + 2 * (CENTER - 268)), (695, 293 + 2 * (CENTER - 293)),
                                (655, 298 + 2 * (CENTER - 298)), (650, 280 + 2 * (CENTER - 280)), "no", "17", True)
eighteen_button = ClockPolygon((680, 233 + 2 * (CENTER - 233)), (685, 258 + 2 * (CENTER - 258)),
                               (645, 268 + 2 * (CENTER - 268)), (635, 245 + 2 * (CENTER - 245)), "no", "18", True)
nineteen_button = ClockPolygon((664, 200 + 2 * (CENTER - 200)), (675, 228 + 2 * (CENTER - 228)),
                               (635, 233 + 2 * (CENTER - 233)), (620, 225 + 2 * (CENTER - 225)), "no", "19", True)
twenty_button = ClockPolygon((648, 167 + 2 * (CENTER - 167)), (663, 194 + 2 * (CENTER - 194)),
                             (613, 213 + 2 * (CENTER - 213)), (600, 199 + 2 * (CENTER - 199)), "4", "20", True)
twenty_one_button = ClockPolygon((625, 135 + 2 * (CENTER - 135)), (643, 159 + 2 * (CENTER - 159)),
                                 (608, 178 + 2 * (CENTER - 178)), (595, 164 + 2 * (CENTER - 164)), "no", "21", True)
twenty_two_button = ClockPolygon((600, 110 + 2 * (CENTER - 110)), (618, 130 + 2 * (CENTER - 130)),
                                 (585, 155 + 2 * (CENTER - 155)), (575, 140 + 2 * (CENTER - 140)), "no", "22", True)
twenty_three_button = ClockPolygon((575, 84 + 2 * (CENTER - 84)), (593, 105 + 2 * (CENTER - 105)),
                                   (570, 130 + 2 * (CENTER - 130)), (550, 115 + 2 * (CENTER - 115)), "no", "23", True)
twenty_four_button = ClockPolygon((545, 64 + 2 * (CENTER - 64)), (568, 80 + 2 * (CENTER - 80)),
                                  (540, 110 + 2 * (CENTER - 110)), (525, 95 + 2 * (CENTER - 95)), "no", "24", True)
twenty_five_button = ClockPolygon((515, 46 + 2 * (CENTER - 46)), (540, 59 + 2 * (CENTER - 59)),
                                  (510, 110 + 2 * (CENTER - 110)), (485, 100 + 2 * (CENTER - 100)), "5", "25", True)
twenty_six_button = ClockPolygon((485, 31 + 2 * (CENTER - 31)), (508, 42 + 2 * (CENTER - 42)),
                                 (485, 75 + 2 * (CENTER - 75)), (468, 65 + 2 * (CENTER - 65)), "no", "26", True)
twenty_seven_button = ClockPolygon((452, 17 + 2 * (CENTER - 17)), (475, 29 + 2 * (CENTER - 29)),
                                   (460, 60 + 2 * (CENTER - 60)), (436, 52 + 2 * (CENTER - 52)), "no", "27", True)
twenty_eight_button = ClockPolygon((415, 8 + 2 * (CENTER - 8)), (442, 15 + 2 * (CENTER - 15)),
                                   (427, 50 + 2 * (CENTER - 50)), (405, 50 + 2 * (CENTER - 50)), "no", "28", True)
twenty_nine_button = ClockPolygon((375, 5 + 2 * (CENTER - 5)), (405, 7 + 2 * (CENTER - 7)),
                                  (395, 50 + 2 * (CENTER - 50)), (375, 50 + 2 * (CENTER - 50)), "no", "29", True)
thirty_button = ClockPolygon((340, 645), (367, 645), (367, 700,), (340, 700), "6", "30", False)
thirty_one_button = ClockPolygon((CENTER - (375 - CENTER), 5 + 2 * (CENTER - 5)),
                                 (CENTER - (405 - CENTER), 7 + 2 * (CENTER - 7)),
                                 (CENTER - (395 - CENTER), 50 + 2 * (CENTER - 50)),
                                 (CENTER - (375 - CENTER), 50 + 2 * (CENTER - 50)), "no", "31", False)
thirty_two_button = ClockPolygon((CENTER - (415 - CENTER), 8 + 2 * (CENTER - 8)),
                                 (CENTER - (442 - CENTER), 15 + 2 * (CENTER - 15)),
                                 (CENTER - (427 - CENTER), 50 + 2 * (CENTER - 50)),
                                 (CENTER - (405 - CENTER), 50 + 2 * (CENTER - 50)), "no", "32", False)
thirty_three_button = ClockPolygon((CENTER - (452 - CENTER), 17 + 2 * (CENTER - 17)),
                                   (CENTER - (475 - CENTER), 29 + 2 * (CENTER - 29)),
                                   (CENTER - (460 - CENTER), 60 + 2 * (CENTER - 60)),
                                   (CENTER - (436 - CENTER), 52 + 2 * (CENTER - 52)), "no", "33", False)
thirty_four_button = ClockPolygon((CENTER - (485 - CENTER), 31 + 2 * (CENTER - 31)),
                                  (CENTER - (508 - CENTER), 42 + 2 * (CENTER - 42)),
                                  (CENTER - (485 - CENTER), 75 + 2 * (CENTER - 75)),
                                  (CENTER - (468 - CENTER), 65 + 2 * (CENTER - 65)), "no", "34", False)
thirty_five_button = ClockPolygon((CENTER - (515 - CENTER), 46 + 2 * (CENTER - 46)),
                                  (CENTER - (540 - CENTER), 59 + 2 * (CENTER - 59)),
                                  (CENTER - (510 - CENTER), 110 + 2 * (CENTER - 110)),
                                  (CENTER - (485 - CENTER), 100 + 2 * (CENTER - 100)), "7", "35", False)
thirty_six_button = ClockPolygon((CENTER - (545 - CENTER), 64 + 2 * (CENTER - 64)),
                                 (CENTER - (568 - CENTER), 80 + 2 * (CENTER - 80)),
                                 (CENTER - (540 - CENTER), 110 + 2 * (CENTER - 110)),
                                 (CENTER - (525 - CENTER), 95 + 2 * (CENTER - 95)), "no", "36", False)
thirty_seven_button = ClockPolygon((CENTER - (575 - CENTER), 84 + 2 * (CENTER - 84)),
                                   (CENTER - (593 - CENTER), 105 + 2 * (CENTER - 105)),
                                   (CENTER - (570 - CENTER), 130 + 2 * (CENTER - 130)),
                                   (CENTER - (550 - CENTER), 115 + 2 * (CENTER - 115)), "no", "37", False)
thirty_eight_button = ClockPolygon((CENTER - (600 - CENTER), 110 + 2 * (CENTER - 110)),
                                   (CENTER - (618 - CENTER), 130 + 2 * (CENTER - 130)),
                                   (CENTER - (585 - CENTER), 155 + 2 * (CENTER - 155)),
                                   (CENTER - (575 - CENTER), 140 + 2 * (CENTER - 140)), "no", "38", False)
thirty_nine_button = ClockPolygon((CENTER - (625 - CENTER), 135 + 2 * (CENTER - 135)),
                                  (CENTER - (643 - CENTER), 159 + 2 * (CENTER - 159)),
                                  (CENTER - (608 - CENTER), 178 + 2 * (CENTER - 178)),
                                  (CENTER - (595 - CENTER), 164 + 2 * (CENTER - 164)), "no", "39", False)
forty_button = ClockPolygon((CENTER - (648 - CENTER), 167 + 2 * (CENTER - 167)),
                            (CENTER - (663 - CENTER), 194 + 2 * (CENTER - 194)),
                            (CENTER - (613 - CENTER), 213 + 2 * (CENTER - 213)),
                            (CENTER - (600 - CENTER), 199 + 2 * (CENTER - 199)), "8", "40", False)
forty_one_button = ClockPolygon((CENTER - (664 - CENTER), 200 + 2 * (CENTER - 200)),
                                (CENTER - (675 - CENTER), 228 + 2 * (CENTER - 228)),
                                (CENTER - (635 - CENTER), 233 + 2 * (CENTER - 233)),
                                (CENTER - (620 - CENTER), 225 + 2 * (CENTER - 225)), "no", "41", False)
forty_two_button = ClockPolygon((CENTER - (680 - CENTER), 233 + 2 * (CENTER - 233)),
                                (CENTER - (685 - CENTER), 258 + 2 * (CENTER - 258)),
                                (CENTER - (645 - CENTER), 268 + 2 * (CENTER - 268)),
                                (CENTER - (635 - CENTER), 245 + 2 * (CENTER - 245)), "no", "42", False)
forty_three_button = ClockPolygon((CENTER - (690 - CENTER), 268 + 2 * (CENTER - 268)),
                                  (CENTER - (695 - CENTER), 293 + 2 * (CENTER - 293)),
                                  (CENTER - (655 - CENTER), 298 + 2 * (CENTER - 298)),
                                  (CENTER - (650 - CENTER), 280 + 2 * (CENTER - 280)), "no", "43", False)
forty_four_button = ClockPolygon((CENTER - (698 - CENTER), 303 + 2 * (CENTER - 303)),
                                 (CENTER - (700 - CENTER), 330 + 2 * (CENTER - 330)),
                                 (CENTER - (655 - CENTER), 328 + 2 * (CENTER - 328)),
                                 (CENTER - (650 - CENTER), 310 + 2 * (CENTER - 310)), "no", "44", False)
forty_five_button = ClockPolygon((10, 340), (10, 367), (65, 367), (65, 340), "9", "45", True)
forty_six_button = ClockPolygon((CENTER - (698 - CENTER), 303), (CENTER - (700 - CENTER), 330),
                                (CENTER - (655 - CENTER), 328), (CENTER - (650 - CENTER), 310), "no", "46", True)
forty_seven_button = ClockPolygon((CENTER - (690 - CENTER), 268), (CENTER - (695 - CENTER), 293),
                                  (CENTER - (655 - CENTER), 298), (CENTER - (650 - CENTER), 280 + 2), "no", "47", True)
forty_eight_button = ClockPolygon((CENTER - (680 - CENTER), 233), (CENTER - (685 - CENTER), 258),
                                  (CENTER - (645 - CENTER), 268), (CENTER - (635 - CENTER), 245), "no", "48", True)
forty_nine_button = ClockPolygon((CENTER - (664 - CENTER), 200), (CENTER - (675 - CENTER), 228),
                                 (CENTER - (635 - CENTER), 233), (CENTER - (620 - CENTER), 225), "no", "49", True)
fifty_button = ClockPolygon((CENTER - (648 - CENTER), 167), (CENTER - (663 - CENTER), 194),
                            (CENTER - (613 - CENTER), 213), (CENTER - (600 - CENTER), 199), "10", "50", True)
fifty_one_button = ClockPolygon((CENTER - (625 - CENTER), 135), (CENTER - (643 - CENTER), 159),
                                (CENTER - (608 - CENTER), 178), (CENTER - (595 - CENTER), 164), "no", "51", True)
fifty_two_button = ClockPolygon((CENTER - (600 - CENTER), 110), (CENTER - (618 - CENTER), 130),
                                (CENTER - (585 - CENTER), 155), (CENTER - (575 - CENTER), 140), "no", "52", True)
fifty_three_button = ClockPolygon((CENTER - (575 - CENTER), 84), (CENTER - (593 - CENTER), 105),
                                  (CENTER - (570 - CENTER), 130), (CENTER - (550 - CENTER), 115), "no", "53", True)
fifty_four_button = ClockPolygon((CENTER - (545 - CENTER), 64), (CENTER - (568 - CENTER), 80),
                                 (CENTER - (540 - CENTER), 110), (CENTER - (525 - CENTER), 95), "no", "54", True)
fifty_five_button = ClockPolygon((CENTER - (515 - CENTER), 46), (CENTER - (540 - CENTER), 59),
                                 (CENTER - (510 - CENTER), 110), (CENTER - (485 - CENTER), 100), "11", "55", True)
fifty_six_button = ClockPolygon((CENTER - (485 - CENTER), 31), (CENTER - (508 - CENTER), 42),
                                (CENTER - (485 - CENTER), 75), (CENTER - (468 - CENTER), 65), "no", "56", True)
fifty_seven_button = ClockPolygon((CENTER - (452 - CENTER), 17), (CENTER - (475 - CENTER), 29),
                                  (CENTER - (460 - CENTER), 60), (CENTER - (436 - CENTER), 52), "no", "57", True)
fifty_eight_button = ClockPolygon((CENTER - (415 - CENTER), 8), (CENTER - (442 - CENTER), 15),
                                  (CENTER - (427 - CENTER), 50), (CENTER - (405 - CENTER), 50), "no", "58", True)
fifty_nine_button = ClockPolygon((CENTER - (375 - CENTER), 5), (CENTER - (405 - CENTER), 7),
                                 (CENTER - (395 - CENTER), 50), (CENTER - (375 - CENTER), 50), "no", "59", True)
sixty_button = ClockPolygon((340, 5), (367, 5), (367, 60,), (340, 60), "12", "0", False)

clock_button_list = [one_button, two_button, three_button, four_button, five_button, six_button,
                     seven_button, eight_button, nine_button, ten_button, eleven_button, twelve_button, thirteen_button,
                     fourteen_button, fifteen_button, sixteen_button, seventeen_button, eighteen_button,
                     nineteen_button, twenty_button, twenty_one_button, twenty_two_button, twenty_three_button,
                     twenty_four_button, twenty_five_button, twenty_six_button, twenty_seven_button, twenty_eight_button,
                     twenty_nine_button, thirty_button, thirty_one_button, thirty_two_button, thirty_three_button,
                     thirty_four_button, thirty_five_button, thirty_six_button, thirty_seven_button,
                     thirty_eight_button, thirty_nine_button, forty_button, forty_one_button, forty_two_button,
                     forty_three_button, forty_four_button, forty_five_button, forty_six_button, forty_seven_button,
                     forty_eight_button, forty_nine_button, fifty_button, fifty_one_button, fifty_two_button,
                     fifty_three_button, fifty_four_button, fifty_five_button, fifty_six_button, fifty_seven_button,
                     fifty_eight_button, fifty_nine_button, sixty_button
                     ]


class GameClock:
    def __init__(self):
        self.x = 0
        self.y = -2
        self.pic = game_clock_image

    def draw_clock(self):
        game_surface.fill(color=WHITE)
        game_window.blit(game_surface, (0, 0))
        for items in clock_button_list:
            items.draw_polygon()
        game_window.blit(self.pic, (self.x, self.y))
        draw_return_button()
        if not game_state == "clock reference" and not game_state == "clock menu":
            clock_repeat_button.draw_button()
            game_window.blit(repeat, (895, 530))
        clock_clear_button.draw_button()
        game_window.blit(eraser, (820, 50))
        pygame.display.update()


game_clock = GameClock()


def draw_minute_hand(coordinates):
    pygame.draw.line(game_window, RED, (353, 353), coordinates, width=10)
    pygame.display.update()


def draw_hour_hand(coordinates):
    pygame.draw.line(game_window, GREEN, (353, 353), coordinates, width=20)
    pygame.display.update()


class Timer:
    def __init__(self):
        self.x = 540
        self.y = 50
        self.color = LIGHT_GREEN
        self.width = stopwatch.get_width()
        self.height = stopwatch.get_height()

    def draw_timer(self):
        timer_text = str(counter).rjust(3)
        game_window.blit(stopwatch, (self.x, self.y), )
        pygame.draw.rect(game_window, self.color, (self.x + 20, self.y + 29, 58, 52))
        game_window.blit(timer_font.render(timer_text, True, (0, 0, 0)), (self.x + 8, self.y + 33))
        pygame.display.update()


timer = Timer()
what_time_timer = Timer()
what_time_timer.y = 275
button_locations = [(310, 10), (610, 10), (910, 10), (10, 10), (10, 260),
                    (10, 510), (910, 260), (310, 510), (610, 510), (910, 510)]
random.shuffle(button_locations)

button_list = [WhatTimeButton(button_locations[x - 1][0], button_locations[x - 1][1], pic_list[x - 1]) for x in range(10)]
answer = ""


def stop_sounds():
    pygame.mixer.Sound.stop(bath_audio)
    pygame.mixer.Sound.stop(bed_audio)
    pygame.mixer.Sound.stop(breakfast_audio)
    pygame.mixer.Sound.stop(dinner_audio)
    pygame.mixer.Sound.stop(dream_audio)
    pygame.mixer.Sound.stop(homework_audio)
    pygame.mixer.Sound.stop(lunch_audio)
    pygame.mixer.Sound.stop(snack_audio)
    pygame.mixer.Sound.stop(study_audio)
    pygame.mixer.Sound.stop(wake_up_audio)


def refresh_question():
    global button_list
    global what_time_timer
    global button_locations
    global pic_list
    global audio_list
    global answer
    stop_sounds()
    answer = random.choice(audio_list)
    random.shuffle(button_locations)
    random.shuffle(pic_list)
    button_list = [WhatTimeButton(button_locations[x - 1][0], button_locations[x - 1][1], pic_list[x - 1]) for x
                   in range(10)]
    game_window.blit(game_surface, (0, 0))
    for buttons in button_list:
        buttons.draw_button()
    what_time_timer.draw_timer()
    what_time_return_button.draw_button()
    game_window.blit(modoru, (539, 380))
    game_window.blit(modoru, (540, 380))
    game_window.blit(modoru, (541, 380))


def what_time_transition_screen():
    # First Blip
    game_surface.fill(BLACK)
    game_window.blit(game_surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(100)
    game_surface.fill(LIGHT_GREEN)
    game_window.blit(game_surface, (0, 0))
    game_window.blit(transition_font.render("3", True, (0, 0, 0)), (500, 190))
    pygame.mixer.Sound.play(countdown_sound)
    pygame.display.update()
    pygame.time.delay(900)
    # Second Blip
    game_surface.fill(BLACK)
    game_window.blit(game_surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(100)
    game_surface.fill(LIGHT_GREEN)
    game_window.blit(game_surface, (0, 0))
    game_window.blit(transition_font.render("2", True, (0, 0, 0)), (500, 190))
    pygame.display.update()
    pygame.time.delay(900)
    # Third Blip
    game_surface.fill(BLACK)
    game_window.blit(game_surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(100)
    game_surface.fill(LIGHT_GREEN)
    game_window.blit(game_surface, (0, 0))
    game_window.blit(transition_font.render("1", True, (0, 0, 0)), (500, 190))
    pygame.display.update()
    pygame.time.delay(900)
    pygame.display.update()
    # Go Blip
    game_surface.fill(BLACK)
    game_window.blit(game_surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(100)
    game_surface.fill(LIGHT_GREEN)
    game_window.blit(game_surface, (0, 0))
    game_window.blit(transition_font.render("GO", True, (0, 0, 0)), (320, 190))
    pygame.display.update()
    pygame.time.delay(1000)
    pygame.display.update()
    pygame.time.delay(150)


# Create the menu buttons


class Scoreboard:
    def __init__(self):
        self.score = 0
        self.number_one_to_twenty_high_score = 999
        self.number_twenty_one_to_sixty_high_score = 999
        self.number_one_to_sixty_high_score = 999
        self.time_high_score = 999
        self.duel_turn = 1
        self.duel_player_1 = 50
        self.duel_player_2 = 50

    def increase_score(self):
        self.score += 1
        # if game_state == "number game":
        #     if self.score >= self.number_high_score:
        #         self.number_high_score = self.score
        # elif game_state == "time game":
        #     if self.score >= self.time_high_score:
        #         self.time_high_score = self.score
        # print(f"{game_state}:  {self.score}")

    def reset_score(self):
        global counter
        global question_generator
        if game_state == "number game":
            if question_generator.low_range == 1:
                if question_generator.high_range == 59:
                    if counter <= self.number_one_to_sixty_high_score:
                        self.number_one_to_sixty_high_score = counter
                else:
                    if counter <= self.number_one_to_twenty_high_score:
                        self.number_one_to_twenty_high_score = counter
            else:
                if question_generator.low_range == 21:
                    if counter <= self.number_twenty_one_to_sixty_high_score:
                        self.number_twenty_one_to_sixty_high_score = counter
        elif game_state == "time game":
            if counter >= self.time_high_score:
                self.time_high_score = counter
        self.score = 0

    def duel_adjustment(self):
        if self.duel_turn == 1:
            self.duel_player_1 -= 1
            self.duel_player_2 += 1
        if self.duel_turn == 2:
            self.duel_player_2 -= 1
            self.duel_player_1 += 1
        # print("_________________________________")
        # print(f"Player 1:  {self.duel_player_1}")
        # print(f"Player 2:  {self.duel_player_2}")
        # print("_________________________________")


scoreboard = Scoreboard()


def draw_main_menu():
    game_surface.fill(color=(100, 250, 208))
    game_window.blit(game_surface, (0, 0))
    menu_title = menu_font.render("Game Modes", True, (0, 0, 0), )
    game_window.blit(menu_title, (270, 5))
    main_menu_what_time_is_it_button.draw_button()
    game_window.blit(end_score_font.render("What Time?", True, (0, 0, 0), ), (344, 165))
    main_menu_numbers_button.draw_button()
    game_window.blit(end_score_font.render("Numbers", True, (0, 0, 0), ), (404, 360))
    main_menu_time_button.draw_button()
    game_window.blit(end_score_font.render("Clock", True, (0, 0, 0), ), (468, 565))
    # game_window.blit(timer_font.render(f"High Score:  {scoreboard.number_high_score}", True, (0, 0, 0), ), (715, 345))
    # game_window.blit(timer_font.render(f"High Score:  {scoreboard.time_high_score}", True, (0, 0, 0), ), (430, 625))

    pygame.display.update()


def draw_menu_2():
    game_surface.fill(color=LIGHT_GREEN)
    game_window.blit(game_surface, (0, 0))
    draw_return_button()
    menu_button_1.draw_button()
    menu_button_2.draw_button()
    menu_button_3.draw_button()
    menu_title = menu_font.render("Numbers Challenge", True, (0, 0, 0), )
    game_window.blit(menu_title, (80, 70))
    one_to_twenty_button_text = menu_font.render("1-20", True, (0, 0, 0), )
    game_window.blit(one_to_twenty_button_text, (73, 260))
    twenty_one_to_sixty_button_text = menu_font.render("21-59", True, (0, 0, 0), )
    game_window.blit(twenty_one_to_sixty_button_text, (56, 460))
    one_to_sixty_button_text = menu_font.render("MAX", True, (0, 0, 0), )
    game_window.blit(one_to_sixty_button_text, (885, 576))
    main_menu_practice_button.draw_button()
    game_window.blit(end_score_font.render("Practice", True, (0, 0, 0), ), (826, 260))
    if scoreboard.number_one_to_twenty_high_score == 999:
        game_window.blit(
            timer_font.render(f"High Score:  -- ", True, (0, 0, 0), ),
            (375, 275))
    else:
        game_window.blit(timer_font.render(f"High Score:  {scoreboard.number_one_to_twenty_high_score}s", True, (0, 0, 0), ), (375, 275))
    if scoreboard.number_twenty_one_to_sixty_high_score == 999:
        game_window.blit(
            timer_font.render(f"High Score:  -- ", True, (0, 0, 0), ),
            (375, 475))
    else:
        game_window.blit(timer_font.render(f"High Score:  {scoreboard.number_twenty_one_to_sixty_high_score}s", True, (0, 0, 0), ), (375, 475))
    if scoreboard.number_one_to_sixty_high_score == 999:
        game_window.blit(
            timer_font.render(f"High Score:  -- ", True, (0, 0, 0), ),
            (375, 615))
    else:
        game_window.blit(timer_font.render(f"High Score:  {scoreboard.number_one_to_sixty_high_score} s", True, (0, 0, 0), ), (375, 615))
    pygame.display.update()


def draw_clock_menu():
    game_surface.fill(color=(197, 180, 227))
    game_window.blit(game_surface, (0, 0))
    draw_clock_return_button()
    clock_menu_duel_button.draw_button()
    game_window.blit(fight_image, (753, 20))
    # game_window.blit(menu_font.render(f"BATTLE", True, (0, 0, 0), ), (745, 10))
    clock_menu_practice_button.draw_button()
    clock_menu_reference_button.draw_button()
    clock_menu_duel_button_60.draw_button()
    game_window.blit(clock_menu_font.render("60", True, (0, 0, 0), ), (800, 330))
    clock_menu_duel_button_90.draw_button()
    game_window.blit(clock_menu_font.render("90", True, (0, 0, 0), ), (1022, 330))
    clock_menu_duel_button_120.draw_button()
    game_window.blit(clock_menu_font.render("120", True, (0, 0, 0), ), (780, 500))
    clock_menu_duel_button_150.draw_button()
    game_window.blit(clock_menu_font.render("150", True, (0, 0, 0), ), (1002, 500))
    game_window.blit(clock_menu_font.render(f"Practice", True, (0, 0, 0), ), (55, 170))
    game_window.blit(clock_menu_font.render(f"Listening", True, (0, 0, 0), ), (40, 470))
    pygame.display.update()


player_input = ""


def display_calculator_input():
    global player_input
    pygame.draw.rect(game_window, RETRO_GREEN, (450, 200, 280, 60))
    pygame.draw.rect(game_window, BLACK, (450, 200, 280, 60), 4)
    if len(player_input) >= 1:
        game_window.blit(calculator_font.render(f"{player_input}", True, (0, 0, 0), ),
                         (700 - (23 * (len(player_input) - 1)), 195))
    else:
        game_window.blit(calculator_font.render(f"{player_input}", True, (0, 0, 0), ), (700, 195))
    pygame.display.update()


def display_correct_calculator_input():
    global player_input
    pygame.draw.rect(game_window, GREEN, (450, 200, 280, 60))
    pygame.draw.rect(game_window, BLACK, (450, 200, 280, 60), 4)
    if len(player_input) >= 1:
        game_window.blit(calculator_font.render(f"{player_input}", True, (0, 0, 0), ),
                         (700 - (23 * (len(player_input) - 1)), 195))
    else:
        game_window.blit(calculator_font.render(f"{player_input}", True, (0, 0, 0), ), (700, 195))
    pygame.display.update()


def display_incorrect_calculator_input():
    global player_input
    pygame.draw.rect(game_window, RED, (450, 200, 280, 60))
    pygame.draw.rect(game_window, BLACK, (450, 200, 280, 60), 4)
    if len(player_input) >= 1:
        game_window.blit(calculator_font.render(f"{player_input}", True, (0, 0, 0), ),
                         (700 - (23 * (len(player_input) - 1)), 195))
    else:
        game_window.blit(calculator_font.render(f"{player_input}", True, (0, 0, 0), ), (700, 195))
    pygame.display.update()


def draw_number_pad():
    game_surface.fill(color=LIGHT_GREEN)
    game_window.blit(game_surface, (0, 0))
    draw_return_button()
    pygame.draw.rect(game_window, (211, 211, 211), (420, 160, 345, 540), )
    pygame.draw.rect(game_window, BLACK, (420, 160, 345, 540), 5)
    pygame.draw.rect(game_window, RETRO_GREEN, (450, 200, 280, 60))
    pygame.draw.rect(game_window, BLACK, (450, 200, 280, 60), 4)
    display_calculator_input()
    number_pad_c.draw_button()
    number_pad_repeat.draw_button()
    game_window.blit(repeat_small, (564, 618))
    for buttons in number_pad_list:
        buttons.draw_button()
        pygame.display.update()


def reset():
    global player_input
    player_input = ""
    question_generator.randomizer()
    question_generator.play_sound()
    # draw_number_pad()
    display_calculator_input()
    pygame.display.update()


def transition_screen():
    global scoreboard
    # First Blip
    if scoreboard.duel_turn == 1:
        player_color = LIGHT_RED
    elif scoreboard.duel_turn == 2:
        player_color = CREAM
    game_surface.fill(BLACK)
    game_window.blit(game_surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(100)
    game_surface.fill(player_color)
    game_window.blit(game_surface, (0, 0))
    game_window.blit(transition_font.render("3", True, (0, 0, 0)), (500, 90))
    game_window.blit(end_score_font.render(f"Player 1", True, (0, 0, 0)), (120, 500))
    game_window.blit(end_score_font.render(f"{scoreboard.duel_player_1}s", True, (0, 0, 0)), (200, 600))
    # pygame.mixer.Sound.play(countdown_sound)
    pygame.display.update()
    pygame.time.delay(900)
    # Second Blip
    game_surface.fill(BLACK)
    game_window.blit(game_surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(100)
    game_surface.fill(player_color)
    game_window.blit(game_surface, (0, 0))
    game_window.blit(transition_font.render("2", True, (0, 0, 0)), (500, 90))
    game_window.blit(end_score_font.render(f"Player 2", True, (0, 0, 0)), (720, 500))
    game_window.blit(end_score_font.render(f"{scoreboard.duel_player_2}s", True, (0, 0, 0)), (800, 600))
    pygame.display.update()
    pygame.time.delay(900)
    # Third Blip
    game_surface.fill(BLACK)
    game_window.blit(game_surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(100)
    game_surface.fill(player_color)
    game_window.blit(game_surface, (0, 0))
    game_window.blit(transition_font.render("1", True, (0, 0, 0)), (500, 90))
    game_window.blit(end_score_font.render(f"Player 1", True, (0, 0, 0)), (120, 500))
    game_window.blit(end_score_font.render(f"Player 2", True, (0, 0, 0)), (720, 500))
    game_window.blit(end_score_font.render(f"{scoreboard.duel_player_1}s", True, (0, 0, 0)), (200, 600))
    game_window.blit(end_score_font.render(f"{scoreboard.duel_player_2}s", True, (0, 0, 0)), (800, 600))
    pygame.display.update()
    pygame.time.delay(900)
    pygame.display.update()
    # Go Blip
    game_surface.fill(BLACK)
    game_window.blit(game_surface, (0, 0))
    pygame.display.update()
    pygame.time.delay(100)
    game_surface.fill(player_color)
    game_window.blit(game_surface, (0, 0))
    game_window.blit(transition_font.render("GO", True, (0, 0, 0)), (320, 190))
    pygame.display.update()
    pygame.time.delay(650)
    pygame.display.update()
    # pygame.time.delay(150)
    pygame.event.clear(pygame.USEREVENT+1)


def draw_duel_game_over_menu():
    global scoreboard
    if scoreboard.duel_player_1 > 0:
        game_surface.fill(LIGHT_RED)
    else:
        game_surface.fill(CREAM)
    game_window.blit(game_surface, (0, 0))
    ending_button.draw_button()
    game_window.blit(end_score_font.render("OK", True, (0, 0, 0), ), (525, 560))
    # game_window.blit(menu_font.render("Game Over!", True, (0, 0, 0), ), (190, 70))
    if scoreboard.duel_player_1 > 0:
        game_window.blit(end_score_font.render("Player 1 Wins!", True, (0, 0, 0), ), (305, 100))
    elif scoreboard.duel_player_1 <= 0:
        game_window.blit(end_score_font.render("Player 2 Wins!", True, (0, 0, 0), ), (305, 100))
    game_window.blit(end_banner, (40, 10))
    pygame.display.update()


def draw_what_time_menu():
    game_surface.fill(color=SKY_BLUE)
    game_window.blit(game_surface, (0, 0))
    # Draw the buttons
    what_time_menu_button_1.draw_button()
    menu_title = menu_font.render("What time is it?", True, (0, 0, 0), )
    game_window.blit(menu_title, (190, 70))
    start_button_text = menu_font.render("START", True, (0, 0, 0), )
    game_window.blit(start_button_text, (425, 340))
    game_window.blit(timer_font.render(f"High Score:  {high_score}", True, (0, 0, 0),), (427, 600))
    draw_return_button()
    # game_window.blit(font.render(f"Current Score:  {score}", True, (0, 0, 0),), (812, 430))
    pygame.display.update()


def draw_game_over_menu():
    global high_score
    global score
    stop_sounds()
    if score > high_score:
        high_score = score
    game_window.blit(game_surface, (0, 0))
    what_time_ending_button_1.draw_button()
    game_window.blit(cross, (335, 540))
    what_time_ending_button_2.draw_button()
    game_window.blit(check, (740, 540))
    # game_window.blit(menu_font.render("Game Over!", True, (0, 0, 0), ), (190, 70))
    game_window.blit(timer_font.render(f"High Score:  {high_score}", True, (0, 0, 0),), (427, 450))
    game_window.blit(end_score_font.render(f"Final Score:  {score}", True, (0, 0, 0),), (290, 180))
    game_window.blit(end_banner, (40, 10))
    pygame.display.update()


question_generator = QuestionGenerator()
question_generator.randomizer()

game_state = "main menu"
click_count = 0
transition_counter = 0
running = True


while running:
    ev = pygame.event.get()
    if game_state == "main menu":
        score = 0
        counter = 60
        draw_main_menu()
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_numbers_button.rect.collidepoint(event.pos):
                    game_state = "number menu"
                elif main_menu_time_button.rect.collidepoint(event.pos):
                    draw_clock_menu()
                    # game_state = "time prep"
                    game_state = "clock menu"
                elif main_menu_what_time_is_it_button.rect.collidepoint(event.pos):
                    game_state = "what time menu"
    if game_state == "clock menu":
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if clock_menu_practice_button.rect.collidepoint(event.pos):
                    game_state = "clock prep"
                if clock_menu_reference_button.rect.collidepoint(event.pos):
                    game_clock.draw_clock()
                    game_state = "clock reference"
                if clock_menu_duel_button.rect.collidepoint(event.pos):
                    scoreboard.duel_player_1 = 30
                    scoreboard.duel_player_2 = 30
                    scoreboard.duel_turn = 1
                    scoreboard.score = 0
                    transition_counter = 0
                    click_count = 0
                    transition_screen()
                    pygame.event.clear(pygame.USEREVENT+1)
                    game_state = "clock transition"
                if clock_menu_duel_button_60.rect.collidepoint(event.pos):
                    scoreboard.duel_player_1 = 60
                    scoreboard.duel_player_2 = 60
                    scoreboard.duel_turn = 1
                    scoreboard.score = 0
                    transition_counter = 0
                    click_count = 0
                    transition_screen()
                    pygame.event.clear(pygame.USEREVENT + 1)
                    game_state = "clock transition"
                if clock_menu_duel_button_90.rect.collidepoint(event.pos):
                    scoreboard.duel_player_1 = 90
                    scoreboard.duel_player_2 = 90
                    scoreboard.duel_turn = 1
                    scoreboard.score = 0
                    transition_counter = 0
                    click_count = 0
                    transition_screen()
                    pygame.event.clear(pygame.USEREVENT + 1)
                    game_state = "clock transition"
                if clock_menu_duel_button_120.rect.collidepoint(event.pos):
                    scoreboard.duel_player_1 = 120
                    scoreboard.duel_player_2 = 120
                    scoreboard.duel_turn = 1
                    scoreboard.score = 0
                    transition_counter = 0
                    click_count = 0
                    transition_screen()
                    pygame.event.clear(pygame.USEREVENT + 1)
                    game_state = "clock transition"
                if clock_menu_duel_button_150.rect.collidepoint(event.pos):
                    scoreboard.duel_player_1 = 150
                    scoreboard.duel_player_2 = 150
                    scoreboard.duel_turn = 1
                    scoreboard.score = 0
                    transition_counter = 0
                    click_count = 0
                    transition_screen()
                    pygame.event.clear(pygame.USEREVENT + 1)
                    game_state = "clock transition"
                if clock_menu_return_button.rect.collidepoint(event.pos):
                    draw_main_menu()
                    game_state = "main menu"
    if game_state == "number menu":
        counter = 0
        player_input = ""
        draw_menu_2()
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.rect.collidepoint(event.pos):
                    game_state = "main menu"
                if menu_button_1.rect.collidepoint(event.pos):
                    question_generator.low_range = 1
                    question_generator.high_range = 20
                    game_state = "number prep"
                if menu_button_2.rect.collidepoint(event.pos):
                    question_generator.low_range = 21
                    question_generator.high_range = 59
                    game_state = "number prep"
                if menu_button_3.rect.collidepoint(event.pos):
                    question_generator.low_range = 1
                    question_generator.high_range = 59
                    game_state = "number prep"
                if main_menu_practice_button.rect.collidepoint(event.pos):
                    draw_number_pad()
                    game_state = "practice"
    if game_state == "practice":
        if len(player_input) == 2:
            if player_input == "01":
                player_input = "1"
            elif player_input == "02":
                player_input = "2"
            elif player_input == "03":
                player_input = "3"
            elif player_input == "04":
                player_input = "4"
            elif player_input == "05":
                player_input = "5"
            elif player_input == "06":
                player_input = "6"
            elif player_input == "07":
                player_input = "7"
            elif player_input == "08":
                player_input = "8"
            elif player_input == "09":
                player_input = "9"
            try:
                pygame.mixer.Sound.play(audio_dictionary[player_input][0])
                pygame.time.delay(610)
            except:
                player_input = "ERROR"
                display_incorrect_calculator_input()
                pygame.display.update()
                pygame.time.delay(500)
            finally:
                try:
                    pygame.mixer.Sound.play(audio_dictionary[player_input][1])
                except:
                    pass
            player_input = ""
            display_calculator_input()
        elif len(player_input) > 2:
            player_input = ""
            display_calculator_input()
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.rect.collidepoint(event.pos):
                    game_state = "number menu"
                for buttons in number_pad_list:
                    if buttons.rect.collidepoint(event.pos):
                        if player_input == "":
                            player_input = buttons.number
                        else:
                            player_input += buttons.number
                        display_calculator_input()
                        pygame.display.update()
                if number_pad_c.rect.collidepoint(event.pos):
                    player_input = ""
                    display_calculator_input()
                    pygame.display.update()
    if game_state == "number prep":
        counter = 0
        draw_number_pad()
        draw_return_button()
        # timer.draw_timer()
        pygame.event.clear()
        question_generator.randomizer()
        question_generator.play_sound()
        game_state = "number game"
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.event.clear(pygame.MOUSEBUTTONDOWN)
    if game_state == "number game":
        if player_input == question_generator.text_answer:
            display_correct_calculator_input()
            pygame.event.clear()
            pygame.time.delay(500)
            scoreboard.increase_score()
            if scoreboard.score >= 15:
                question_generator.stop_sound()
                scoreboard.reset_score()
                game_state = "number menu"
            else:
                reset()
        elif len(player_input) >= 2:
            display_incorrect_calculator_input()
            pygame.time.delay(500)
            reset()
        for event in ev:
            if event.type == pygame.USEREVENT:
                counter += 1
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for buttons in number_pad_list:
                    if buttons.rect.collidepoint(event.pos):
                        if player_input == "":
                            player_input = buttons.number
                        else:
                            player_input += buttons.number
                        display_calculator_input()
                        pygame.display.update()
                if number_pad_repeat.rect.collidepoint(event.pos):
                    question_generator.stop_sound()
                    question_generator.play_sound()
                    pygame.event.clear()
                if number_pad_c.rect.collidepoint(event.pos):
                    player_input = ""
                    # print(player_input)
                    display_calculator_input()
                    pygame.display.update()
                if return_button.rect.collidepoint(event.pos):
                    # scoreboard.reset_score()
                    scoreboard.score = 0
                    game_state = "number menu"
    if game_state == "clock prep":
        game_clock.draw_clock()
        question_generator.clock_randomizer()
        question_generator.play_sound()
        game_state = "clock practice"
    if game_state == "clock reference":
        if click_count == 2:
            question_generator.stop_sound()
            question_generator.answer_hour, question_generator.answer_minute = player_hour_answer, player_minute_answer
            question_generator.stop_sound()
            question_generator.play_sound()
            click_count = 0
            pygame.event.clear()
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if clock_clear_button.rect.collidepoint(event.pos):
                    player_minute_coordinates = ""
                    player_hour_coordinates = ""
                    player_hour_answer = ""
                    player_minute_answer = ""
                    click_count = 0
                    game_clock.draw_clock()
                if return_button.rect.collidepoint(event.pos):
                    draw_clock_menu()
                    scoreboard.reset_score()
                    player_minute_coordinates = ""
                    player_hour_coordinates = ""
                    player_hour_answer = ""
                    player_minute_answer = ""
                    click_count = 0
                    game_state = "clock menu"
                for areas in clock_button_list:
                    if areas.pointtest(event.pos):
                        if click_count == 0:
                            if areas.hour == "no":
                                pass
                            else:
                                player_hour_coordinates = areas.assign_hour_coordinates()
                                player_hour_answer = areas.hour
                                game_clock.draw_clock()
                                draw_hour_hand(player_hour_coordinates)
                                click_count += 1
                        elif click_count == 1:
                            player_minute_coordinates = areas.assign_minute_coordinates()
                            player_minute_answer = areas.minute
                            # print(player_minute_coordinates)
                            game_clock.draw_clock()
                            draw_hour_hand(player_hour_coordinates)
                            draw_minute_hand(player_minute_coordinates)
                            click_count += 1
    if game_state == "clock practice":
        if click_count == 2:
            if player_hour_answer == question_generator.answer_hour and \
                    player_minute_answer == question_generator.answer_minute:
                pygame.mixer.Sound.play(correct_audio)
                pygame.time.delay(int(250 * correct_audio.get_length()))
                scoreboard.increase_score()
                # print(f"score - {scoreboard.score}")
            else:
                pygame.mixer.Sound.play(wrong_audio)
                pygame.time.delay(int(250 * wrong_audio.get_length()))
                # print(f"No Score increase - Score - {scoreboard.score}")
            # pygame.time.delay(500)
            player_minute_coordinates = ""
            player_hour_coordinates = ""
            click_count = 0
            pygame.event.clear()
            question_generator.clock_randomizer()
            question_generator.play_sound()
            game_clock.draw_clock()
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if clock_repeat_button.rect.collidepoint(event.pos):
                    question_generator.stop_sound()
                    question_generator.play_sound()
                if clock_clear_button.rect.collidepoint(event.pos):
                    player_minute_coordinates = ""
                    player_hour_coordinates = ""
                    player_hour_answer = ""
                    player_minute_answer = ""
                    click_count = 0
                    game_clock.draw_clock()
                if return_button.rect.collidepoint(event.pos):
                    draw_clock_menu()
                    scoreboard.reset_score()
                    player_minute_coordinates = ""
                    player_hour_coordinates = ""
                    player_hour_answer = ""
                    player_minute_answer = ""
                    click_count = 0
                    game_state = "clock menu"
                for areas in clock_button_list:
                    if areas.pointtest(event.pos):
                        if click_count == 0:
                            if areas.hour == "no":
                                pass
                            else:
                                player_hour_coordinates = areas.assign_hour_coordinates()
                                player_hour_answer = areas.hour
                                game_clock.draw_clock()
                                draw_hour_hand(player_hour_coordinates)
                                click_count += 1
                        elif click_count == 1:
                            player_minute_coordinates = areas.assign_minute_coordinates()
                            player_minute_answer = areas.minute
                            # print(player_minute_coordinates)
                            game_clock.draw_clock()
                            draw_hour_hand(player_hour_coordinates)
                            draw_minute_hand(player_minute_coordinates)
                            click_count += 1
    if game_state == "clock transition":
        # transition_screen()
        for event in ev:
            if event.type == pygame.USEREVENT+1:
                transition_counter += 1
                if transition_counter == 1:
                    game_clock.draw_clock()
                    question_generator.clock_randomizer()
                    question_generator.play_sound()
                if transition_counter == 10:
                    game_state = "clock duel"
    if game_state == "clock duel":
        if scoreboard.duel_player_1 <= 0 or scoreboard.duel_player_2 <= 0:
            draw_duel_game_over_menu()
            game_state = "game over"
        if click_count == 2:
            if player_hour_answer == question_generator.answer_hour and \
                    player_minute_answer == question_generator.answer_minute:
                pygame.mixer.Sound.play(correct_audio)
                pygame.time.delay(int(250 * correct_audio.get_length()))
                scoreboard.increase_score()
                if scoreboard.score >= 3:
                    if scoreboard.duel_turn == 1:
                        scoreboard.duel_turn = 2
                    elif scoreboard.duel_turn == 2:
                        scoreboard.duel_turn = 1
                    scoreboard.score = 0
                    # transition_screen()
                    # pygame.event.clear(pygame.USEREVENT+1)
                    # pygame.time.set_timer(pygame.USEREVENT + 1, 1500)
                    transition_counter = 0
                    click_count = 0
                    transition_screen()
                    game_state = "clock transition"
                    # print(f"score - {scoreboard.score}")
                else:
                    player_minute_coordinates = ""
                    player_hour_coordinates = ""
                    click_count = 0
                    pygame.event.clear()
                    question_generator.clock_randomizer()
                    question_generator.play_sound()
            else:
                pygame.mixer.Sound.play(wrong_audio)
                pygame.time.delay(int(250 * wrong_audio.get_length()))
                player_minute_coordinates = ""
                player_hour_coordinates = ""
                click_count = 0
                pygame.event.clear()
                question_generator.clock_randomizer()
                question_generator.play_sound()
                # print(f"No Score increase - Score - {scoreboard.score}")
            # pygame.time.delay(500)
            # player_minute_coordinates = ""
            # player_hour_coordinates = ""
            # click_count = 0
            # pygame.event.clear()
            # question_generator.clock_randomizer()
            # question_generator.play_sound()
            # print("made it to the end of the chain")
            # game_clock.draw_clock()
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                scoreboard.duel_adjustment()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if clock_repeat_button.rect.collidepoint(event.pos):
                    question_generator.stop_sound()
                    question_generator.play_sound()
                if clock_clear_button.rect.collidepoint(event.pos):
                    player_minute_coordinates = ""
                    player_hour_coordinates = ""
                    player_hour_answer = ""
                    player_minute_answer = ""
                    click_count = 0
                    game_clock.draw_clock()
                if return_button.rect.collidepoint(event.pos):
                    draw_clock_menu()
                    scoreboard.reset_score()
                    player_minute_coordinates = ""
                    player_hour_coordinates = ""
                    player_hour_answer = ""
                    player_minute_answer = ""
                    click_count = 0
                    game_state = "clock menu"
                for areas in clock_button_list:
                    if areas.pointtest(event.pos):
                        if click_count == 0:
                            if areas.hour == "no":
                                pass
                            else:
                                player_hour_coordinates = areas.assign_hour_coordinates()
                                player_hour_answer = areas.hour
                                game_clock.draw_clock()
                                draw_hour_hand(player_hour_coordinates)
                                click_count += 1
                        elif click_count == 1:
                            player_minute_coordinates = areas.assign_minute_coordinates()
                            player_minute_answer = areas.minute
                            # print(player_minute_coordinates)
                            game_clock.draw_clock()
                            draw_hour_hand(player_hour_coordinates)
                            draw_minute_hand(player_minute_coordinates)
                            click_count += 1
    if game_state == "game over":
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ending_button.rect.collidepoint(event.pos):
                    draw_clock_menu()
                    game_state = "clock menu"
            if event.type == pygame.QUIT:
                running = False
    if game_state == "what time menu":
        draw_what_time_menu()
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if what_time_menu_button_1.rect.collidepoint(event.pos):
                    pygame.event.clear()
                    game_state = "what time load"
                if return_button.rect.collidepoint(event.pos):
                    game_state = "main menu"
    if game_state == "what time load":
        what_time_transition_screen()
        refresh_question()
        pygame.event.clear()
        pygame.mixer.Sound.play(what_time_audio_dictionary[answer])
        # print(answer)
        game_state = "what time play"
    # elif game_state == "test":
    #     for event in ev:
    #         if event.type == pygame.QUIT:
    #             running = False
    if game_state == "what time play":
        pygame.display.update()
        if counter == 0:
            game_state = "what time end"
        for event in ev:
            if event.type == pygame.USEREVENT:
                counter -= 1
                what_time_timer.draw_timer()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if what_time_return_button.rect.collidepoint(event.pos) and not counter == 60:
                    score = 0
                    counter = 60
                    game_state = "what time menu"
                for buttons in button_list:
                    if buttons.rect.collidepoint(event.pos):
                        if buttons.name == answer:
                            score += 1
                            stop_sounds()
                            pygame.mixer.Sound.play(correct_audio)
                        else:
                            score -= 1
                            stop_sounds()
                            pygame.mixer.Sound.play(wrong_audio)
                        pygame.time.delay(300)
                        # print(score)
                        refresh_question()
                        pygame.mixer.Sound.play(what_time_audio_dictionary[answer])
                        pygame.time.delay(100)
                        pygame.event.clear(pygame.MOUSEBUTTONDOWN)
                        # print(answer)
    if game_state == "what time end":
        draw_game_over_menu()
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if what_time_ending_button_1.rect.collidepoint(event.pos):
                    game_state = "main menu"
                if what_time_ending_button_2.rect.collidepoint(event.pos):
                    score = 0
                    counter = 60
                    game_state = "what time load"