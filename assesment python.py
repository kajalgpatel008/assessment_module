
"""
E-Notebook Console-Based Application
Author: Kajal Patel
Description: This is a Python-based console application to manage notes with file handling.
Operations: Generate Note, View Note, Exit
"""

import os
import datetime

# File where notes will be stored
NOTES_FILE = "notes.txt"
LOG_FILE = "log.txt"


def display_menu():
    """Display the main menu to the user."""
    print("\n" + "="*40)
    print("       📘 PYTHON E-NOTEBOOK 📘")
    print("="*40)
    print("1. Generate Note")
    print("2. View Notes")
    print("3. Exit")
    print("="*40)


def generate_note():
    """Allow the user to enter and save a note."""
    print("\n--- 📝 Generate a New Note ---")
    while True:
        name = input("Enter E-Note Generator Name: ").strip()
        if not name.replace(" ","").isalpha():
            print("Invalid input! Name must contain only letteres(no number or symbols).Try again.")
            continue
        break
    title = input("Enter E-Note Title: ").strip()
    content = input("Enter E-Note Content: ").strip()

    if not title or not content:
        print("⚠ Title and content cannot be empty! Try again.")
        return

    try:
        with open(NOTES_FILE, 'a', encoding='utf-8') as file:
            file.write(f"Title: {title}\n")
            file.write(f"Content: {content}\n")
            file.write(f"Timestamp: {datetime.datetime.now()}\n")
            file.write("-" * 40 + "\n")

        with open(LOG_FILE, 'a', encoding='utf-8') as log:
            log.write(f"Note Created - Title: {title} at {datetime.datetime.now()}\n")

        print("✅ Note saved successfully!")
    except Exception as e:
        print(f"❌ Error saving note: {e}")


def view_notes():
    """Display all saved notes."""
    print("\n--- 📖 Viewing All Notes ---")
    if not os.path.exists(NOTES_FILE):
        print("📭 No notes found.")
        return

    try:
        with open(NOTES_FILE, 'r', encoding='utf-8') as file:
            content = file.read()
            if content.strip():
                print(content)
            else:
                print("📭 No notes available.")
    except Exception as e:
        print(f"❌ Error reading notes: {e}")


def main():
    """main function use to run in loop"""
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            generate_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            print("👋 Thank you for using E-Notebook. Goodbye!")
            break
        else:
            print("⚠ Invalid option!Please try again.")


#entry point

if __name__=="__main__":
    main()



