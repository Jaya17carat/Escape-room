"""
HORROR ESCAPE ROOM GAME
A text-based escape room adventure with 4 mysterious rooms.
Solve puzzles to escape before time runs out!
"""

import time
import random

class EscapeRoomGame:
    def __init__(self):
        self.player_name = ""
        self.current_room = 1
        self.inventory = []
        self.start_time = 0
        self.time_limit = 600  # 10 minutes in seconds
        self.rooms_completed = 0
        self.game_won = False
        
    def display_welcome(self):
        """Display welcome message and get player name"""
        print("\n" + "="*60)
        print("           🏚️  HORROR ESCAPE ROOM GAME  🏚️")
        print("="*60)
        print("\n🔓 STORYLINE 🔓")
        print("-" * 60)
        print("You wake up in an abandoned mansion with no memory.")
        print("The doors are locked. Strange symbols cover the walls.")
        print("You have 10 minutes to escape before... something happens.")
        print("Solve puzzles. Find clues. SURVIVE.\n")
        print("-" * 60)
        
        self.player_name = input("Enter your name, survivor: ").strip()
        if not self.player_name:
            self.player_name = "Mysterious Stranger"
        
        print(f"\nGood luck, {self.player_name}...\n")
        time.sleep(2)
    
    def room_1_dusty_library(self):
        """Room 1: Dusty Library with cryptic books"""
        print("\n" + "="*60)
        print("🏚️ ROOM 1: THE DUSTY LIBRARY 📚")
        print("="*60)
        print("\nYou enter a cold, dusty library. Candles flicker weakly.")
        print("Shelves of old books surround you. Something feels... watched.")
        print("\nYou see:")
        print("  1) A locked DESK with a red book on top")
        print("  2) Ancient BOOKSHELVES with strange symbols")
        print("  3) A PAINTING on the wall (crooked)")
        
        while True:
            choice = input("\nWhat do you examine? (1/2/3): ").strip()
            
            if choice == "1":
                print("\n📖 You pick up the RED BOOK...")
                print("Its title reads: 'THE FORBIDDEN KNOWLEDGE'")
                print("Inside, you find a CRYPTIC RIDDLE:\n")
                print("   'I have keys but no locks.")
                print("    I have space but no room.")
                print("    What am I?'")
                print("\nWhat is the answer? (Type your answer)")
                answer = input("> ").strip().lower()
                
                if answer == "piano" or answer == "keyboard":
                    print("\n✅ CORRECT! A hidden compartment opens in the desk!")
                    print("You find a GOLDEN KEY inside. It feels ancient.")
                    self.inventory.append("Golden Key")
                    print(f"\n📦 Inventory: {', '.join(self.inventory)}")
                    break
                else:
                    print("\n❌ Wrong answer. The book slams shut. Try again.")
                    
            elif choice == "2":
                print("\n🔮 You study the BOOKSHELVES carefully...")
                print("The symbols spell out: S-O-L-U-T-I-O-N")
                print("Wait... they're pointing to specific books!")
                print("You pull them in order and hear a CLICK.")
                print("A secret drawer slides open...")
                print("Inside: A SILVER COMPASS with strange engravings.")
                self.inventory.append("Silver Compass")
                print(f"\n📦 Inventory: {', '.join(self.inventory)}")
                break
                
            elif choice == "3":
                print("\n🖼️ You straighten the PAINTING...")
                print("Behind it: A HIDDEN SAFE with a CODE LOCK.")
                print("You need to find the 3-digit code (000-999).")
                code = "1701"  # Birth year of the mansion (fictional)
                user_code = input("Enter a 3-digit code: ").strip()
                if user_code == "170":
                    print("\n✅ CORRECT! The safe opens with a CLICK.")
                    print("Inside: A LEATHER DIARY and a RUSTY CHAIN.")
                    self.inventory.extend(["Leather Diary", "Rusty Chain"])
                    print(f"\n📦 Inventory: {', '.join(self.inventory)}")
                    break
                else:
                    print(f"\n❌ Code rejected. Try again. (Hint: Think about age...)")
            else:
                print("\n❓ That's not an option. Please choose 1, 2, or 3.")
    
    def room_2_dark_basement(self):
        """Room 2: Dark Basement with machinery"""
        print("\n" + "="*60)
        print("🏚️ ROOM 2: THE DARK BASEMENT ⚙️")
        print("="*60)
        print("\nYou descend into the basement. Water drips from the ceiling.")
        print("The air is cold and damp. Rusted machinery surrounds you.")
        print(f"\nInventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")
        print("\nYou see:")
        print("  1) A LARGE MACHINE with colored wires")
        print("  2) Stacks of OLD DOCUMENTS")
        print("  3) A METAL BOX sealed with a chain")
        
        while True:
            choice = input("\nWhat do you investigate? (1/2/3): ").strip()
            
            if choice == "1":
                print("\n⚙️ You examine the MACHINE...")
                print("It has 4 colored wires: RED, BLUE, GREEN, YELLOW")
                print("There's a note: 'Connect in order of: Sky, Grass, Fire, Ocean'")
                user_order = input("Enter order (e.g., blue,green,red,yellow): ").lower().strip()
                correct = "blue,green,red,yellow"
                if user_order == correct:
                    print("\n✅ CORRECT CONNECTION!")
                    print("The machine hums to life. A METAL PANEL slides open.")
                    print("Inside: A STRANGE CRYSTAL and COPPER WIRE.")
                    self.inventory.extend(["Strange Crystal", "Copper Wire"])
                    print(f"\n📦 Inventory: {', '.join(self.inventory)}")
                    break
                else:
                    print("\n❌ Wrong sequence. The machine sparks dangerously!")
                    
            elif choice == "2":
                print("\n📄 You read the OLD DOCUMENTS...")
                print("They're logs from 1845. They mention:")
                print("  - 'The ritual requires 4 items of power'")
                print("  - 'Hidden beneath the library for eternity'")
                print("  - 'Only the worthy shall escape'")
                print("\nYou also find a MAP showing the mansion's layout!")
                self.inventory.append("Mansion Map")
                print(f"\n📦 Inventory: {', '.join(self.inventory)}")
                break
                
            elif choice == "3":
                if "Rusty Chain" in self.inventory:
                    print("\n🔗 You use the RUSTY CHAIN to break the seal!")
                    print("The METAL BOX opens, revealing...")
                    print("A MUSIC BOX! It plays a haunting melody.")
                    print("Inside the lining: An OLD PHOTOGRAPH and a KEY.")
                    self.inventory.extend(["Music Box", "Old Photograph"])
                    print(f"\n📦 Inventory: {', '.join(self.inventory)}")
                    break
                else:
                    print("\n❌ The chain won't budge without something to break it.")
                    print("   (You might find what you need elsewhere...)")
            else:
                print("\n❓ That's not an option. Please choose 1, 2, or 3.")
    
    def room_3_haunted_bedroom(self):
        """Room 3: Haunted Bedroom with mirror puzzle"""
        print("\n" + "="*60)
        print("🏚️ ROOM 3: THE HAUNTED BEDROOM 👻")
        print("="*60)
        print("\nYou climb to the bedroom. Dust particles dance in fading light.")
        print("An old mirror hangs on the wall. The room feels... occupied.")
        print(f"\nInventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")
        print("\nYou see:")
        print("  1) A CRACKED MIRROR with strange reflections")
        print("  2) A MUSIC BOX on the dresser")
        print("  3) A WARDROBE with heavy doors")
        
        while True:
            choice = input("\nWhat do you examine? (1/2/3): ").strip()
            
            if choice == "1":
                print("\n🪞 You look into the CRACKED MIRROR...")
                print("Wait... your reflection is moving DIFFERENTLY!")
                print("It points behind you. You turn around but see nothing.")
                print("The mirror shows a HIDDEN DOOR in the wall!")
                print("You press where the mirror indicated...")
                print("A section of the wall CLICKS and slides open!")
                print("Inside: A GLOWING AMULET and ANCIENT SCROLL.")
                self.inventory.extend(["Glowing Amulet", "Ancient Scroll"])
                print(f"\n📦 Inventory: {', '.join(self.inventory)}")
                break
                
            elif choice == "2":
                if "Music Box" in self.inventory:
                    print("\n🎵 You play the MUSIC BOX...")
                    print("The melody fills the room. A hidden panel OPENS!")
                    print("Inside: A SILVER DAGGER and INCENSE.")
                    self.inventory.extend(["Silver Dagger", "Incense"])
                    print(f"\n📦 Inventory: {', '.join(self.inventory)}")
                    break
                else:
                    print("\n🎵 There's already a music box here, but it won't open.")
                    
            elif choice == "3":
                print("\n👔 You open the WARDROBE...")
                print("It's filled with old clothes from centuries past.")
                print("As you search, something falls out...")
                print("A JOURNAL! You read the final entry:")
                print("\n   'To escape this cursed place, gather the 4 items'")
                print("   'of power. The crystal, the key, the compass, the amulet.'")
                print("   'Place them in the ritual circle. Only then are you free.'")
                self.inventory.append("Final Journal Entry")
                print(f"\n📦 Inventory: {', '.join(self.inventory)}")
                break
            else:
                print("\n❓ That's not an option. Please choose 1, 2, or 3.")
    
    def room_4_ritual_chamber(self):
        """Room 4: Final chamber - use collected items"""
        print("\n" + "="*60)
        print("🏚️ ROOM 4: THE RITUAL CHAMBER ✨")
        print("="*60)
        print("\nYou descend into the deepest part of the mansion.")
        print("Candles burn in a perfect circle. Ancient symbols cover the floor.")
        print("This is it. The way out.")
        print(f"\nInventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")
        
        required_items = ["Strange Crystal", "Golden Key", "Silver Compass", "Glowing Amulet"]
        found_items = [item for item in required_items if item in self.inventory]
        
        print(f"\n📊 Items Required: {len(required_items)}")
        print(f"📊 Items Found: {len(found_items)}")
        
        if len(found_items) >= 3:
            print("\n🔮 You place the items in the ritual circle...")
            print("The symbols begin to GLOW with an eerie light!")
            time.sleep(1)
            print("The ground trembles...")
            time.sleep(1)
            print("A door materializes before you!")
            print("\n✨ THE SEAL BREAKS! YOU ARE FREE! ✨")
            self.game_won = True
        else:
            print("\n❌ You don't have enough items!")
            print(f"   You have {len(found_items)}, but need {len(required_items)}.")
            print("   You must have missed something...")
            print("   (Go back and search more thoroughly!)")
    
    def calculate_stats(self):
        """Calculate final game statistics"""
        elapsed_time = time.time() - self.start_time
        minutes = int(elapsed_time) // 60
        seconds = int(elapsed_time) % 60
        time_remaining = max(0, self.time_limit - int(elapsed_time))
        
        return {
            "elapsed": f"{minutes}m {seconds}s",
            "remaining": f"{time_remaining}s",
            "items_found": len(self.inventory)
        }
    
    def display_end_screen(self):
        """Display end game screen"""
        stats = self.calculate_stats()
        
        print("\n" + "="*60)
        if self.game_won:
            print("           🎉 YOU ESCAPED! 🎉")
            print("="*60)
            print(f"\nSurvivor: {self.player_name}")
            print(f"Time Used: {stats['elapsed']}")
            print(f"Time Remaining: {stats['remaining']}")
            print(f"Items Collected: {stats['items_found']}")
            print("\nYou step out into the moonlight, free at last...")
            print("But questions remain. What WAS that place?")
            print("And will it ever let you forget?")
        else:
            print("           💀 GAME OVER 💀")
            print("="*60)
            print(f"\nSurvivor: {self.player_name}")
            print(f"Time Used: {stats['elapsed']}")
            print(f"Items Found: {stats['items_found']}")
            print("\nYou didn't find enough clues to escape.")
            print("The mansion claims another victim...")
        
        print("\n" + "="*60)
        print("Thank you for playing HORROR ESCAPE ROOM!")
        print("="*60 + "\n")
    
    def play(self):
        """Main game flow"""
        self.display_welcome()
        self.start_time = time.time()
        
        print("Starting your escape in 3 seconds...\n")
        time.sleep(3)
        
        # Play through all rooms
        self.room_1_dusty_library()
        self.rooms_completed = 1
        
        self.room_2_dark_basement()
        self.rooms_completed = 2
        
        self.room_3_haunted_bedroom()
        self.rooms_completed = 3
        
        self.room_4_ritual_chamber()
        
        self.display_end_screen()

def main():
    """Entry point of the game"""
    game = EscapeRoomGame()
    game.play()
    
    # Ask if player wants to play again
    while True:
        play_again = input("Play again? (yes/no): ").lower().strip()
        if play_again in ['yes', 'y']:
            game = EscapeRoomGame()
            game.play()
        elif play_again in ['no', 'n']:
            print("\nGoodbye, survivor...\n")
            break
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
