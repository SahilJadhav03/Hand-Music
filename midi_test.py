import pygame.midi
import time

pygame.midi.init()

device_id = 3  # Microsoft GS Wavetable Synth
print(f"🎵 Testing MIDI device ID: {device_id}")

try:
    player = pygame.midi.Output(device_id)
    player.set_instrument(0)  # Set to Acoustic Grand Piano

    print("🎹 Playing test note...")
    player.note_on(60, 127)  # Play Middle C
    time.sleep(2)  # Hold note for 2 seconds
    player.note_off(60, 127)  # Stop note

    player.close()
    print("✅ Test complete, MIDI is working.")

except pygame.midi.MidiException as e:
    print(f"⚠️ MIDI Error: {e}")

pygame.midi.quit()
