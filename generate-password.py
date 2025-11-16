import time
import os
import string
import random

# ============================================================
#                    Utility Functions
# ============================================================

def animate(word, repeats=3, delay=0.5):
    """Animated loading text."""
    for i in range(repeats):
        dots = '.' * ((i % 3) + 1)
        print(f"\r{word}{dots}  ", end='', flush=True)
        time.sleep(delay)
    print()

def pause():
    """Pause until user presses Enter."""
    print()
    input("Press Enter to continue...")
    time.sleep(0.5)

def error(msg):
    """Show error message with animation."""
    print()
    print(f"❌ {msg}")
    time.sleep(1.2)
    pause()

def clear_screen():
    """Clear terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

# ============================================================
#                  Core Password Generator
# ============================================================

def generate_password(level):
    """Generate password based on difficulty level."""
    match level:
        case "easy":
            chars = string.ascii_uppercase + string.digits
            length = 8
        case "normal":
            chars = string.ascii_letters + string.digits
            length = 10
        case "hard":
            chars = string.ascii_letters + string.digits + string.punctuation
            length = 12
        case "impossible":
            chars = string.ascii_letters + string.digits + string.punctuation
            length = 16
        case _:
            return None

    return "".join(random.choices(chars, k=length))

# ============================================================
#                         UI Display
# ============================================================

def show_header():
    """Display a visually appealing header."""
    clear_screen()
    print()
    print("╔══════════════════════════════════════════════════╗")
    print("║          🔐 ᴘᴀssᴡᴏʀᴅ ɢᴇɴᴇʀᴀᴛᴏʀ 𝟸.𝟶 🔐            ║")
    print("║   ғᴀsᴛ • sᴇᴄᴜʀᴇ • ᴍᴜʟᴛɪᴘʟᴇ sᴛʀᴇɴɢᴛʜ ᴏᴘᴛɪᴏɴs      ║")
    print("╚══════════════════════════════════════════════════╝")
    print()
    time.sleep(2)

def show_menu():
    """Display password options menu."""
    print("💡 Choose password strength:")
    print("──────────────────────────────")
    print("1️⃣  Easy       (8 chars)       🔹")
    print("2️⃣  Normal     (10 chars)      🔹")
    print("3️⃣  Hard       (12 chars)      🔹")
    print("4️⃣  Impossible (16 chars)      🔹")
    print("5️⃣  Exit                       ❌")
    print("──────────────────────────────")
    print()
    time.sleep(1)

# ============================================================
#                           MAIN
# ============================================================

def main():
    is_running = True

    while is_running:
        show_header()
        show_menu()

        choice = input("Enter your choice (1-5): ").strip()

        # Exit Handler
        if choice == "5":
            for i in range(3):
                print("Exiting" + "." * (i + 1))
                time.sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
            print("\n🔒 Thank you for using Password Generator 2.0!")
            print("Stay safe and secure! ✔\n")
            is_running = False
            break

        # Map choices to levels
        levels = {
            "1": "easy",
            "2": "normal",
            "3": "hard",
            "4": "impossible"
        }

        if choice not in levels:
            animate("Checking", 3, 0.5)
            error("Invalid menu choice!")
            continue

        animate("Generating", 3, 0.4)
        password = generate_password(levels[choice])

        # Beautiful password display
        print()
        print("✨ Password Generated Successfully! ✨")
        print("────────────────────────────────────────")
        print(f"🔑 Your Password: {password}")
        print("────────────────────────────────────────")
        time.sleep(1)

        # Ask to generate again
        again = input("Generate another password? (y/n): ").strip().lower()

        if again in ["n", "no"]:
            animate("Exiting", 3, 0.5)
            print("\n🔒 Thank you for using Password Generator 2.0!")
            print("Stay safe and secure! ✔\n")
            is_running = False
        elif again not in ["y", "yes"]:
            print()
            print("❌ Invalid choice! Exiting program...")
            time.sleep(2)
            is_running = False

# ============================================================
#                     PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    try:
        # Startup Animation
        for i in range(3):
            print(" 🚀 Starting" + "." * (i + 1))
            time.sleep(1)
            clear_screen()

        main()

    except KeyboardInterrupt:
        print("\n\n🔒 Program closed. Stay safe! ✔\n")
