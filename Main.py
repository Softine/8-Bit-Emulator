from tkinter import *
from tkinter import ttk, filedialog
from random import randint
import os
import base64

BUILTIN_PROGS = {"Blitz": b'EhdCTElUWiBCeSBEYXZpZCBXSU5URVKjQWAEYQliDmcE0B7yHnAMMEASIfAKAOAi2fAKAOCOcKMeax/MH4zE3LI/ARJJ3LISOcoHegF7/tyyev86ABJNfv8+ABI5awCMcG0AbgCjG93jPwASwTsAEoFgBeCeEodrAYjQeAKJ4HkDox7YkYHwYAXwFfAHMAASizsBEqujHjEB2JF5ATkgEqtrADEAfP9MABK7oxvd430CPUASuW0AfgESZQDgdwISLaMb3eNgFGECYgujINAb8h5wCDAsEs0S12AKYQ1iBaMH0BXyHnAIMCoS4YBwcP6ABqOH8DPyZWAt8SlhDdAVcAXyKdAVAO6DgoOC++gIiAXivqC4ID6AgICA+ID4/MDA+YHby/sA+oqamfjvKugpKQBvaC5Mj76guLC+AL4iPjSy2NgAw8MA2NgAw8MA2NjAwADAwADAwADAwADb29vbABgYABgYABgYANvb29sAGBgAGBgAGBgAGBjb2wADAwAYGADAwADb2w==',
                "Tetris": b'orQj5iK2cAHQETAlEgZx/9ARYBrQEWAlMQASDsRwRHASHMMDYB5hAyJc9RXQFD8BEjzQFHH/0BQjQBIc56EicuihIoTpoSKW4p4SUGYA9hX2BzYAEjzQFHEBEiqixPQeZgBDAWYEQwJmCEMDZgz2HgDu0BRw/yM0PwEA7tAUcAEjNADu0BRwASM0PwEA7tAUcP8jNADu0BRzAUMEYwAiXCM0PwEA7tAUc/9D/2MDIlwjNADugABnBWgGaQRhH2UQYgcA7kDgAABAwEAAAOBAAEBgQABAQGAAIOAAAMBAQAAA4IAAQEDAAADgIABgQEAAgOAAAEDAgADAYAAAQMCAAMBgAACAwEAAAGDAAIDAQAAAYMAAwMAAAMDAAADAwAAAwMAAAEBAQEAA8AAAQEBAQADwAADQFGY1dv82ABM4AO6itIwQPB58ATwefAE8HnwBI15LCiNykcAA7nEBE1BgG2sA0BE/AHsB0BFwATAlE2IA7mAb0BFwATAlE3SOEI3gfv9gG2sA0OE/ABOQ0OETlNDRewFwATAlE4ZLABOmff9+/z0BE4IjwD8BI8B6ASPAgKBtB4DSQAR1/kUCZQQA7qcA8lWoBPoz8mXwKW0ybgDd5X0F8Snd5X0F8ind5acA8mWitADuagBgGQDuNyM=',
                "Opcode Test": b'Ek7qrKrqzqqqruCgoODAQEDg4CDA4OBgIOCg4CAgYEAgQOCA4ODgICAg4OCg4ODgIOBAoOCg4MCA4OCAwICgQKCgogLatADuogLatBPcaAFpBWoKawFlKmYrohbYtKI+2bSiAjYrogbatGsGohrYtKI+2bSiBkUqogLatGsLoh7YtKI+2bSiBlVgogLatGsQoibYtKI+2bSiBnb/RiqiAtq0axWiLti0oj7ZtKIGlWCiAtq0axqiMti0oj7ZtCJCaBdpG2ogawGiCti0ojbZtKIC2rRrBqIq2LSiCtm0ogaHUEcqogLatGsLoirYtKIO2bSiBmcqh7FHK6IC2rRrEKIq2LSiEtm0ogZmeGcfh2JHGKIC2rRrFaIq2LSiFtm0ogZmeGcfh2NHZ6IC2rRrGqIq2LSiGtm0ogZmjGeMh2RHGKIC2rRoLGkwajRrAaIq2LSiHtm0ogZmjGd4h2VH7KIC2rRrBqIq2LSiItm0ogZm4IZuRsCiAtq0awuiKti0ojbZtKIGZg+GZkYHogLatGsQojrYtKIe2bSj6GAAYTDxVaPp8GWiBkAwogLatGsVojrYtKIW2bSj6GaJ9jPyZaICMAGiBjEDogYyB6IG2rRrGqIO2LSiPtm0EkgT3A==',
                "Worm": b'ElxXb3JtIHYuNCwgYnk6IFJCLCBDaGlwLTggdmVyc2lvbiBieTogTWFydGlqbiBXZW50aW5nIC8gUmV2aXZhbCBTdHVkaW9zAFJCOTIAAAAfAAATfAAABg4BAAQA4KJN/mWjpfBV/B5xATEAEmSjj9qzo47UIdQxdAI0OhJ0o5xjANMh1CFyATIfEoKiSPBlogLwM6IC9TMjIiN0o5vXYXYCNiESnGMG8xWjpfge8GWEAICgo6X4HvBVpKX4HvBlgQCAsKSl+B7wVaOSNADUE6OG+R7xZaOV2rKKBIsUo4/asz8AEzzAD0AAI3B4AZjgaABjBvMVZv9hBuGhZgBhAuGhZgJhBOGhZgRhCOGhZgY2/4lg8wczABL2EqYjIqIC9TNjAGQ8ogLyZfAp1DVzBvEp1DVzBvIp1DUA7iOAo4/as9qzPwATUmQC9Bh1ASMcEuxkCvQY2rOKBYsVo5XasqJI8GWiSIBVgFBPAPBVE25+AQDuo5fMP80f3NRPAADuo5fc1BN2BAAA/PwAAATA4ODg4KDgAEAwWHgw8ICAgICAgICAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=',
                "Pong": b'IvxrDGw/bQyi6tq23NZuACLUZgNoAmBg8BXwBzAAEhrHF3cIaf+i8NZxourattzWYAHgoXv+YATgoXsCYB+LAtq2YAzgoX3+YA3goX0CYB+NAtzWovDWcYaEh5RgP4YCYR+HEkYAEnhGPxKCRx9p/0cAaQHWcRIqaAJjAYBwgLUSimj+YwqAcIDVPwESomECgBU/ARK6gBU/ARLIgBU/ARLCYCDwGCLUjjQi1GY+MwFmA2j+MwFoAhIWef9J/mn/Esh5AUkCaQFgBPAYdgFGQHb+Emyi8v4z8mXxKWQUZQLUVXQV8inUVQDugICAgICAgAAAAAAAwMDAAP8AayBsAKL228R8BDwgEwJqAGsAbB+i+tqx2sF6CDpAExKi9moAayDboQDu',
                "UFO": b'os1pOGoI2aOi0GsAbAPbw6LWZB1lH9RRZwBoDyKiIqxIABIiZB5lHKLT1FNuAGaAbQTtoWb/bQXtoWYAbQbtoWYBNoAi2KLQ28PNAYvU28M/ABKSos3Zo80BPQBt/3n+2aM/ABKMTgASLqLT1FNFABKGdf+EZNRTPwESRm0IjVJNCBKMEpIirHj/Eh4ioncFEpYioncPIqJtA/0YotPUUxKGovj3M2MAIrYA7qL4+DNjMiK2AO5tG/Jl8CnT1XMF8SnT1XMF8inT1QDuAXz+fGDwYEDgoPjUbgFtEP0YAO4='}
OPTIONS = {"paused": False, 
           "speed": 16, 
           "loaded": False,
           "prog_name": "",
           "prog_data": None}

#######################################################################
# Display
#
# Implements the 64 by 32 CHIP-8 display
#
#######################################################################

class Display(Canvas):
    WIDTH = 64
    HEIGHT = 32
    COLOURMAP = ("black", "yellow")

    def __init__(self, parent, scale=1):
        super().__init__(parent)

        self.the_scale = scale
        self["width"] = self.WIDTH*self.the_scale
        self["height"] = self.HEIGHT*self.the_scale

        self.pixels = [randint(0,1) for _ in range(64*32)]   
        self.screen_pixels = []

        self.pixels = [0]*(self.WIDTH*self.HEIGHT)
        self.pixel_ids = []
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                id = self.create_rectangle((x*self.the_scale, y*self.the_scale, 
                                      (x+1)*self.the_scale, (y+1)*self.the_scale), 
                                      fill=self.COLOURMAP[0], width=0)
                self.pixel_ids.append(id)        
        
    def yx_to_loc(self, y, x):
        return (y%self.HEIGHT)*self.WIDTH + (x%self.WIDTH)

    def get_pixel(self, y, x):
        return self.pixels[self.yx_to_loc(y, x)]
    
    def set_pixel(self, y, x, val):
        self.pixels[self.yx_to_loc(y,x)] = val
        self.itemconfigure(self.pixel_ids[self.yx_to_loc(y,x)], fill=self.COLOURMAP[val])

    def flip_pixel(self, y, x):
        old_value = self.get_pixel(y,x)
        self.set_pixel(y, x, 1-old_value)
        return old_value

    def clear(self):
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                self.set_pixel(y, x, 0)

#######################################################################
# Keypad
#
# Implements the hex keypad
#
# We use the keys 1234 to map to the keypad keys 123C
#                 QWER                           456D
#                 ASDF                           789E
#                 ZXCV                           A0BF
#######################################################################

class Keypad:
    MAPPING = {"1": 0x1, "2": 0x2, "3": 0x3, "4": 0xC,
               "Q": 0x4, "W": 0x5, "E": 0x6, "R": 0xD,
               "A": 0x7, "S": 0x8, "D": 0x9, "F": 0xE,
               "Z": 0xA, "X": 0x0, "C": 0xB, "V": 0xF}

    def __init__(self, window):
        self.pressed = set()

        window.bind_all("<KeyPress>", self.key_down)
        window.bind_all("<KeyRelease>", self.key_up)

    def key_down(self, event):
        key = event.keysym.upper()
        if key in self.MAPPING:
            self.pressed.add(self.MAPPING[key])

    def key_up(self, event):
        key = event.keysym.upper()
        if key in self.MAPPING:
            self.pressed.discard(self.MAPPING[key])        

    def is_pressed(self, key):
        return key in self.pressed

    def something_pressed(self):
        return len(self.pressed) > 0

    def value(self):
        return list(self.pressed)[0] if self.pressed else None

#######################################################################
# Chip8CPU
#
# Implements the CPU of the Chip8 system
#
#######################################################################

class Chip8CPU:
    FONT_DATA = "F999F"+"26227"+"F1F8F"+"F1F1F"+\
                "99F11"+"F8F1F"+"F8F9F"+"F1244"+\
                "F9F9F"+"F9F1F"+"F9F1F"+"E9E9E"+\
                "F888F"+"E999E"+"F8F8F"+"F8F88"
    FONT_START = 0x50
    PROG_START = 0x200

    def __init__(self, display, keypad):
        self.display = display
        self.keypad = keypad
        self.paused = True
        self.hard_reset()

    # Hard reset - wipe all memory and registers
    def hard_reset(self):
        self.display.clear()
        self.paused = True
        self.memory = [0]*4096
        # Font data is stored starting at 0x50      
        for (i, val) in enumerate(self.FONT_DATA):
            self.memory[self.FONT_START+i] = int(val,16)*16  
        self.soft_reset()       

    # Soft reset - keep memory but reset registers
    def soft_reset(self):
        self.reg = [0]*16          # 16 registers V0 to VF
        self.stack = []            # call stack
        self.I = 0                 # index register
        self.PC = self.PROG_START  # traditional start point for Chip8 code
        self.delay_timer = 0       # programmable delay timer
        self.sound_timer = 0       # programmable delay timer

    def load(self, data):
        self.hard_reset()
        # Code is stored starting at location 0x200
        for (i, val) in enumerate(data):
            self.memory[0x200 + i] = val
        self.paused = False

     ######################################################
    # Routines which execute the various opcodes

    def execute_routine(self, NNN):
        # Only two valid routines to execute:
        # 0 0E0 -> Clear screen
        # 0 0EE -> Return from subroutine

        if   NNN == 0x0E0:
            self.display.clear()
        elif NNN == 0x0EE:
            self.PC = self.stack.pop()
        else:
            print(f"Invalid opcode: 'execute' 0:{NNN:0x}")

    def execute_jump(self, NNN):
        # Jump to location NNN
        self.PC = NNN

    def execute_call(self, NNN):
        # Call subroutine at location NNN
        self.stack.append(self.PC)
        self.PC = NNN

    def execute_skip_if_equal_to(self, NNN):
        X = NNN >> 8
        NN = NNN & 0xFF
        # Skip the next instruction if VX is equal to NN
        if self.reg[X] == NN:
            self.PC += 2

    def execute_skip_if_unequal_to(self, NNN):
        X = (NNN >> 8) & 0xF
        NN = NNN & 0xFF
        # Skip the next instruction if VX is not equal to NN
        if self.reg[X] != NN:
            self.PC += 2

    def execute_skip_if_equal_regs(self, NNN):
        X = (NNN >> 8) & 0xF
        Y = (NNN >> 4) & 0xF
        # Skip the next instruction if VX is equal to VY
        if self.reg[X] == self.reg[Y]:
            self.PC += 2

    def execute_load_value(self, NNN):
        X = (NNN >> 8) & 0xF
        NN = NNN & 0xFF
        # Load value NN into register VX
        self.reg[X] = NN
    
    def execute_add_value(self, NNN):
        X = (NNN >> 8) & 0xF
        NN = NNN & 0xFF
        # Increment register VX by NN
        self.reg[X] = (self.reg[X] + NN) % 256

    def execute_arithmetic(self, NNN):
        X = (NNN >> 8) & 0xF
        Y = (NNN >> 4) & 0xF
        N =  NNN       & 0xF
        # Perform an arithmetic operation, based on N:
        # N = 0: VX = VY
        #     1: VX = VX  or VY
        #     2: VX = VX and VY
        #     3: VX = VX xor VY
        #     4: VX = VX + VY    (VF is carry flag)
        #     5: VX = VX - VY    (VF is NOT borrow)
        #     6: VX = VX >> 1    (VF is LSB of VX before shift)
        #     7: VX = VY - VX    (VF is NOT borrow)
        #     E: VX = VX << 1    (VF is MSB of VX before shift)
        if N == 0:
            self.reg[X] = self.reg[Y]
        elif N == 1:
            self.reg[X] |= self.reg[Y]
        elif N == 2:
            self.reg[X] &= self.reg[Y]
        elif N == 3:
            self.reg[X] ^= self.reg[Y]
        elif N == 4:
            result = self.reg[X] + self.reg[Y]
            if result > 0xFF: self.reg[0xF] = 1
            self.reg[X] = result % 256
        elif N == 5:
            result = self.reg[X] - self.reg[Y]
            self.reg[0xF] = 0 if result < 0 else 1
            self.reg[X] = result % 256
        elif N == 6:
            reg_to_shift = X#Y                                # C8: shift Y into X. SCHIP: always shift X
            self.reg[0xF] = self.reg[reg_to_shift] & 0x01
            self.reg[X] = self.reg[reg_to_shift] >> 1
        elif N == 7:
            self.reg[0xF] = (self.reg[Y] - self.reg[X] >= 0)
            self.reg[X] = (self.reg[Y] - self.reg[X])
        elif N == 0xE:
            reg_to_shift = X#Y                                # C8: shift Y into X. SCHIP: always shift X
            self.reg[0xF] = (self.reg[reg_to_shift] & 0x80) >> 7
            self.reg[X] = (self.reg[reg_to_shift] << 1) % 256
        else:
            print(f"Invalid opcode: 'arithmetic' 8:{NNN:0x}")

    def execute_skip_if_unequal_regs(self, NNN):
        X = (NNN >> 8) & 0xF
        Y = (NNN >> 4) & 0xF
        # Skip next instruction if specified registers are unequal
        if self.reg[X] != self.reg[Y]:
            self.PC += 2

    def execute_load_index(self, NNN):
        # Loads the index register with the given value
        self.I = NNN

    def execute_jump_relative(self, NNN):
        # Jump to location V0 + NNN (this has an S-CHIP quirk)
        self.PC = self.reg[0] + NNN
    
    def execute_load_random(self, NNN):
        X = (NNN >> 8) & 0xF
        NN = NNN & 0xFF
        # Load VX with (random byte) and NN
        self.reg[X] = randint(0,255) & NN        

    def execute_draw(self, NNN):
        X = (NNN >> 8) & 0xF
        Y = (NNN >> 4) & 0xF
        N =  NNN       & 0xF
        # Display an N-byte sprite at location I to screen position (VX, VY)
        # Set VF if there has been a collision

        # The screen location wraps but the sprite doesn't
        xbase = self.reg[X] % self.display.WIDTH
        ybase = self.reg[Y] % self.display.HEIGHT

        self.reg[0xF] = 0
        for dy in range(N):
            if ybase + dy >= self.display.HEIGHT: break
            for dx in range(8):
                if xbase + dx >= self.display.WIDTH: break                

                sprite_pixel = self.memory[self.I + dy] & (0x80 >> dx)
                if sprite_pixel:
                    collision = self.display.flip_pixel(ybase+dy, xbase+dx)
                    if collision: self.reg[0xF] = 1

    def execute_skip_if_key(self, NNN):
        X = (NNN >> 8) & 0xF
        NN = NNN & 0xFF
        # Only two valid opcodes in this range:
        # NN = 0x9E: skip if key in VX has been pressed
        #      0xA1: skip if key in Vx has NOT been pressed

        if NN == 0x9E:
            if self.keypad.is_pressed(self.reg[X]):
                self.PC += 2
        elif NN == 0xA1:
            if not self.keypad.is_pressed(self.reg[X]):
                self.PC += 2
        else:
             print(f"Invalid opcode: 'key handing' E:{NNN:0x}")
             
             
    def execute_miscellaneous_loads(self, NNN):
        X = (NNN >> 8) & 0xF
        NN = NNN & 0xFF
        # A rag-bag of miscellaneous load instructions
        # NN = 0x07: VX = delay timer value
        #      0x0A: VX = wait for key press then store
        #      0x15: delay timer = VX
        #      0x18: sound timer = VX
        #      0x1E: I = I + VX (out of place!)
        #      0x29: I = location of sprite for digit VX
        #      0x33: store BCD rep of VX in I (hundreds), I+1 (tens), I+2 (units)
        #      0x55: store registers V0-VX to memory starting at I
        #      0x65: read registers V0-VX from memory starting at I
        if NN == 0x07:
            self.reg[X] = self.delay_timer
        elif NN == 0x0A:
            if not self.keypad.something_pressed():
                self.PC -= 2
            else:
                self.reg[X] = self.keypad.value()
        elif NN == 0x15:
            self.delay_timer = self.reg[X]
        elif NN == 0x18:
            self.sound_timer = self.reg[X]
        elif NN == 0x1E:
            self.I = (self.I + self.reg[X]) % 0x1000
        elif NN == 0x29:
            self.I = self.FONT_START + 5*self.reg[X]
        elif NN == 0x33:
            value = self.reg[X]
            self.memory[self.I+2], value = value%10, value//10
            self.memory[self.I+1], value = value%10, value//10
            self.memory[self.I  ], value = value%10, value//10
        elif NN == 0x55:
            for i in range(X+1):
                self.memory[self.I+i] = self.reg[i]
            #self.I += X+1                                           # C8: increment I. SCHIP: leave I unchanged
        elif NN == 0x65:
            for i in range(X+1):
                self.reg[i] = self.memory[self.I+i]
            #self.I += X+1                                           # C8: increment I. SCHIP: leave I unchanged
        else:
            print(f"Invalid opcode: 'memory loads' F:{NNN:0x}")

    ##########################################
    # Perform one fetch-decode-execute step

    def step(self):
        if self.paused: return
        # Fetch and decode next opcode
        opcode = self.memory[self.PC]*256 + self.memory[self.PC+1]
        self.PC += 2

        A = opcode >> 12
        NNN = opcode & 0x0FFF

        # Now execute the appropriate instruction
        opcode_table = {0: self.execute_routine, 
                        1: self.execute_jump,
                        2: self.execute_call,
                        3: self.execute_skip_if_equal_to,
                        4: self.execute_skip_if_unequal_to,
                        5: self.execute_skip_if_equal_regs,
                        6: self.execute_load_value,
                        7: self.execute_add_value,
                        8: self.execute_arithmetic,
                        9: self.execute_skip_if_unequal_regs,
                        0xA: self.execute_load_index,
                        0xB: self.execute_jump_relative,
                        0xC: self.execute_load_random,
                        0xD: self.execute_draw,
                        0xE: self.execute_skip_if_key,
                        0xF: self.execute_miscellaneous_loads}
        opcode_table[A](NNN)

    # Every 60th of a second the delay and sound timers are supposed to tick down
    def timer_tick(self):
        if self.delay_timer > 0: self.delay_timer -= 1
        if self.sound_timer > 0: self.sound_timer -= 1

#######################################################################
# Setup the menu
def setup_menu(window):
    def command_file_open():
        filename = filedialog.askopenfilename(filetypes=[("Chip 8", "*.ch8"),])
        if filename:
            data = open(filename, "rb").read()
            OPTIONS["prog_name"] = os.path.basename(filename).split(".")[0]
            OPTIONS["prog_data"] = data
            OPTIONS["loaded"] = True
            window.event_generate("<<ComputerRestart>>")

    def command_file_close():
        OPTIONS["prog_name"] = ""
        OPTIONS["prog_data"] = ""
        OPTIONS["loaded"] = False
        window.event_generate("<<ComputerShutdown>>")

    def command_file_load_builtin(name):
        OPTIONS["prog_name"] = "Builtin: " + name
        OPTIONS["prog_data"] = base64.decodebytes(BUILTIN_PROGS[name])
        OPTIONS["loaded"] = True
        window.event_generate("<<ComputerRestart>>")

    def command_options_pause():
        OPTIONS["paused"] = not OPTIONS["paused"]

    def command_options_speedup():
        window.event_generate("<<ComputerSpeedUp>>")

    def command_options_slowdown():
        window.event_generate("<<ComputerSlowDown>>")

    def command_options_reset():
        window.event_generate("<<ComputerRestart>>")

    window.option_add("*tearOff", FALSE)  # Needed to remove legacy tear-off menus
    menubar = Menu(window)
    window["menu"] = menubar
    menu_file = Menu(menubar)
    menu_options = Menu(menubar)
    menubar.add_cascade(menu=menu_file, label="File")
    menubar.add_cascade(menu=menu_options, label="Options")

    menu_file.add_command(label="Open...", command=command_file_open)
    menu_file.add_command(label="Close", command=command_file_close)
    menu_file.add_separator()
    menu_recent = Menu(menu_file)
    menu_file.add_cascade(menu=menu_recent, label="Built In")

    menu_recent.add_command(label="Blitz", command=lambda: command_file_load_builtin("Blitz"))
    menu_recent.add_command(label="Opcode Test", command=lambda: command_file_load_builtin("Opcode Test"))
    menu_recent.add_command(label="Pong", command=lambda: command_file_load_builtin("Pong"))
    menu_recent.add_command(label="Tetris", command=lambda: command_file_load_builtin("Tetris"))
    menu_recent.add_command(label="UFO", command=lambda: command_file_load_builtin("UFO"))
    menu_recent.add_command(label="Worm", command=lambda: command_file_load_builtin("Worm"))

    menu_file.add_separator()
    menu_file.add_command(label="Exit", command=root.destroy)

    paused_var = IntVar()
    menu_options.add_checkbutton(label="Pause", variable=paused_var, command=command_options_pause)
    check = StringVar()
    menu_options.add_command(label="Speed up", command=command_options_speedup)
    menu_options.add_command(label="Slow down", command=command_options_slowdown)
    menu_options.add_command(label="Reset", command=command_options_reset)

    return menubar
#######################################################################

# Setup the status bar
def setup_status(window):
    bar = Frame(window, relief="sunken", bd=1)

    loaded_prog = StringVar()
    speed = StringVar()
    loaded_prog.set("No program loaded")
    speed.set(OPTIONS["speed"])

    Label(bar, textvariable = loaded_prog).grid(column=0, row=0, sticky=W)
    Label(bar, text="Speed: ", anchor=E).grid(column=1, row=0, sticky=E)
    Label(bar, textvariable = speed, anchor=E).grid(column=2, row=0, sticky=E)
    return bar, {"prog": loaded_prog, "speed": speed}

#######################################################################

if __name__=="__main__":
    # Setup the UI and the Chip8 system
    root = Tk()
    menubar = setup_menu(root)
    root.title("CHIP-8 Emulator")
    root.resizable(width=False, height=False)
    statusbar, statusdata = setup_status(root); statusbar.grid(column=0, row=1, sticky=(W, E))
    display = Display(root, scale=14); display.grid(column=0, row=0, sticky=(N, W, E, S))
    keypad = Keypad(root)
    cpu = Chip8CPU(display, keypad)

    # Create all the event bindings for computer restart, speed up/down, etc.
    def computer_restart(*args):
        cpu.load(OPTIONS["prog_data"]) 
        statusdata["prog"].set(OPTIONS["prog_name"])       
    root.bind("<<ComputerRestart>>", computer_restart)
    root.bind("<Key-Escape>", computer_restart)

    def computer_shutdown(*args):
        cpu.hard_reset()
        statusdata["prog"].set("No program loaded")
    root.bind("<<ComputerShutdown>>", computer_shutdown)        

    def computer_speedup(*args):
        OPTIONS["speed"] += 1
        statusdata["speed"].set(OPTIONS["speed"])
    root.bind("<<ComputerSpeedUp>>", computer_speedup)
    root.bind("<Key-equal>", computer_speedup)

    def computer_slowdown(*args):
        if OPTIONS["speed"] > 1:
            OPTIONS["speed"] -= 1
            statusdata["speed"].set(OPTIONS["speed"])
    root.bind("<<ComputerSlowDown>>", computer_slowdown)
    root.bind("<Key-minus>", computer_slowdown)

    def computer_reset(*args):
        cpu.soft_reset()
    root.bind("<<ComputerReset>>", computer_reset)
    root.bind("<Key-BackSpace>", computer_reset)

    # Main computer-run loop, called 60 times per second
    def run_computer():
        if not OPTIONS["paused"]:
            for _ in range(OPTIONS["speed"]):
                cpu.step()
            cpu.timer_tick()

        root.after(1000//60, run_computer)
    run_computer()

    root.mainloop()
#######################################################################
