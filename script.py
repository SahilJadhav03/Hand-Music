import pygame.midi
pygame.midi.init()
print(f"Default Output ID: {pygame.midi.get_default_output_id()}")
print("Available MIDI devices:")
for i in range(pygame.midi.get_count()):
    print(f"Device {i}: {pygame.midi.get_device_info(i)}")
pygame.midi.quit()