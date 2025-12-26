#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import random

RESET = "\033[0m"
BOLD = "\033[1m"

COLORS = [
    "\033[31m", "\033[32m", "\033[33m",
    "\033[34m", "\033[35m", "\033[36m",
    "\033[91m", "\033[92m", "\033[93m",
    "\033[94m", "\033[95m", "\033[96m",
]

STAR_FRAMES = ["✦", "✧", "✺", "✹", "✶"]
LIGHTS = ["●", "○", "◉", "✱", "✳", "◆"]

FIREWORKS = ["*", "✦", "✹", "✧", "❋", "❇"]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def c(txt, color):
    return f"{color}{txt}{RESET}"

def draw_fireworks(width, frame):
    """Draw fireworks randomly in the sky area"""
    lines = []
    sky_height = 6

    for y in range(sky_height):
        row = []
        for x in range(width):
            if random.random() < 0.02 + (frame % 5) * 0.005:
                fw = random.choice(FIREWORKS)
                row.append(c(fw, random.choice(COLORS)))
            else:
                row.append(" ")
        lines.append("".join(row))
    return lines

def draw_tree(height, frame):
    lines = []
    width = height * 2 - 1

    # 🎆 Fireworks sky
    lines.extend(draw_fireworks(width, frame))

    # ⭐ Star
    star = STAR_FRAMES[frame % len(STAR_FRAMES)]
    lines.append(" " * (height - 1) + c(BOLD + star + RESET, random.choice(COLORS)))

    # 🌲 Tree body
    for i in range(height):
        pad = height - i - 1
        row = []
        for _ in range(i * 2 + 1):
            if random.random() < 0.2:
                row.append(c(random.choice(LIGHTS), random.choice(COLORS)))
            else:
                row.append(c("▲", random.choice(["\033[32m", "\033[92m"])))
        lines.append(" " * pad + "".join(row))

    # 🪵 Trunk
    trunk_w = max(3, height // 4 * 2 + 1)
    pad = (width - trunk_w) // 2
    for _ in range(2):
        lines.append(" " * pad + c("█" * trunk_w, "\033[33m"))

    # 🎁 Gifts
    gifts = ["🎁", "🎀", "🧸", "🍬"]
    lines.append(" " * (pad - 1) + " ".join(c(g, random.choice(COLORS)) for g in gifts))

    return "\n".join(lines)

def main():
    height = 14
    fps = 8
    duration = 25

    frames = fps * duration

    try:
        for f in range(frames):
            clear()
            print(draw_tree(height, f))
            print("\n   🎄 메리크리스마스 🎆")
            
            time.sleep(1 / fps)
    except KeyboardInterrupt:
        clear()
        print("🎅 메리 크리스마스! 🎄")

if __name__ == "__main__":
    main()